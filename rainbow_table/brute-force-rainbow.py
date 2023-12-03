import csv
import hashlib

# Hedef hash değeri
hedef_hash = input("Hedef hash değeri: ")  # Örnek SHA-256 hash

# CSV dosyasının adı
csv_dosya_adi = "hash_list.csv" 

try:
    with open(csv_dosya_adi, newline='') as dosya:
        okuyucu = csv.reader(dosya)
        for satir in okuyucu:
            if len(satir) >= 2:
                metin = satir[0]
                hash_degeri = satir[1]

                # Metinden SHA-256 hash hesaplama
                hesaplanan_hash = hashlib.sha256(metin.encode()).hexdigest()

                if hesaplanan_hash == hedef_hash:
                    print(f"Hedef hash değeri bulundu. Karşılık gelen metin --> {metin}")
                    break
        else:
            print("Hedef hash değeri bulunamadı.")

except FileNotFoundError:
    print(f"'{csv_dosya_adi}' adlı CSV dosyası bulunamadı.")
except Exception as e:
    print(f"Bir hata oluştu: {e}")
