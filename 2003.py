#girilen baslangic ve bitis tahminleri arasinda denklemin kokunu bulan program
#orta nokta bularak gitmek iyi bir yontem cunku aralik ne kadar buyuk olursa olsun ikiye bolerek cok cabuk kisaltiyoruz
def f(x):
    return(x**2-4*x+3)

x1 = int(input("Baslangic tahmini giriniz: "))
x2 = int(input("Bitis tahmini: "))

if(f(x1)*f(x2)==0): #girilen tahmin kok mu kontrolu
    print("tahminlerinizden biri denklemin kokudur")
elif(f(x1)*f(x2)>0):
    print("girdiginiz aralikta tek sayida kok yoktur")
else:
    for i in range(100):
        xr = (x1+x2)/2
        if(f(xr)==0):
            print("kok bulundu: ", xr, i) # i, kacinci seferde bulundugunu soylemek icin konuldu
            break
        elif(f(x1)*f(xr)<0):
            x2 = xr
        else:
            x1 = xr
       # print(xr)
    
