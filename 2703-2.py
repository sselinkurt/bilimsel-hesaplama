#integral hesaplama

def f(x):
    return(x**2)
x1 = 4
x2 = 6

#araligin kac parcaya bolunecegi
n = 1000 # n buyudukce dogru sonuca daha cok yaklasir
h = (x2-x1)/n
integral = 0

for i in range(n): #dikdortgenler(kisa kenarli) icin cozum yontemi
    integral += f(x1+i*h)*h
print(integral)

integral = 0
for i in range(1,n+1): # uzun kenarli dikdortgen icin cozum yontemi
    integral += f(x1+i*h)*h
print(integral)

integral = 0
for i in range(n): #gercek sonuca en yakin olan bu, orta noktayi almak
    integral += f(x1+h/2+i*h)*h
print(integral)

integral = 0
for i in range(n): #yamuklar ile integrali bulmaya calisma
    integral += (f(x1+i*h)+f(x1+(i+1)*h))*h/2
print(integral)


