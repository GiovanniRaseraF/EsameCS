# Esercizio 4
import math
# Utils:
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
    while(True):
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
        riprovare = input("Vuoi riprovare? (s,n): ")
        riprovare = riprovare[0]

        if riprovare == "n":
            break

    # 3) Fattorizzazione
    print("Fattorizzazione:")
    ## 3.1) G1
    pivot = A[0][0]
    g1_10 = "-("+A[1][0]+"/"+pivot+")"
    g1_20 = "-("+A[2][0]+"/"+pivot+")"
    G1 = [
        ["1",       "0",        "0"], 
        [g1_10,     "1",        "0"],
        [g1_20,     "0",        "1"]
    ]
    print("G1: (Interessanti)")
    print("G1(1,0): \n"+ g1_10, end="");input()
    print("G1(2,0): \n"+ g1_20, end="");input()

    ## 3.2) G1A
    g1a_11 = "("+G1[1][0]+"*("+A[0][1]+")+"+A[1][1]+")"
    g1a_12 = "("+G1[1][0]+"*("+A[0][2]+")+"+A[1][2]+")"
    g1a_21 = "("+G1[2][0]+"*("+A[0][1]+")+"+A[2][1]+")"
    g1a_22 = "("+G1[2][0]+"*("+A[0][2]+")+"+A[2][2]+")"
    G1A = [
        [A[0][0],   A[0][1],        A[0][2]], 
        ["0",       g1a_11,         g1a_12],
        ["0",       g1a_21,         g1a_22]
    ]
    print("G1A: (Interessanti)")
    print("G1A(1,1): \n"+ g1a_11, end="");input()
    print("G1A(1,2): \n"+ g1a_12, end="");input()
    print("G1A(2,1): \n"+ g1a_21, end="");input()
    print("G1A(2,2): \n"+ g1a_22, end="");input()

    ## 3.3) G2
    pivot = G1A[1][1]
    g2_21 = "-("+G1A[2][1]+")\n/\n"+pivot
    G2 = [
        ["1",       "0",        "0"], 
        ["0",       "1",        "0"],
        ["0",       g2_21,      "1"]
    ]
    print("G2: (Interessanti)")
    print("G2(2,1): \n"+G2[2][1], end="")
    input()

    ## 3.4) G2G1A
    g2g1a_22 = g2_21+"*"+g1a_12+"\n+\n"+g1a_22
    G2G1A = [
        [A[0][0],   A[0][1],    A[0][2]], 
        ["0",       g1a_11,     g1a_12],
        ["0",       "0",        g2g1a_22]
    ]
    print("G2G1A: (Interessanti)")
    print("G2G1A(2,2): \n"+G2G1A[2][2], end="")
    input()

    ## 3.5) Conclusioni
    print("U = G2G1A")
    print("L = G1^-1 * G2^-1")
    l_10 = "-("+g1_10+")"
    l_20 = "-("+g1_20+")"
    l_21 = "-("+g2_21+")"
    L = [
        ["1",       "0",        "0"], 
        [l_10,      "1",        "0"],
        [l_20,      l_21,       "1"]
    ]
    print("L: (Importanti)")
    print("L(1,0): \n"+ l_10, end="");input()
    print("L(1,0): \n"+ l_20, end="");input()
    print("L(2,1): \n"+ l_21, end="");input()
    input()

    # Menu
    while(True):
        print("Menu: ")
        print("(A a)(G1 g1)(G2 g2)\n(G1A g1a)(G2G1A g2g1a)\n(U u)(L l)\n(Fine f)")
        stampa = input().lower()
        if stampa == "a":
            stampaMatrice(A, RIGHE, COLONNE)
            input()
        elif stampa == "g1":
            stampaMatrice(G1, RIGHE, COLONNE)
            input()
        elif stampa == "g2":
            stampaMatrice(G2, RIGHE, COLONNE)
            input()
        elif stampa == "g1a":
            stampaMatrice(G1A, RIGHE, COLONNE)
            input()
        elif stampa == "g2g1a":
            stampaMatrice(G2G1A, RIGHE, COLONNE)
            input()
        elif stampa == "u":
            stampaMatrice(G2G1A, RIGHE, COLONNE)
            input()
        elif stampa == "l":
            stampaMatrice(L, RIGHE, COLONNE)
            input()
        else:
            break
    
    # 4) Pivot Parziale
    print("Pivot Parziale:\nUsa Grafici Calcolatrice")

    # 5) PA = LU
    ## 5.1) Inserimento di a e b
    a = int(input("Valore di a: "))
    b = 0
    b = (input("Valore di b: (0 se non presente)"))
    if b == "":
        b = 0

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
    pivot = A_PA[0][0]
    g1_10 = A_PA[1][0] / pivot
    g1_20 = A_PA[2][0] / pivot
    G1 = [
        [1,0,0],
        [g1_10,1,0],
        [g1_20,0,1]
    ]
    print("G1: ")
    stampaMatriceInt(G1, RIGHE, COLONNE)
    input()



Main()