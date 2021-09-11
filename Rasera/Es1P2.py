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
        return ""+num[0:t], exponent
    else:
        pos = t-1
        # Trova gli 1
        while pos != -1 and num[pos] == '1':
            pos = pos - 1

        # Aggiunti un esponente
        if pos == -1: 
            exponent += 1
            return ""+"1000000000000"[0:t], exponent
        else:
            num = num[0:pos]+'100000000000000'
            return ""+num[0:t], exponent
    return "", 0

def from2to10(num_original, num_period, s):
    num_pure = num_original.replace('.', '').replace('(', '').replace(')', '')
    num_before = num_original[0:num_original.find('.')]
    num_pure_10 = int(num_pure, 2)
    num_before_10 = int(num_before, 2)
    period_len = '1' * (len(num_period))
    period_len_10 = int(period_len, 2)

    print("{}: ({}-{})/{}".format(s, num_pure_10, num_before_10, period_len_10))
    res = (num_pure_10 - num_before_10)/period_len_10
    return res

def fromFlto10(num_fl, num_exp, s):
    exponent = -1
    result = 0

    for i in range(0, len(num_fl)):
        result += int(num_fl[i]) * 2**exponent
        exponent -= 1
    
    print("{}: {} * 2**{}".format(s, result, num_exp))
    return result * 2**num_exp


# Main
## Seconda Parte
t = int(input("t= "))
emax = int(input("Emax= "))
emin = int(input("Emin= "))
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

x_str = x_str.replace('('+x_period+')', x_period*10)
y_str = y_str.replace('('+y_period+')', y_period*10)

x_str = x_str[0:t+1]
y_str = y_str[0:t+1]

# Pulizia della stringa
x_str, x_exp = trasforma(x_str, t, x_exp)
y_str, y_exp = trasforma(y_str, t, y_exp)

# Stampa in Float
print("x': 0."+x_str+" x2**"+str(x_exp))
print("y': 0."+y_str+" x2**"+str(y_exp))

# Trasformazione in base 10
x_10 = from2to10(x_str_original, x_period, "x10")
y_10 = from2to10(y_str_original, y_period, "y10")
xt_10 = fromFlto10(x_str, x_exp, "x'10")
yt_10 = fromFlto10(y_str, y_exp, "y'10")

print("x10: {}\ny10: {}\nx'10: {}\ny'10: {}".format(x_10, y_10, xt_10, yt_10))
#print("x_fl: {} x 2^{}".format(x_period, x_exp))