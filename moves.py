def elegxosPaikth1(epilogh, pinakas,sthles):
    """
    >>> pinakas=[[1,2,0],[3,2,1],[1,3,2]]
    >>> elegxosPaikth1(2,pinakas,3)  #doctest: +SKIP
    This column is full!  
    Choose a different column number: 
    >>> elegxosPaikth1(3,pinakas,3)
    [[1, 2, 1], [3, 2, 1], [1, 3, 2]]
    """
    """
    Γίνεται έλεγχος εγκυρότητας για την επιλογή στήλης του παίκτη 1 (Αν η στήλη είναι γεμάτη εμφανίζει μήνυμα και ξανά ζητάει αριθμό).
    Τοποθετείται το στοιχείο στη πιο χαμηλή κενή θέση του πίνακα.
    epilogh --> Αριθμός στήλης που διάλεξε ο παίκτης να τοποθετήσει το πιόνι του.
    sthles --> Αριθμός στηλών πίνακα.
    pinakas --> Λίστα που περιέχει τα στοιχεία κάθε γραμμής του πίνακα σε εμφωλιασμένες λίστες.
    """
    if pinakas[0][epilogh-1]!=0:
        while pinakas[0][epilogh-1]!=0:
            epilogh=int(input('This column is full! \nChoose a different column number: '))  
    i=sthles-1
    while i>=0:
        if pinakas[i][epilogh-1]==0:
            pinakas[i][epilogh-1]=1
            break
        i-=1
    return pinakas

def elegxosPaikth2(epilogh,pinakas,sthles):
    """
    >>> pinakas=[[1,0,0,1],[1,0,2,3],[2,0,1,1],[2,1,2,3]]
    >>> elegxosPaikth2(2,pinakas,4)
    [[1, 0, 0, 1], [1, 0, 2, 3], [2, 2, 1, 1], [2, 1, 2, 3]]
    >>> elegxosPaikth2(1,pinakas,4)    #doctest: +SKIP
    This column is full! 
    Choose a different column number:  
    >>> elegxosPaikth2(3,pinakas,4)
    [[1, 0, 2, 1], [1, 0, 2, 3], [2, 2, 1, 1], [2, 1, 2, 3]]
    """
    """
    Γίνεται έλεγχος εγκυρότητας για την επιλογή στήλης του παίκτη 2 (Αν η στήλη είναι γεμάτη εμφανίζει μήνυμα και ξανά ζητάει αριθμό).
    Τοποθετείται το στοιχείο στη πιο χαμηλή κενή θέση του πίνακα.
    epilogh --> Αριθμός στήλης που διάλεξε ο παίκτης να τοποθετήσει το πιόνι του.
    sthles --> Αριθμός στηλών πίνακα.
    pinakas --> Λίστα που περιέχει τα στοιχεία κάθε γραμμής του πίνακα σε εμφωλευμένες λίστες.
    """
    if pinakas[0][epilogh-1]!=0:
        while pinakas[0][epilogh-1]!=0:
            epilogh=int(input('This column is full! \nChoose a different column number: '))
    i=sthles-1
    while i>=0:
        if pinakas[i][epilogh-1]==0:
            pinakas[i][epilogh-1]=2
            break
        i-=1
    return pinakas