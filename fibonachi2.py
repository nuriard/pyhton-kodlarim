"""
n=int(input("fibonachi cizgisi için sayı seçin: "))
if (n<0):
    print("Hata: Sayı negatif olamaz.")
else:
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a+b
        print(b
"""


#ya da


n=int(input("fibonachi cizgisi için sayı seçin: "))
if (n<0):
    print("Hata: Sayı negatif olamaz.")
elif n==0:
    print(0)


else:
    a = 0
    b=1
    for i in range(1,n):
        a, b = b, a + b
        print(b)
        