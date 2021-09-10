# Esercizio 1
def realmin(emim):
    return 2**(-emi-1)

def realmax(t, emax):
    return (2**emax)*(1  - 2**(-t))

def F(t, emax, emin):
    return 2 * (2 - 1) * 2**(t-1) * (emax + emin + 1)

def Fpos(t, emax, emin):
    return (2 - 1) * 2**(t-1) * (emax + emin + 1)

def Fzero(t, emax, emin):
    return 1 + F(t, emax, emin) 

def U(t):
    return 1/2 * 2**(1-t)

def numeridenormalizzati(t):
    return 1 + 2 * 2**(t-1)


# Main
## Raccogliemento Clausole
print("Clausole(f -> stop)")
clausole = []
while(True):
    clausola = input(">")

    if clausola == "f":
        break
    else:
        clausole.append(clausola)

## Verifica Clausole
for t in range(1,30):
    for ema in range(1, 30):
        for emi in range(1, 30):
            rmi = realmin(emi)
            rma = realmax(t, ema)
            f = F(t, ema, emi)
            fz = Fzero(t, ema, emi)
            fp = Fpos(t, ema, emi)
            u = U(t)
            nd = numeridenormalizzati(t)

            check = True
            # ckeck
            for cla in clausole:
                #print("t:{},emax:{},emin:{}".format(t,ema,emi), end="")
                check = check and eval(cla)

            if check == True:
                print("t:{}\nemax:{}\nemin:{}".format(t,ema,emi))

## Seconda Parte
