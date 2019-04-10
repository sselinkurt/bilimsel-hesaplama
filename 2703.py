#sekant yontemi ile koklere yaklasma

def f(x):
    return(x**2-4*x+3)

x1 = int(input("baslangic degeri: "))
x2 = int(input("bitis degeri: "))

if(f(x1)*f(x2)==0):
    print("Girdiginiz degerlerden biri kok")
else:
    while(abs(f(x2)-f(x1))>0.01): #abs mutlak deger fonksiyonudur
        x3 = x1 - f(x1)*(x2-x1)/(f(x2)-f(x1))
        x1, x2 = x2, x3
        if(x1==x2): #zero division hatasi vermesin diye burda durduruyoruz cunku belli bir yerden sonra x1 ve x2 birbirine yaklasicak
            break
print(x1,x2)
