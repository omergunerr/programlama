finansmanGelir=int(input("Finansman Gelirinizi Giriniz:"))
pazarGelir=int(input("Pazar Gelirinizi Giriniz:"))
kiraGelir=int(input("Kira Gelirinizi Giriniz:"))
toplamGelir=finansmanGelir+pazarGelir+kiraGelir

ucret=int(input("Ücretlerinizi Giriniz:"))
finansmanGider=int(input("Finansman Giderlerinizi Giriniz:"))
pazarGider=int(input("Pazar Giderlerinizi Giriniz:"))
kiraGider=int(input("Kira Giderlerinizi Giriniz:"))
muhasebeGider=int(input("Muhasebe Giderlerinizi Giriniz:"))
toplamGider=ucret+finansmanGider+pazarGider+kiraGider+muhasebeGider

kar=toplamGelir-toplamGider

if kar>1000:
    print("Durumunuz Karlı,Karınız:",kar)
else:
    print("Karınız Yeterli Değil",kar)
