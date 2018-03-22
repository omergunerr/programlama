i=0
uretim=200
toplamDefo=0
while True:
    uyarı=uretim*20/100
    defo=int(input("Defolu ürün sayısını giriniz:"))
    if(defo>uyarı):
        print("DİKKAT! Defolu ürün sayınız %20'nin üzerinde!")
        break
    else:
        toplamDefo=toplamDefo+defo
        i=i+1
        print(i,".gün toplam defolu ürün sayınız:",toplamDefo)
