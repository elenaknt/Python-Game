from checks import *
from display import *
from io_utils import *
from moves import *
from scoring import *

apanthsh=input("Καλώς ορίσατε στο παιχνίδι! \nΘα θέλατε να ξεκινήσετε καινούργιο παιχνίδι (Ν) ή να συνεχίσετε ένα αποθηκεύμενο (S); ")
pinakas,sthles,s1,s2=arxi_paixnidiou(apanthsh)                  #Ορίζεται ο αρχικός πίνακας (για νέο ή αποθηκευμένο παιχνίδι)
four1, four2 = False, False                                     #Ξεκινάει το κοινό κομμάτι για νέο και αποθηκευμένο
w="a"                       
telos=False
while w!="s":
    if gematospinakas(pinakas,sthles)==True and telos==False:   #Ελέγχει αν ο πίνακας είναι γεμάτος (μετά από επιλογή πιονιού του παίκτη 2)    
        print('Τέλος παιχνιδιού!')
        telos=True
    else:
        pinakas,four1=elegxosPinaka1(pinakas, sthles)           #Γίνεται ο έλεγχος για πιθανές τετράδες του παίκτη 1 (μετά από επιλογή πιονιού του παίκτη 2)
        if four1==True:         
            g1(sthles,pinakas)                                  #Εμφανίζει τον πίνακα
            s1=score1(s1,pinakas,sthles)                        #Μετράει το σκορ του παίκτη 1
            while four1==True:                                  #Ελέγχει επαναληπτικά για τετράδες του παίκτη 1 μέχρι να μην υπάρχουν
                pinakas=mhdenismos(pinakas,sthles)              #Μηδενίζει τις τετράδες αν υπήρξαν
                flag=False
                while flag==False:                              #Κάνει επαναληπτικά ολίσθηση μέχρι να μην υπάρχουν άλλα στοιχεία για να την κάνει 
                    pinakas, flag =olisthish(pinakas,sthles) 
                gyroi(four1,four2)                              #Εμφανίζει τον νικητή του γύρου
                pinakas,four1=elegxosPinaka1(pinakas, sthles)
                if four1==True:                                  
                   g1(sthles,pinakas)
                   s1=score1(s1,pinakas,sthles)
        epilogh1=int(input("\nΠαίκτη 1, επίλεξε έναν αριθμό στήλης: "))
        while epilogh1<1 or epilogh1>sthles:                    #Γίνεται έλεγχος της επιλογής στήλης του παίκτη 1
            epilogh1=int(input('Παίκτη 1 έχεις επιλέξει λάθος αριθμό στήλης! \nΕπίλεξε έναν ακέραιο αριθμό στήλης εντός των ορίων: '))
        pinakas=elegxosPaikth1(epilogh1, pinakas,sthles)        #Γίνεται ο έλεγχος αν η στήλη είναι γεμάτη και τοποθετεί το πιόνι  
        pinakas,four1=elegxosPinaka1(pinakas, sthles)           #Γίνεται ο έλεγχος για πιθανές τετράδες του παίκτη 1 (μετά από επιλογή πιονιού του παίκτη 1)
        g1(sthles,pinakas)                                      #Εμφανίζει τον πίνακα
        while four1==True:                                      #Ελέγχει επαναληπτικά για τετράδες του παίκτη 1 μέχρι να μην υπάρχουν
            s1=score1(s1,pinakas,sthles)                        #Μετράει το σκορ του παίκτη 1
            pinakas=mhdenismos(pinakas,sthles)                  #Μηδενίζει τις τετράδες αν υπήρξαν
            flag=False
            while flag==False:                                  #Κάνει επαναληπτικά ολίσθηση μέχρι να μην υπάρχουν άλλα στοιχεία για να την κάνει
                pinakas, flag =olisthish(pinakas,sthles)                
            gyroi(four1,four2)                                  #Εμφανίζει τον νικητή του γύρου
            pinakas,four1=elegxosPinaka1(pinakas, sthles)
            if four1==True:                                     
                g1(sthles,pinakas)
