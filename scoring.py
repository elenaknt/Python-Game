def nikhths(s1,s2):
    """
    >>> nikhths(10,11) #doctest: +SKIP
    "Congratulations! Player 2 is the winner!"
    >>> nikhths(20,11) #doctest: +SKIP
    "Congratulations! Player 1 is the winner!"
    >>> nikhths(10,10) #doctest: +SKIP
    "The game ended in a draw. No winner this time!"
    >>> nikhths(0,0) #doctest: +SKIP
    "The game ended in a draw. No winner this time!"
    """
    """
    Παίρνει τα τελικά σκορ κάθε παίκτη τα εμφανίζει και έπειτα 
    αφού κάνει σύγκριση εμφανίζει μήνυμα με τον νικητή. Τέλος
    αυτή η συνάρτηση καλείται όταν ο πίνακας έχει γεμίσει 
    οπότε το παιχνίδι δεν μπορεί να συνεχιστεί και ζητείται 
    η αποθήκευση του.
    """
    print("Final score: ",s1,"-",s2)                        
    if s1>s2:
        print("Congratulations! Player 1 is the winner!")
    elif s2>s1:
        print("Congratulations! Player 2 is the winner!")
    elif s1==s2:
        print("The game ended in a draw. No winner this time!")
    
    while w!="s":                                           
        w=input("Press 's' to save the game: ")
    return w

def mhdenismos(pinakas,sthles):
    """
    >>> pinakas=[[3,2,2,1],[1,3,2,1],[1,2,3,4],[2,1,2,3]]
    >>> mhdenismos(pinakas,4)
    [[0, 2, 2, 1], [1, 0, 2, 1], [1, 2, 0, 0], [2, 1, 2, 0]]
    >>> pinakas=[[1,2,2,1,3],[1,2,3,1,2],[1,3,2,3,4],[2,1,2,3,3],[3,2,1,2,1]]
    >>> mhdenismos(pinakas,5)
    [[1, 2, 2, 1, 0], [1, 2, 0, 1, 2], [1, 0, 2, 0, 0], [2, 1, 2, 0, 0], [0, 2, 1, 2, 1]]
    """
    """
    Μηδενίζει τα στοιχεία που σχημάτισαν τετράδα και τα ίδια πιόνια στη διεύθυνση της τετράδας
    ώστε να γίνει η ολίσθηση των απο πάνω. 
    sthles --> Αριθμός στηλών πίνακα.
    pinakas --> Λίστα που περιέχει τα στοιχεία κάθε γραμμής του πίνακα σε εμφωλευμένες λίστες.
    """
    for i in range(sthles):
        for j in range(sthles):
            if pinakas[i][j]==3 or pinakas[i][j]==4:
                pinakas[i][j]=0
    return pinakas

def olisthish(pinakas,sthles):
    """
    >>> pinakas=[[0,2,2,1],[1,0,2,1],[1,2,0,4],[2,1,2,0]]
    >>> olisthish(pinakas,4)
    ([[0, 0, 0, 1], [1, 2, 2, 1], [1, 2, 2, 4], [2, 1, 2, 0]], False)
    >>> pinakas=[[1,2,2,0,1],[1,0,2,1,2],[0,1,0,2,1],[1,0,2,0,0],[0,0,0,0,1]]
    >>> olisthish(pinakas,5)
    ([[0, 0, 0, 0, 0], [1, 2, 2, 0, 1], [1, 0, 2, 1, 2], [0, 1, 0, 2, 1], [1, 0, 2, 0, 1]], False)
    >>> pinakas=[[1,2,2,0,1],[1,1,2,1,2],[2,1,1,2,1],[1,1,2,1,1],[1,1,1,1,1]]
    >>> olisthish(pinakas,5)
    ([[1, 2, 2, 0, 1], [1, 1, 2, 1, 2], [2, 1, 1, 2, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1]], True)
    """
    """
    Γίνεται ολίσθηση των στοιχείων που βρίσκονταν πάνω από αυτά που σχημάτισαν τετράδα ή των 
    αντίστοιχων γειτονικών της τετράδας και μηδενίστηκαν.
    sthles --> Αριθμός στηλών πίνακα.
    pinakas --> Λίστα που περιέχει τα στοιχεία κάθε γραμμής του πίνακα σε εμφωλευμένες λίστες.
    """
    flag=True
    for i in range(sthles-1,0,-1):
        k=0
        while k<=sthles-1:
            if pinakas[i][k]==0 and (pinakas[i-1][k]==1 or pinakas[i-1][k]==2):
                pinakas[i][k]=pinakas[i-1][k]
                pinakas[i-1][k]=0
                flag=False
            k+=1
    return pinakas,flag

def score1(s1,pinakas,sthles):  
    """
    >>> pinakas=[[0,2,3,1],[0,0,3,1],[0,2,3,0],[0,1,3,0]]
    >>> score1(10,pinakas,4)
    14
    >>> pinakas=[[4,2,2,0,1],[1,3,2,1,2],[0,1,3,2,1],[1,0,2,3,0],[0,0,0,0,3]]
    >>> score2(20,pinakas,5)
    25
    """            
    """
    Υπολογίζει το σκορ του παίκτη 1 για κάθε πιόνι που αφαιρείται.
    s1 --> Μετρητής του σκορ του παίκτη 1.
    sthles --> Αριθμός στηλών πίνακα.
    pinakas --> Λίστα που περιέχει τα στοιχεία κάθε γραμμής του πίνακα σε εμφωλευμένες λίστες.
    """
    for i in range(sthles):
        for j in range(sthles):
            if pinakas[i][j]==3 or pinakas[i][j]==4:
                s1+=1
    return s1

def score2(s2,pinakas,sthles):  
    """
    >>> pinakas=[[3,2,2,1],[3,0,2,1],[3,2,0,0],[3,1,2,0]]
    >>> score2(0,pinakas,4)
    4
    >>> pinakas=[[3,2,2,0,1],[1,3,2,1,2],[0,1,3,2,1],[1,0,2,3,0],[0,0,0,0,4]]
    >>> score2(0,pinakas,5)
    5
    """          
    """
    Υπολογίζει το σκορ του παίκτη 2 για κάθε πιόνι που αφαιρείται.
    pinakas --> Λίστα που περιέχει τα στοιχεία κάθε γραμμής του πίνακα σε εμφωλευμένες λίστες.
    """ 
    for i in range(sthles):
        for j in range(sthles):
            if pinakas[i][j]==3 or pinakas[i][j]==4:
                s2+=1
    return s2

def gyroi(four1,four2):  
    """
    >>> gyroi(True,False)
    "Congratulations! Player 1 is the winner!"
    >>> gyroi(False,True)
    "Congratulations! Player 2 is the winner!"
    """                       
    """
    Εμφανίζει τον νικητή του κάθε γύρου.
    four1, four2 --> Λογικές τιμές για το ποιός κέρδισε τον γύρο.
    """
    if four1==True:
        print("Congratulations! Player 1 is the winner!")
    elif four2==True:
        print("Congratulations! Player 2 is the winner!")