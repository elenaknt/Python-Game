def orizontia1(pinakas,sthles):
    """
    >>> pinakas=[[1,1,1,1,1],[2,5,6,7,7],[0,1,1,1,1],[8,7,8,7,7],[0,1,1,1,1]]
    >>> orizontia1(pinakas,5)
    ([[3, 3, 3, 3, 4], [2, 5, 6, 7, 7], [0, 3, 3, 3, 3], [8, 7, 8, 7, 7], [0, 3, 3, 3, 3]], True)
    >>> pinakas=[[1,1,1,1,0,1],[2,5,6,7,5,7],[0,1,1,1,5,1],[8,7,8,7,5,7],[1,0,1,1,1,1],[1,1,1,1,1,1]]
    >>> orizontia1(pinakas,6)
    ([[3, 3, 3, 3, 0, 1], [2, 5, 6, 7, 5, 7], [0, 1, 1, 1, 5, 1], [8, 7, 8, 7, 5, 7], [1, 0, 3, 3, 3, 3], [3, 3, 3, 3, 4, 4]], True)
    """
    """
    Ελέγχει για ύπαρξη τετράδας του παίκτη 1 οριζόντια επιστρέφοντας την 
    τιμή True αν υπάρχει, αλλιώς False. Αν υπάρχει μετατρέπει
    την τετράδα σε '3' και τα γειτονικά πιόνια του ίδιου παίκτη σε '4'.
    sthles --> Αριθμός στηλών πίνακα.
    pinakas --> Λίστα που περιέχει τα στοιχεία κάθε γραμμής του πίνακα σε εμφωλευμένες λίστες.
    """
    four1=False
    for i in range(sthles):
        c1=0
        for j in range(sthles):
            if pinakas[i][j]==1:
                c1+=1
            else:
                c1=0
            if c1==4:
                four1=True
                for a in range(j-3,j+1):
                    pinakas[i][a]=3
                #Έλεγχος πιονιών στην ίδια διεύθυνση με την τετράδα
                for b in range(j-4,-1,-1):                  
                    if (pinakas[i][b+1]==3 or pinakas[i][b+1]==4) and pinakas[i][b]==1:
                        pinakas[i][b]=4
                for c in range(j+1,sthles):
                    if (pinakas[i][c-1]==3 or pinakas[i][c-1]==4) and pinakas[i][c]==1:
                        pinakas[i][c]=4
    return pinakas,four1

def orizontia2(pinakas,sthles):
    """
    >>> pinakas=[[2,2,2,2,2],[2,5,6,7,7],[0,2,2,2,2],[8,7,8,7,7],[0,2,2,2,2]]
    >>> orizontia2(pinakas,5)
    ([[3, 3, 3, 3, 4], [2, 5, 6, 7, 7], [0, 3, 3, 3, 3], [8, 7, 8, 7, 7], [0, 3, 3, 3, 3]], True)
    >>> pinakas=[[2,2,2,2,0,2],[2,5,6,7,5,7],[0,2,2,2,5,2],[8,7,8,7,5,7],[2,0,2,2,2,2],[2,2,2,2,2,2]]
    >>> orizontia2(pinakas,6)
    ([[3, 3, 3, 3, 0, 2], [2, 5, 6, 7, 5, 7], [0, 2, 2, 2, 5, 2], [8, 7, 8, 7, 5, 7], [2, 0, 3, 3, 3, 3], [3, 3, 3, 3, 4, 4]], True)
    """
    """
    Ελέγχει για ύπαρξη τετράδας του παίκτη 2 οριζόντια επιστρέφοντας την 
    τιμή True αν υπάρχει, αλλιώς False. Αν υπάρχει μετατρέπει
    την τετράδα σε '3' και τα γειτονικά πιόνια του ίδιου παίκτη σε '4'.
    sthles --> Αριθμός στηλών πίνακα.
    pinakas --> Λίστα που περιέχει τα στοιχεία κάθε γραμμής του πίνακα σε εμφωλευμένες λίστες.
    """
    four2=False
    for i in range(sthles):
        c=0
        for j in range(sthles):
            if pinakas[i][j]==2:
                c+=1
            else:
                c=0
            if c==4:
                four2=True
                for a in range(j-3,j+1):
                    pinakas[i][a]=3
                #Έλεγχος πιονιών στην ίδια διεύθυνση με την τετράδα
                for b in range(j-4,-1,-1):                  
                    if (pinakas[i][b+1]==3 or pinakas[i][b+1]==4) and pinakas[i][b]==2:
                        pinakas[i][b]=4
                for c in range(j+1,sthles):
                    if (pinakas[i][c-1]==3 or pinakas[i][c-1]==4) and pinakas[i][c]==2:
                        pinakas[i][c]=4
    return pinakas,four2