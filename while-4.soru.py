#çalışılan günü 5 gün olarak aldım.
calisan=50
saat=40
yevmiye=90
haftalikMaas=450
while True:
    maas=haftalikMaas*4
    i=int(input("Aylık mesai saati giriniz:"))
    x=i*yevmiye*10/100
    
    if(i>22):
        print("Maksimum mesai saatini aştınız.Mesai saatini yeniden giriniz.(Maksimum mesai saati:22)")
        
    else:
        maas=maas+x
        print("Aylık maas:",maas)
        
