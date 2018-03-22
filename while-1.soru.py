satisMiktari=500
satisFiyati=20
ciro=5000
i=0
while True:
    ciro=ciro+(satisMiktari*satisFiyati)
    satisMiktari=satisMiktari+200
    satisFiyati=satisFiyati+10
    i=i+1
    if(ciro>500000):
        print(i," ay sonra şirket cirosu 500.000 TL 'den fazla olacaktır.")
        break
    
