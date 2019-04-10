#dogruya yaklasma

sozluk = {1:3, 2:5, 3:7, 4:9, 6:13, 7:15, 9:19}  

xiyi = 0

for i in range(len(sozluk.keys())):
    xiyi += list(sozluk.keys())[i]*list(sozluk.values())[i] # xiyi += x[i]*y[i]

a1 = (len(sozluk.keys())*xiyi - sum(sozluk.keys())*sum(sozluk.values()))/(len(sozluk.keys())*sum([i**2 for i in sozluk.keys()])-sum(sozluk.keys())**2)
a0 = (sum(sozluk.values())-a1*sum(sozluk.keys()))/len(sozluk.keys())

print(a0, a1)
