def sxhmatismosGrammhs(sthles,pinakas,y):
    """
    >>> pinakas=[[1,2,0],[3,2,1],[1,3,2]]  
    >>> sxhmatismosGrammhs(3,pinakas,2)    #doctest: +SKIP
    '  O|  *|  X|'
    """
    """
    sthles --> Αριθμός στηλών πίνακα.
    pinakas --> Λίστα που περιέχει τα στοιχεία κάθε γραμμής του πίνακα σε εμφωλευμένες λίστες.
    y --> Η γραμμή που θα δημιουργηθεί.
    Δημιουργία μιάς γραμμής του πίνακα κάθε φορά που καλείται από την συνάρτηση g1.
    """
    
    px=["\t "+"|","\tX"+"|","\tO"+"|","\t*"+"|"]
    sum=""
    i=0
    while i<=sthles-1:
        if pinakas[y][i]==0:                    
            sum=sum+px[0]
        elif pinakas[y][i]==1:
            sum=sum+px[2]
        elif pinakas[y][i]==2:
            sum=sum+px[1]
        elif pinakas[y][i]==3:
            sum=sum+px[3]
        elif pinakas[y][i]==4:
            sum=sum+px[0]
        i+=1
    return sum

def g1(sthles,pinakas):
    """
    Εμφάνιση πίνακα με πολλαπλές for για κάθε γραμμή. 
    sthles --> Αριθμός στηλών πίνακα.
    pinakas --> Λίστα που περιέχει τα στοιχεία κάθε γραμμής του πίνακα σε εμφωλευμένες λίστες.
    """
    grammata=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    row1=[i for i in range(sthles)]
    for k in range(sthles):
        print("   "+str(row1[k]+1), end="\t")
    print("\n")
    for r in range(8*sthles):
        print("-", end="")
    print("\n")
    for y in range(sthles):
            line=sxhmatismosGrammhs(sthles,pinakas,y)
            print(grammata[y]+"|"+line)
    for x in range(8*sthles):
        print("-", end="")
    print("\n")

def tamplo(sthles):
    """
    >>> tamplo(5)
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    >>> tamplo(6)
    [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    >>> pinakas=tamplo(10)
    >>> len(pinakas)
    10
    >>> pinakas[0][5]
    0
    """
    """
    Δημιουργεί και επιστρέφει έναν αρχικό πίνακα με όλες τις θέσεις κενές.
    sthles --> Ακέραιος αριθμός που ορίζει το μέγεθος του πίνακα.
    """
    board = [[0 for i in range(sthles)] for j in range(sthles)]
    return board