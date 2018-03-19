#toplamSatis=Toplam Satış Miktarı
#hamMadde=Hammadde Maliyeti
#bakim=Bakım Onarım Giderleri
#sevkiyat=Sevkiyat Giderleri
#hizmet=Satın Alınan Hizmet Giderleri



def kciro(toplamSatis,hamMadde,bakim,sevkiyat,hizmet):
    ciro=toplamSatis-(hamMadde+bakim+sevkiyat+hizmet)

    global kciro
    return ciro
    

x=int(input("Toplam Satış Miktarınızı Giriniz:"))
y=int(input("Hammadde Maliyetinizi Giriniz:"))
z=int(input("Bakım Onarım Giderlerinizi Giriniz:"))
t=int(input("Sevkiyat Giderlerinizi Giriniz:"))
d=int(input("Satın Alınan Hizmet Giderlerinizi Giriniz:"))
k=kciro(x,y,z,t,d)

if (k>1000):
    print("İşletme katma değer cirosu yüksek")
elif (k<500):
    print("İşletme katma değer cirosu düşük")
else:
    print("İşletme katma değer cirosu normal")
