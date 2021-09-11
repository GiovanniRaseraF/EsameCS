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

def trasforma(num, t, exponent):
    if num[t] == '0':
        return "0."+num[0:t], exponent
    else:
        pos = t-1
        # Trova gli 1
        while pos != -1 and num[pos] == '1':
            pos = pos - 1

        # Aggiunti un esponente
        if pos == -1: 
            exponent += 1
            return "0."+"1000000000"[0:t], exponent
        else:
            num = num[0:pos]+'1000000000'
            return "0."+num[0:t], exponent
    return "", 0



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

t_good = 0; emax_good = 0; emin_good = 0
## Verifica Clausole
for t in range(1,15):
    for ema in range(1, 15):
        for emi in range(1, 15):
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
                t_good = t; emax_good = ema; emin_good = emi
input()

## Seconda Parte
t = int(input("t= "))
emax = int(input("Emax= "))
emin = int(input("Emin= "))
#t = t_good
#emax = emax_good
#emin = emin_good
# Inserimento variabili
print("1.0(10) <-(period)")
x_str_original = input("x= ")
y_str_original = input("y= ")
x_str = x_str_original
y_str = y_str_original
x_str = x_str.replace(' ', '')
y_str = y_str.replace(' ', '')

# Trovo esponente
x_exp = x_str.find('.')
y_exp = y_str.find('.')
x_str = x_str.replace('.', '')
y_str = y_str.replace('.', '')

# Trova Periodo
x_AP = x_str.find('(')
x_CH = x_str.find(')')
y_AP = y_str.find('(')
y_CH = y_str.find(')')

x_period = x_str[x_AP+1:x_CH]
y_period = y_str[y_AP+1:y_CH]

x_str = x_str.replace('('+x_period+')', x_period+x_period+x_period)
y_str = y_str.replace('('+y_period+')', y_period+y_period+y_period)

x_str = x_str[0:t+1]
y_str = y_str[0:t+1]

# Pulizia della stringa
x_str, x_exp = trasforma(x_str, t, x_exp)
y_str, y_exp = trasforma(y_str, t, y_exp)
print(x_str+" x2**"+str(x_exp))
print(y_str+" x2**"+str(y_exp))

#print("x_fl: {} x 2^{}".format(x_period, x_exp))