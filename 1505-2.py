#diferansiyel denklem cozumunu euler yontemi ile bulma

def f(x,y):
    return -yi/x

h = float(input("h degeri giriniz: "))
ys = int(input("yson degerini girin: "))
yi = 3/4  #y4 un degeri

for i in range(4,ys):
    yi = yi + f(i,i)*h
    print("y",i+1,"degeri:", yi)

