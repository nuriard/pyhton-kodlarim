"""

#accerman yaptık fonskiyon bağlama muhabbeti

def A(m, n):
    
    if m == 0:
        return n + 1
        
    elif m > 0 and n == 0:
        return A(m - 1, 1)
        
    elif m > 0 and n > 0:
        return A(m - 1, A(m, n - 1))

m=int(input("m= "))
n=int(input("n= "))                   ### BURAYI YAZMAZSAK EĞER YANİ İNPUTLARI KOYMAZSAK SADECE A((0,1)) GİBİ YAZAR 
print("sonuç: ", A(m,n))
  
print(f"A(0, 1) = {A(0, 1)}")
print(f"A(1, 1) = {A(1, 1)}")
print(f"A(2, 1) = {A(2, 1)}")
print(f"A(3, 0) = {A(3, 0)}")

"""


# ARABA ALACAZ alış fiyatı=
# motor hacmi= < 1.3 -1.6-2.0->
#ÖTV %     GELİŞ FİYATI 1Milyon altı olanlar icin   =    20   30   45
#GELİŞ FİYATI 1Milyon üstü olanlar için =           =    30    40   50


def f(gF, mH):
    global sF
    if gF>1:
        if mH>2:
            sF((gF*1.9)*1.2)*1.1
        elif mH>1.6:
            sF((gF*1.7)*1.2)*1.1
        elif mH>1.3:
            sF((gF*1.45)*1.2)*1.1
        elif mH<1.3:
            sF((gF*1.3)*1.2)*1.1
    else:
        if mH>2:
            sF=((gF*1.7)*1.2)*1.1
        elif mH>1.6:
            sF=((gF*1.45)*1.2)*1.1
        elif mH>1.3:
            sF=((gF*1.3)*1.2)*1.1
        elif mH<1.3:
            sF=((gF*1.2)*1.2)*1.1
    return sF

gF=float(input("Geliş Fiyatı: "))
mH=float(input("Motor Hacmi: "))
print("Satman Gereken Fiyat: ", f(gF, mH))



            
            
            
            


 
