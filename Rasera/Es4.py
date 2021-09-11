# Esercizio 4
import math
# Utils:
def multiplyMatrix(A, B):
    R_A = len(A); C_A = len(A[0])
    R_B = len(B); C_B = len(B[0])
    K = []
      
    for i in range(0,R_A):
        K_row = []
        for j in range(0,C_B):
            K_row.append(0)
        K.append(K_row)

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                K[i][j] += A[i][k] * B[k][j]
    
    return K

def stampaMatrice(Mat, R, C):
    for riga in range(0, R):
        print("", end="")
        for colonna in range(0, C):
            val = (Mat[riga][colonna]).replace('\n', '')
            print(val+"  ", end="")
        print("", end="\n")

def stampaMatriceInt(Mat, R, C):
    for riga in range(0, R):
        print("", end="")
        for colonna in range(0, C):
            val = "{:.2f}".format(Mat[riga][colonna])
            print(val+"  ", end="")
        print("", end="\n")

def trovaMatricediPermutazioneP1(A_PA):
    maxVal = max([abs(A_PA[0][0]), abs(A_PA[1][0]), abs(A_PA[2][0]),])
    P1A = []

    if maxVal == abs(A_PA[0][0]):
        P1 =  [[1,0,0],[0,1,0],[0,0,1]]
        P1A = A_PA
    elif maxVal == abs(A_PA[1][0]):
        P1 =  [[0,1,0],[1,0,0],[0,0,1]]
        P1A = []
        P1A.append(A_PA[1])
        P1A.append(A_PA[0])
        P1A.append(A_PA[2])
    else:
        P1 =  [[0,0,1],[0,1,0],[1,0,0]]
        P1A = []
        P1A.append(A_PA[2])
        P1A.append(A_PA[1])
        P1A.append(A_PA[0])

    return P1, P1A  

def allameno1(M):
    RIGHE = 3
    COLONNE = 3
    VUOTO = 0
    RES = [
        [VUOTO, VUOTO, VUOTO], 
        [VUOTO, VUOTO, VUOTO],
        [VUOTO, VUOTO, VUOTO]
    ]

    for riga in range(0, RIGHE):
        for colonna in range(0, COLONNE):
            # Inseriemnto valore per valore
            if M[riga][colonna] != 0 and M[riga][colonna] != 1:
                RES[riga][colonna] = -M[riga][colonna]
            else:
                RES[riga][colonna] = M[riga][colonna]

    return RES

def trovaMatricediPermutazioneP2(G1P1A):
    maxVal = max([abs(G1P1A[1][1]), abs(G1P1A[2][1])])
    P2 = []

    if maxVal == abs(G1P1A[1][1]):
        P2 = [[1,0,0],[0,1,0],[0,0,1]]
    else:
        P2 = [[1,0,0],[0,0,1],[0,1,0]]
    
    return P2


# Main:
def Main():
    # Composizione della matrice
    print(
    """
Matrice: (y,x)
| 0,0 0,1 0,2 |
| 1,0 1,1 1,2 | 
| 2,0 2,1 2,2 |
    """
    ,end="")
    input()

    # 1) Inseriemento di A
    riprovare = "s"
    VUOTO = ""
    RIGHE = 3
    COLONNE = 3
    A = [
        [VUOTO, VUOTO, VUOTO], 
        [VUOTO, VUOTO, VUOTO],
        [VUOTO, VUOTO, VUOTO]
    ]

    print("-- Inserisci A --")
    print("HINT: Puoi inserire anche variabili")
    for riga in range(0, RIGHE):
        for colonna in range(0, COLONNE):
            # Inseriemnto valore per valore
            A[riga][colonna] = input("("+str(riga)+","+str(colonna)+")= ")
            
    # 2) Controlla
    print("A: ")
    stampaMatrice(A, RIGHE, COLONNE)
    input()

    # 5) PA = LU
    print("PA = LU")
    ## 5.2) Calocolo di A_PA
    A_PA = [
        [VUOTO, VUOTO, VUOTO], 
        [VUOTO, VUOTO, VUOTO],
        [VUOTO, VUOTO, VUOTO]
    ]
    for riga in range(0, RIGHE):
        for colonna in range(0, COLONNE):
            # Inseriemnto valore per valore
            A_PA[riga][colonna] = eval(A[riga][colonna])

    print("A_PA: ")
    stampaMatriceInt(A_PA, RIGHE, COLONNE)
    input()

    ## 5.3) Trova P1
    P1, P1A = trovaMatricediPermutazioneP1(A_PA)

    print("P1: ")
    stampaMatriceInt(P1, RIGHE, COLONNE)
    input()
    print("P1A: ")
    stampaMatriceInt(P1A, RIGHE, COLONNE)
    input()

    ## 5.4) Trova G1
    pivot = P1A[0][0]
    g1_10 = -P1A[1][0] / pivot
    g1_20 = -P1A[2][0] / pivot
    G1 = [
        [1,0,0],
        [g1_10,1,0],
        [g1_20,0,1]
    ]
    print("G1: ")
    stampaMatriceInt(G1, RIGHE, COLONNE)
    input()

    ## 5.5) Trova G1P1A
    G1P1A = multiplyMatrix(G1, P1A)
    print("G1P1A: ")
    stampaMatriceInt(G1P1A, RIGHE, COLONNE)
    input()

    ## 5.6) Trova P2
    P2 = trovaMatricediPermutazioneP2(G1P1A)
    print("P2: ")
    stampaMatriceInt(P2, RIGHE, COLONNE)
    input()

    ## 5.7) Trova P2G1P1A
    P2G1P1A = multiplyMatrix(P2, G1P1A)
    print("P2G1P1A: ")
    stampaMatriceInt(P2G1P1A, RIGHE, COLONNE)
    input()

    ## 5.8) Trova G2
    pivot = P2G1P1A[1][1]
    g2_21 = -P2G1P1A[2][1] / pivot
    G2 = [
        [1,0,0],
        [0,1,0],
        [0,g2_21,1]
    ]
    print("G2: ")
    stampaMatriceInt(G2, RIGHE, COLONNE)
    input()

    ## 5.9) Trova G2P2G1P1A
    G2P2G1P1A = multiplyMatrix(G2, P2G1P1A)
    print("G2P2G1P1A: ")
    stampaMatriceInt(G2P2G1P1A, RIGHE, COLONNE)
    input()

    ## 5.10) Trova L
    G1_i = allameno1(G1)
    G2_i = allameno1(G2)

    P2G2_i = multiplyMatrix(P2, G2_i)
    G1_iP2G2_i = multiplyMatrix(G1_i, P2G2_i)
    L = multiplyMatrix(P2, G1_iP2G2_i)
    print("L: ")
    stampaMatriceInt(L, RIGHE, COLONNE)

Main()