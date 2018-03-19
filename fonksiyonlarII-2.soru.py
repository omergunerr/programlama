#saat=Çalışılan Süre
#sayı=Toplam Müşteri Sayısı

saat=170
sayı=50
def sure(saat,sayı):
    csure=saat/sayı
    global sure
    return csure
x=sure(saat=170,sayı=50)
print("2016 Yılı Müşterilerle Çalışma Süresi:",x)

saat=saat+50
sayı=sayı+20

def sure2(saat,sayı):
    csure2=saat/sayı
    global sure2
    return csure2
y=sure2(saat,sayı)
print("2017 Yılı Müşterilerle Çalışma Süresi:",y)

def fark(x,y):
    surefark=x-y
    global fark
    return surefark
a=fark(x,y)
print("Müşterilerle Çalışma Süresi Arasındaki Fark(2016-2017):",a)

