begeni1=365000
begeni2=450000
begeni3=582000
yorum1=65000
yorum2=25000
yorum3=52000
paylasim1=870
paylasim2=380
paylasim3=1200
icerik1=500
icerik2=100
icerik3=650
takipci1=1125000
takipci2=1450000
takipci3=2000000
def oran1(begeni1,yorum1,paylasim1,icerik1,takipci1):
    global a
    a=(((begeni1+yorum1+paylasim1)/icerik1)/takipci1)*100
    return a

def oran2(begeni2,yorum2,paylasim2,icerik2,takipci2):
    global b
    b=(((begeni2+yorum2+paylasim2)/icerik2)/takipci2)*100
    return b

def oran3(begeni3,yorum3,paylasim3,icerik3,takipci3):
    global c
    c=(((begeni3+yorum3+paylasim3)/icerik3)/takipci3)*100
    return c

x=oran1(begeni1,yorum1,paylasim1,icerik1,takipci1)
y=oran2(begeni2,yorum2,paylasim2,icerik2,takipci2)
z=oran3(begeni3,yorum3,paylasim3,icerik3,takipci3)
