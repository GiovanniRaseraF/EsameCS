import math
from math import sqrt as sqrt

def MultiplyAndPrintMatrix(A, B):

    R_A = len(A); C_A = len(A[0])
    R_B = len(B); C_B = len(B[0])

    K = []
      
    for i in range(0,R_A):
        K_row = []
        for j in range(0,C_B):
            K_row.append(0)
        K.append(K_row)

    # iterating by row of A
    for i in range(len(A)):
    
        # iterating by column by B
        for j in range(len(B[0])):
    
            # iterating by rows of B
            for k in range(len(B)):
                K[i][j] += A[i][k] * B[k][j]
    
    for i in range(0,R_A):
        for j in range(0,C_B):
            print("{:.2f}".format(K[i][j]) + "  ", end="")
        print()
        


# Main:
def Main():
    # Composizione della matrice
    print(
    """
Matrice: (y,x)
| 0,0 0,1 |
| 1,0 1,1 | 
| 2,0 2,1 |
| 3,0 3,1 |
    """
    ,end="")
    input()

    # 1) Inserimento (X,Y)
    while(True):
        riprovare = "s"
        VUOTO = -100000
        RIGHE = 4
        COLONNE = 2
        Mat = [
            [VUOTO, VUOTO], 
            [VUOTO, VUOTO],
            [VUOTO, VUOTO],
            [VUOTO, VUOTO]
        ]

        """
        print("-- Inserisci Coordinate --")
        print("HINT: Puoi inserire anche variabili")
        for riga in range(0, RIGHE):
            for colonna in range(0, COLONNE):
                # Inseriemnto valore per valore
                Mat[riga][colonna] = eval(input("("+str(riga)+","+str(colonna)+")= "))

        
        x0 = Mat[0][0]
        x1 = Mat[1][0]
        x2 = Mat[2][0]
        x3 = Mat[3][0]
        y0 = Mat[0][1]
        y1 = Mat[1][1]
        y2 = Mat[2][1]
        y3 = Mat[3][1]
        
        """
        x0 = -1
        x1 = 0
        x2 = 1
        x3 = sqrt(3)
        y0 = 1
        y1 = 0
        y2 = 1
        y3 = 2
        
        
        try:
            V1 = (y0 - y1)/(x0 - x1)
        except:
            V1 = 0
        
        try:
            V2 = (y1 - y2)/(x1 - x2)
        except:
            V2 = 0
        
        try:
            V3 = (y2 - y3)/(x2 - x3)
        except:
            V3 = 0

        try:
            V10 = (V1 - V2)/(x0 - x2)
        except:
            V10 = 0

        try:
            V20 = (V2 - V3)/(x1 - x3)
        except:
            V20 = 0

        try:
            V100 = (V10 - V20)/(x0 - x3)
        except:
            V100 = 0
        
        


        print("-------------------")
        print(V1)
        print("     " + "{:.2f}".format(V10))
        print("{:.2f}".format(V2) + "        " + "{:.2f}".format(V100)) 
        print("     " + "{:.2f}".format(V20))
        print("{:.2f}".format(V3))
        print("-------------------")



        print("p(x):")
        print("{:.1f}".format(y0) + "+(x-" + "{:.1f}".format(x0) +")*" + "{:.1f}".format(V1) + "+")
        print("+(x-" + "{:.1f}".format(x0) +")*(x-" + "{:.1f}".format(x1) +")*" + "{:.1f}".format(V10))
        print("---------------------")

        
        print("p(x) completo:")
        print("{:.1f}".format(y0) + "+(x-" + "{:.1f}".format(x0) +")*" + "{:.1f}".format(V1) + "+")
        print("+(x-" + "{:.1f}".format(x0) +")*(x-" + "{:.1f}".format(x1) + ")*" + "{:.1f}".format(V10))
        print("+(x-" + "{:.1f}".format(x0) +")*(x-" + "{:.1f}".format(x1) + ")*" + "(x-" + "{:.1f}".format(x2) + ")*" + "{:.1f}".format(V100))
        print("---------------------")





        A = [[1, 1, 1, 1],
            [x0, x1, x2, x3]]
        
        B = [[1, x0],
            [1, x1],
            [1, x2],
            [1, x3]]

        C = [[y0],
            [y1],
            [y2],
            [y3]]
            
        print("---------")
        print("Mat SX")
        MultiplyAndPrintMatrix(A,B)
        print("---------")
        print("Mat DX")
        MultiplyAndPrintMatrix(A,C)


        break





Main()