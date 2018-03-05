def ciroHesapla(satisMiktari,birimSatisFiyati):
    ciro=satisMiktari*birimSatisFiyati
    return ciro

def adamCiroHesapla(toplamCiro,toplamCalisan):
    adamCiro=toplamCiro/toplamCalisan
    return adamCiro

toplamCalisan=25
satisMiktari=int(input("Satış Miktarınızı Giriniz:"))
birimSatisFiyati=int(input("Birim Satış Fiyatınızı Giriniz:"))


print("Adam Başına Ciro:",adamCiroHesapla(ciroHesapla(satisMiktari,birimSatisFiyati),toplamCalisan))
