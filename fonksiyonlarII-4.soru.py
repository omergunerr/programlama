#koltuk=Koltuk sayısı
#yatak=Yatak sayısı
#dolap=Dolap sayısı




def donemBasi(koltuk,yatak,dolap):
    stok=koltuk+yatak+dolap
    global donemBasi
    return stok
def donemSonu (satilanKoltuk=25,satilanYatak=20,satilanDolap=10,alinanKoltuk=10,alinanYatak=15,alinanDolap=5):
    stokSon=(satilanKoltuk+satilanYatak+satilanDolap)-(alinanKoltuk+alinanYatak+alinanDolap)
    global donemSonu
    return stokSon

def ortalama (donemBasiStok,donemSonuStok,donem=2):
    ortalamaStok=(donemBasiStok+donemSonuStok)/donem
    global ortalama
    return ortalamaStok

a=int(input("Dönem Başı Koltuk Sayısını Giriniz:"))
b=int(input("Dönem Başı Yatak Sayısını Giriniz:"))
c=int(input("Dönem Başı Dolap Sayısını Giriniz:"))

x=donemBasi(a,b,c)
y=x-(donemSonu (satilanKoltuk=25,satilanYatak=20,satilanDolap=10,alinanKoltuk=10,alinanYatak=15,alinanDolap=5))
z=ortalama(x,y)
print("Dönem Başı Stok Durumunuz",x)

print("Dönem İçi Satılan Koltuk Sayısı=25")
print("Dönem İçi Satılan Yatak Sayısı=20")
print("Dönem İçi Satılan Dolap Sayısı=10")
print("Dönem İçi Alınan Koltuk Sayısı=10")
print("Dönem İçi Alınan Yatak Sayısı=15")
print("Dönem İçi Alınan Dolap Sayısı=5")

print("Dönem Sonu Stok Durumunuz",y)

print("Yıllık Ortalama Stok Durumunuz=",z)
