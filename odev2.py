def ekipmanKullanilabilirlikOrani(planlanmisUretimSuresi,plansizDurus):
    kullanilabilirlik=(planlanmisUretimSuresi-plansizDurus)/planlanmisUretimSuresi
    return kullanilabilirlik

def kaliteOrani(saglamUrun,toplamUretimMiktari):
    kalite=saglamUrun/toplamUretimMiktari
    return kalite

def performansOrani(standartCevrim,uretimMiktari,planlanmisUretimSuresi,plansizDurus):
    performans=(standartCevrim*uretimMiktari)/(planlanmisUretimSuresi-plansizDurus)
    return performans

def ekipmanEtkililikOrani(kullanilabilirlik,performans,kalite):
    oee=kullanilabilirlik*performans*kalite
    return oee

planlanmisUretimSuresi=int(input("Planlanmış Üretim Süresini Giriniz:"))
plansizDurus=int(input("Plansız Duruş Süresini Giriniz:"))
standartCevrim=int(input("Standart Çevrim Süresini Giriniz:"))
uretimMiktari=int(input("Üretim Miktarını Giriniz:"))
saglamUrun=int(input("Sağlam Ürün Miktarını Giriniz:"))
toplamUretimMiktari=int(input("Toplam Üretim Miktarını Giriniz:"))


print("Ekipman Kullanılabilirlik Oranı:%",ekipmanKullanilabilirlikOrani(planlanmisUretimSuresi,plansizDurus))
print("Kalite Oranı:%",kaliteOrani(saglamUrun,toplamUretimMiktari))
print("Performans Oranı:%",performansOrani(standartCevrim,uretimMiktari,planlanmisUretimSuresi,plansizDurus))
print("Ekipman Etkililik Oranı:%",ekipmanEtkililikOrani(ekipmanKullanilabilirlikOrani(planlanmisUretimSuresi,plansizDurus),kaliteOrani(saglamUrun,toplamUretimMiktari),performansOrani(standartCevrim,uretimMiktari,planlanmisUretimSuresi,plansizDurus)))