#Παίκτης 2
    if gematospinakas(pinakas,sthles)==True and telos==False:   #Ελέγχει αν ο πίνακας είναι γεμάτος (μετά από επιλογή πιονιού του παίκτη 1)
        print('Τέλος παιχνιδιού!')
        telos=False
    else:
        pinakas,four2=elegxosPinaka2(pinakas, sthles)           #Γίνεται ο έλεγχος για πιθανές τετράδες του παίκτη 2 (μετά από επιλογή πιονιού του παίκτη 1)
        if four2==True:                                         
            s2=score2(s2,pinakas,sthles)                        #Μετράει το σκορ του παίκτη 2
            g1(sthles,pinakas)                                  #Εμφανίζει τον πίνακα
            while four2==True:                                  #Ελέγχει επαναληπτικά για τετράδες του παίκτη 2 μέχρι να μην υπάρχουν
                pinakas=mhdenismos(pinakas,sthles)              #Μηδενίζει τις τετράδες αν υπήρξαν
                flag=False
                while flag==False:                              #Κάνει επαναληπτικά ολίσθηση μέχρι να μην υπάρχουν άλλα στοιχεία για να την κάνει
                    pinakas, flag =olisthish(pinakas,sthles)
                gyroi(four1,four2)                              #Εμφανίζει τον νικητή του γύρου
                pinakas,four2=elegxosPinaka2(pinakas,sthles)
                if four2==True:                                 
                    g1(sthles,pinakas)                          
                    s2=score2(s2,pinakas,sthles)
        epilogh2=int(input("\nΠαίκτη 2, επίλεξε έναν αριθμό στήλης: "))           
        while epilogh2<1 or epilogh2>sthles :                   #Γίνεται έλεγχος της επιλογής στήλης του παίκτη 2
            epilogh2=int(input('Παίκτη 2, έχεις επιλέξει λάθος αριθμό στήλης! \nΕπίλεξε έναν ακέραιο αριθμό στήλης εντός των ορίων: '))
        pinakas=elegxosPaikth2(epilogh2, pinakas,sthles)        #Γίνεται ο έλεγχος αν η στήλη είναι γεμάτη και τοποθετεί το πιόνι
        pinakas,four2=elegxosPinaka2(pinakas, sthles)           #Γίνεται ο έλεγχος για πιθανές τετράδες του παίκτη 2 (μετά από επιλογή πιονιού του παίκτη 2) 
        g1(sthles,pinakas)                                      #Εμφανίζει τον πίνακα
        while four2==True:                                      #Ελέγχει επαναληπτικά για τετράδες του παίκτη 2 μέχρι να μην υπάρχουν
            s2=score2(s2,pinakas,sthles)                        #Μετράει το σκορ του παίκτη 2
            pinakas=mhdenismos(pinakas,sthles)                  #Μηδενίζει τις τετράδες αν υπήρξαν
            flag=False
            while flag==False:                                  #Κάνει επαναληπτικά ολίσθηση μέχρι να μην υπάρχουν άλλα στοιχεία για να την κάνει
                pinakas, flag =olisthish(pinakas,sthles)
            gyroi(four1,four2)                                  #Εμφανίζει τον νικητή του γύρου
            pinakas,four2=elegxosPinaka2(pinakas,sthles)
            if four2==True:                                     
                g1(sthles,pinakas)
        print("\nΤο σκορ είναι: ",s1,"-",s2)                    #Εμφανίζει μετά την επιλογή του παίκτη 2 το σκορ τους
        w=input('Πιέστε "s" για αποθήκευση του παιχνιδιού ή οποιοδήποτε άλλο πλήκτρο για να συνεχίσετε: ')
    if telos==True:                                             #Αν ο πίνακας είναι γεμάτος θα τελειώνει το παιχνίδι με την αποθήκευση του εμφανίζοντας νικητή
        w=nikhths(s1,s2)
filename=input("Δώστε όνομα για το αρχείο: ")                   #Ζητά όνομα για την αποθήκευση
save(filename,sthles,pinakas,s1,s2)                             #Το αποθηκεύει

