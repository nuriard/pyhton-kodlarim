
"""
sayi=int(input("sayı gir: "))
if sayi<2:
    print("girilen sayı >=2 olmalıdır")
else:
    sonuc="Sayı asaldır"
    for i in range (2, sayi):
        if sayi%i==0:
            sonuc="sayı degıldır"
            break
        print(sonuc)
        
        #GİRİLEN SAYININ ASAL OLUP OLMADIGINI BULAN KODU YAZDIK!!!
        
        """
        
        
        # GİRİLEN 3 BASAMAKL SAYININ GÜCLÜ SAYI OLUP OLMADIGINI EKRANA YAZAN PROGRAM!!::
        # YANİ 145 = 1! + 4! + 5! = 1+24+120= 145 GİBİSİNDEN...
        
        
sayi=int(input("3 basmaklı sayı gir: "))
if sayi<100and sayi>999:
    print("girilen sayi 3 basamaklı olmalıdır.")
else:
    birler=sayi%10
    yüzler=sayi//100
    onlar=(sayi%100)//10
    birler_f=1
    onlar_f=1
    yüzler_f=1
    for i in range(1, birler+1):
        birler_f*=i
    for i in range(1, onlar+1):
        onlar_f*=i
    for i in range(1, yüzler+1):
        yüzler_f*=1
print(f"birler: {birler} onlar: {onlar} yüzler: {yüzler}")
print(f"birler_f: {birler_f} onlar_f: {onlar_f} yüzler_f: {yüzler_f}")
if sayi==birler_f+onlar_f+yüzler_f:
    print("güclü sayıır knk")
else:
    print("güclü sayı değildir")