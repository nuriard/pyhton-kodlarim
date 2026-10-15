#♥#

list=["bade","berat","ömer","levent"]

for i in range(4):
    print((i+1),".çocuğumun adı: ",
    list[i])

#     burda hastaghleri kaldırırsan calısıyo kod ben kod devam etsin diye kapadım.

"""
list=["bade","berat","ömer","levent"]


for i in range(4):
     print((i+1),".çocuğumun adı: ",
           print(i))
"""

"""
#for d in range(0,24,2):
 #   print(d)
    """
"""
#for i in range(24):
 #   if i%2==0:
  #      print(i)
  """
  
"""   
#for i in range(0,57,8):
#    print(i)
"""
    
"""
sonuç=0
for i in range(8):     #○-----> mesela 8x7yi çarpma işlemi kullanmadan direkt sonuçu bize yazdırmasını istedik
   sonuç=sonuç+7
  """
  
"""
a="python"
for i in a:
   print(i)"""
 

"""
sayi=0
while sayi!=0:
       sayi=int(input("SAYI GİR KARDEŞİM:")) 
       print("GİRİLEN SAYININ KARESİ: ", sayi**2)
      """ 
      
""" 
bolunen=int(input("bölünecek sayı: "))
bolen=int(input("bölen sayı: "))
bolum=0
while bolunen >= bolen:
    bolunen-bolen
    bolum=bolum+1
print("bölüm",bolunen)
print("kalan",bolunen)
"""

#break ve continue ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !


  #0dan 24 e kadar 2şer artacak ama 3 e bölünenleri sayıları yazmayan kod
"""
 for i in range(0,24,2):
    if i%3==0:
        continue
    print(i)
"""
#bu kodda continue yerine break yazsaydım 2,4,gidecekti
#6 ya geldiğinde duracaktı.!7

"""  #burda 0 yerine 1yazınca değişiyor calısıyor break için.
for i in range(1,24,2):
   if i%3==0:
       break
print(i)
""" 

#kullanıcı 1den 10 a kadar 1 sayı girsin.
#diyelim ki 6 girdi.
#6 larda dahil olmak üzere bize çarpım tablosu hazırlasın.
#1x1= 1x2=2 1x3=3 1x4=4 1x5=5 1x6=6... 1x10=10 a kadar yazan çarpım tablosunu yazınız

"""
x=int(input("x: "))
for i in range(1,x+1):
    print("---------")
    #her çarpım yani 1den10a kadar çarpımlar gerçekleştikten sonra araya
    #kesikli çizgi gelmesi için bunu buraya yazarım.
    for j in range(1,11):
        print(i," x "," j ","=",(i*j))

"""
"""
#kullanıcıdan bir sayı girmesini iste.

x=int(input("çarpım tablosu için bir sayı giriniz: "))
#girdiği sayı mesela  5 olsun 1x1 1x2 1x3 1x4 1x5 e kadar gitmesini sağlayacak bir kod yazalım.
#bunun için 1,x+1 diyeceğim 1 den başlıcak ve xsayısınıa 1 ekleyerek devam edecek
for i in range(1,x+1):
    #her çarpma işleminden sonra araya çizgi geçsin diye araya ---- yazıcam
    print("----------")
    #burada 11e kadar yani max x10 yazsın diye 1,11 arası dedim 1,10 deseydim x9 da kalırdı
    for d in range(1,11):
        print(i," x "," d ","=",(i*d))
"""
        
        #hoca sınavda mesela bu tarz bir soru örneği verip bizden
      #çalıştırmamızı isteyecek yazılım vize soru tarzı tam olarak bunlara iyi çalışmak gerek.
        
"""
x=int(input("X için bir sayı seçiniz: "))
for i in range(1,x+1):
    print("<----------->")
    for e in range(1,20):
        print(i," x "," e ","=",(i*e))
        
        #burada yaptığım hata 20ye kadar çarpmasını istedim ama 1,20 dediğim için
        #1den 20ye kadar yani 1,2,3,4,5,.....15,16,17,18,19 yaptı 20 yok
        #20 dahil olması için 1,21 yapmam gerekiyor.
        #çünkü (başlangıç,son,adım) diye gidiyor 
        #şimdi aynı kodu (1,21) olarak yazacağım ve 1,2,3,4,5,6,7,....."Xsayısı" x 20 yapacak

""
""  
x=int(input("X için bir sayı seçiniz: "))
for i in range(1,x+1):
            print("<----------->")
            for e in range(1,21):
                print(i," x "," e ","=",(i*e))
                
             #burada başarılı ve istediğim biçimde çalıştı kod.
   #SAKIN AMA SAKIN KODU YAZDIKTAN SONRA KONTROL ETMEDEN, ÇALIŞTIRMADAN HOCAYA SUNMA TAMAMLAMA!
   
"""

   
   
   
                
        
        
        
               
        
        
        


 



 


   