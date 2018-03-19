#yazilim=Yazılım Geliri
#finansman=Finansman Geliri
#satis=Ürün Satış Geliri
#maas=Çalışan Maaşları
#kira=Kira Gideri
#donanim=Donanım Maliyeti
#sponsorluk=Sponsorluk Geliri
#eticaret=E-ticaret Geliri
#bakim=Bakım Maliyeti

def ilk6(yazilim,finansman,satis,maas,kira,donanim):
    kar1=(yazilim+finansman+satis)-(maas+kira+donanim)
    global ilk6
    return kar1

def son6(yazilim,sponsorluk,eticaret,satis,maas,kira,bakim):
    kar2=(yazilim+sponsorluk+eticaret+satis)-(maas+kira+bakim)
    global son6
    return kar2


def karfark(kar2,kar1):
    fark=kar2-kar1
    global karfark
    return fark

a=int(input("İlk 6 Aylık Yazılım Gelirinizi Giriniz:"))
b=int(input("İlk 6 Aylık Finansman Gelirinizi Giriniz:"))
c=int(input("İlk 6 Aylık Ürün Satış Gelirinizi Giriniz:"))
d=int(input("İlk 6 Aylık Çalışan Maaşlarını Giriniz:"))
e=int(input("İlk 6 Aylık Kira Giderlerinizi Giriniz:"))
f=int(input("İlk 6 Aylık Donanım Maliyetlerinizi Giriniz:"))

g=int(input("Son 6 Aylık Yazılım Gelirinizi Giriniz:"))
z=int(input("Son 6 Aylık Sponsorluk Gelirinizi Giriniz:"))
t=int(input("Son 6 Aylık E-Ticaret Gelirinizi Giriniz:"))
h=int(input("Son 6 Aylık Ürün Satış Gelirinizi Giriniz:"))
i=int(input("Son 6 Aylık Çalışan Maaşlarını Giriniz:"))
k=int(input("Son 6 Aylık Kira Giderlerinizi Giriniz:"))
p=int(input("Son 6 Aylık Bakım Maliyetlerinizi Giriniz:"))

x=ilk6(a,b,c,d,e,f)

y=son6(g,z,t,h,i,k,p)

j=karfark(y,x)
if(j>5000):
    print("İşletme çok karlı!")
elif(j<1000):
    print("İşletme yeterince karda değil.")
else:
    print("İşletme karı normal.")

    
