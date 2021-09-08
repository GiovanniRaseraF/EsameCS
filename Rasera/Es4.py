# Esercizio 4
import math
# Utils:
def stampaMatrice(Mat, R, C):
    for riga in range(0, R):
        print("", end="")
        for colonna in range(0, C):
            print(Mat[riga][colonna]+"  ", end="")
        print("", end="\n")

"""
def prodottoG1A(Mat1, Mat2):
    pass
"""

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
    g1a_11 = ""+G1[1][0]+"*("+A[0][1]+")+"+A[1][1]+""
    g1a_12 = ""+G1[1][0]+"*("+A[0][2]+")+"+A[1][2]+""
    g1a_21 = ""+G1[2][0]+"*("+A[0][1]+")+"+A[2][1]+""
    g1a_22 = ""+G1[2][0]+"*("+A[0][2]+")+"+A[2][2]+""
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


Main()