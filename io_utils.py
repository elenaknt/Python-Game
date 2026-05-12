from display import *

def fortwsh(onoma):
    """  
    Γίνεται η φόρτωση παιχνιδιού από αρχείο.
    Δημιουργεί πίνακα που περιέχει κάθε γραμμή του αρχείου σε εμφωλευμένη λίστα βγάζοντας κάθε περιττό
    χαρακτήρα, χωρίζοντας τα στοιχεία από το "," και αλλάζοντας τα στοιχεία από string σε integer.
    Το ίδιο κάνει και με το σκορ των παικτών (s1,s2) και βάζει στη μεταβλητή sthles τον αριθμό 
    των στηλών.  
    Επιστρέφει τον πίνακα, τις στήλες και το σκορ στο πρόγραμμα.
    onoma --> Το όνομα που έδωσε ο παίκτης για φόρτωση του αρχείου.  
    """                    
    f = open(onoma,'r')
    ls=f.readlines()
    pinakas=[]
    skor=ls[len(ls)-1].strip()
    skor=skor.split(',')
    s1=int(skor[0])
    s2=int(skor[1])
    for i in range(len(ls)-1):
        x=ls[i].strip()
        x=x.split(',')
        pinakas.append(x)
    for i in range(len(pinakas)):
        for j in range(len(pinakas)):
            pinakas[i][j]=int(pinakas[i][j])
    sthles=len(pinakas)
    return sthles,pinakas,s1,s2

def save(filename,sthles,pinakas,s1,s2):
    """
    >>> pinakas=[[0,0,0,0,0],[1,1,1,1,1],[2,2,2,2,2],[2,1,2,1,1],[1,2,1,2,1]]
    >>> sthles=5
    >>> filename='dokimastiko.csv'
    >>> s1=7
    >>> s2=9
    >>> save(filename,sthles,pinakas,s1,s2)
    """
    """
    Κάνει αποθήκευση του παιχνιδιού.
    Κάθε γραμμή του πίνακα (εμφωλευμένη λίστα) γίνεται λίστα με string στοιχεία τα οποία
    ενώνονται σαν ένα μεγάλο string και χωρίζονται με "," ενώ αλλάζει γραμμή για την επόμενη 
    εμφωλευμένη λίστα του πίνακα και έτσι δημιουργείται αρχείο για αποθήκευση μαζί με το σκορ 
    στη τελευταία γραμμή.
    filename --> Όνομα αρχείου που δίνει ο χρήστης για αποθήκευση.
    s1, s2 --> Σκορ του κάθε παίκτη.
    sthles --> Αριθμός στηλών πίνακα.
    pinakas --> Λίστα που περιέχει τα στοιχεία κάθε γραμμής του πίνακα σε εμφωλευμένες λίστες.
    """
    def ls_to_str(pinakas,i):
        nls=[]
        for j in range(len(pinakas)):
            if pinakas[i][j]==1:
                nls.append('1')
            elif pinakas[i][j]==2:
                nls.append('2')
            elif pinakas[i][j]==0:
                nls.append('0')
        return nls
    f=open(filename,"w")
    s1=str(s1)
    s2=str(s2)
    skor=[s1,s2]
    for i in range(sthles):
        newls=ls_to_str(pinakas,i)
        f.write(','.join(newls)+"\n")
    f.write(','.join(skor)+"\n")
    f.close()

def arxi_paixnidiou(apanthsh):
    """
    Ξεκινάει το παιχνίδι είτε με δημιουργία νέου είτε με φόρτωση αποθηκευμένου.
    Επιστρέφοντας τον πίνακα, τις στήλες και το σκορ κάθε παίκτη.
    apanthsh --> Τιμή string για δήλωση απάντησης.
    """
    if apanthsh=="N":
        temp=int(input("Enter an integer between 5 and 10 (rows/columns): "))
        while temp<5 or temp>10 or int(temp)!=temp:
            temp=int(input("Enter an integer between 5 and 10 (rows/columns): "))
        sthles=temp
        pinakas=tamplo(sthles)
        g1(sthles,pinakas)
        s1=0
        s2=0
    elif apanthsh=="S":
        onoma=input("Enter the file name: ")
        sthles,pinakas,s1,s2=fortwsh(onoma)
        g1(sthles,pinakas)
    return pinakas,sthles,s1,s2