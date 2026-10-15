"""

def fakt(n):
    # n'in negatif veya sıfır olma durumları için kontrol
    if n < 0:
        return "Negatif sayıların faktöriyeli tanımsızdır."
    elif n == 0:
        return 1 # 0'ın faktöriyeli 1'dir.
    else:
        sonuc = 1
        # 1'den n'e kadar sayıları çarp
        for i in range(1, n + 1):
            sonuc *= i
        return sonuc

# --- Kullanım Örnekleri ---
print(fakt(5)) # Çıktı: 120 (5 * 4 * 3 * 2 * 1)
print(fakt(0)) # Çıktı: 1
print(fakt(-3)) # Çıktı: Negatif sayıların faktöriyeli tanımsızdır.

"""


def fakt(n):
    if n<=1:
        return 1
    else:
        return n*fakt(n-1)