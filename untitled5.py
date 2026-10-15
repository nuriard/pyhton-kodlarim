# --- Kullanıcı ayarları tam olarak 1'den 20'ye ayarlandı ---
SATIR_BASLANGIC = 1
SATIR_SONU = 20  # 20. satır dahil
SUTUN_HARFLERI = ['A', 'B', 'C', 'D'] # Kullanılacak harfler

print(f"--- {SATIR_BASLANGIC}A'dan {SATIR_SONU}D'ye Kadar Desen Başlangıcı ---")

# Dış döngü: Satır numaraları için (1'den 20'ye kadar)
# range(1, 21) -> 1, 2, ..., 20 sayılarını üretir.
for satir_no in range(SATIR_BASLANGIC, SATIR_SONU + 1):
    
    satir_cikisi = [] # Her satırın çıktısını tutacak geçici liste
    
    # İç döngü: Sütun harfleri için (A, B, C, D)
    for harf in SUTUN_HARFLERI:
        
        # Sayı ve harfi birleştirerek elemanı oluştur
        eleman = f"{satir_no}{harf}"
        
        # Elemanı satır çıktısına ekle
        satir_cikisi.append(eleman)
        
    # Satır tamamlandığında elemanları boşlukla birleştirerek yazdır
    print(" ".join(satir_cikisi))
    
    # İsteğe bağlı: 20 satırı kolay takip etmek için araya kesik çizgiler ekleyelim
    if satir_no % 5 == 0 and satir_no < SATIR_SONU:
        print("...")

print("--- Desen Sonu ---")