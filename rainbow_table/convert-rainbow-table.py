import hashlib

# Giriş dosyası (word_list.txt) adı
input_file = "word_list.txt"

# Çıkış dosyası (hash_list.csv) adı
output_file = "hash_list.csv"

# SHA-256 hesaplamalarını yapmak için bir fonksiyon tanımlayın
def calculate_sha256(input_string):
    return hashlib.sha256(input_string.encode('utf-8')).hexdigest()

# Giriş dosyasını oku ve her satırın SHA-256 değerini hesapla
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        line = line.strip()  # Satır sonundaki gereksiz boşlukları kaldırın
        if line:  # Boş satırları atla
            hashed_value = calculate_sha256(line)
            outfile.write(f"{line},{hashed_value}\n")

print("SHA-256 hash değerleri", output_file, "dosyasına yazıldı.")
