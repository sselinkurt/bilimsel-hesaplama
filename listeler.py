i = int(input("kaca kaclik birim matris hesaplansin : "))
print([[1 if satir==sutun else 0 for sutun in range(i)] for satir in range(i)] )
