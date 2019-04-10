#dizi ile dogruya yaklasma cozumu

def dogruyaYaklasma(x, y):
    xiyi = 0
    for i in range(len(x)): 
        xiyi += x[i]*y[i]

    a1 = (len(x)*xiyi - sum(x)*sum(y))/(len(x)*sum([i**2 for i in x])-sum(x)**2)
    a0 = (sum(y)-a1*sum(x))/len(x)

    print(a0, a1)

def dogruyaYaklasma2(x, y): #yukaridaki fonksiyon ile ayni isi yapiyor. Burada xiyi degiskeni tanimlanmadan cozulmustur.

    a1 = (len(x)*sum([x[i]*y[i] for i in range(len(x))])-sum(x)*sum(y)) / (len(x)*sum([i**2 for i in x])-sum(x)**2)
    a0 = (sum(y)-a1*sum(x))/len(x)
    print(a0, a1)



x = [1, 2, 3, 4, 6, 7, 9]
y = [3, 5, 7, 9, 13, 15, 19] 
dogruyaYaklasma(x, y)
dogruyaYaklasma2(x, y)
