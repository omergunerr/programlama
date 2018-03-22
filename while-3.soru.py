i=0
while True:
    a=int(input("Bir sayı giriniz. Çıkmak için 0'a basınız."))
    if(a==0):
        print("Çıkış yaptınız!")
        break
    else:
        i=i+a%3
        print("Sayının 3'e bölümünden kalanlar toplamı:",i)
