import math

# Kullanıcıdan kenar uzunluklarını al
a = float(input("1. kenarın uzunluğunu girin (a): "))
b = float(input("2. kenarın uzunluğunu girin (b): "))

# Hipotenüsü hesapla (c = √(a² + b²))
c = math.sqrt(a**2 + b**2)

# Sonucu yazdır
print(f"Hipotenüs (c) = {c:.2f}")
 
""
