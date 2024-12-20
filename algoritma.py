# Program Python untuk mengimplementasikan Autokey Cipher
# Kamus untuk mencari indeks huruf
dict1 = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
         'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
         'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
         'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
         'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

dict2 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
         5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
         10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
         15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
         20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

# Key Generation
def generate_key(message, key):
    i = 0
    while True:
        # Cek apakah panjang kunci sudah sama dengan panjang pesan
        if len(key) == len(message):
            break
        
        # Jika karakter pada indeks ke-i dalam pesan adalah spasi,
        # maka lanjut ke karakter berikutnya
        if message[i] == ' ':
            i += 1
        else:
            # Jika karakter pada indeks ke-i dalam pesan bukan spasi,
            # tambahkan karakter tersebut ke dalam kunci
            key += message[i]
            i += 1

    # Kembalikan kunci yang telah dibentuk
    return key


# Enkripsi Autokey
def encryptMessageAutokey(message, key_new):
    cipher_text = ''  # Variabel untuk menyimpan teks sandi hasil enkripsi
    i = 0  # Variabel untuk melacak indeks kunci baru (key_new)
    
    # Loop melalui setiap karakter dalam pesan
    for letter in message:
        if letter == ' ':
            cipher_text += ' '  # Jika karakter adalah spasi, tambahkan spasi ke dalam teks sandi
        else:
            # Hitung nilai enkripsi menggunakan aturan autokey
            x = (dict1[letter] + dict1[key_new[i]]) % 26
            i += 1  # Pindah ke indeks berikutnya pada kunci baru
            cipher_text += dict2[x]  # Tambahkan karakter terenkripsi ke dalam teks sandi
    
    return cipher_text  # Kembalikan teks sandi hasil enkripsi


# Dekripsi Autokey
def decryptMessageAutokey(cipher_text, key_new):
    # Inisialisasi variabel untuk menyimpan teks asli
    or_txt = ''
    
    # Inisialisasi variabel indeks i
    i = 0
    
    # Iterasi melalui setiap karakter dalam teks sandi
    for letter in cipher_text:
        # Jika karakter adalah spasi, tambahkan spasi ke teks asli
        if letter == ' ':
            or_txt += ' '
        else:
            # Hitung nilai x menggunakan rumus kriptografi
            x = (dict1[letter] - dict1[key_new[i]] + 26) % 26
            
            # Tambahkan 1 ke indeks i
            i += 1
            
            # Tambahkan karakter hasil dekripsi ke teks asli
            or_txt += dict2[x]
    
    # Kembalikan teks asli yang telah didekripsi
    return or_txt


# Python3 implementation of Columnar Transposition
import math

# Enkripsi Columnar
def encryptMessageColumnar(msg, key):
    cipher = ""

    # Lacak indeks kunci
    k_indx = 0

    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))

    # Hitung jumlah kolom matriks
    col = len(key)

    # Hitung jumlah maksimum baris matriks
    row = int(math.ceil(msg_len / col))

    # Tambahkan karakter padding '_' di sel-sel kosong
    # pada matriks
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)

    # Buat matriks dan masukkan pesan serta
    # karakter padding secara baris
    matrix = [msg_lst[i: i + col]
              for i in range(0, len(msg_lst), col)]

    # Baca matriks secara kolom menggunakan kunci
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx]
                           for row in matrix])
        k_indx += 1

    return cipher


# Dekripsi Columnar
def decryptMessageColumnar(cipher, key):
    msg = ""

    # Lacak indeks kunci
    k_indx = 0

    # Lacak indeks pesan
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)

    # Hitung jumlah kolom matriks
    col = len(key)
    
    # Hitung jumlah maksimum baris matriks
    row = int(math.ceil(msg_len / col))

    # Ubah kunci menjadi daftar dan urutkan
    # secara alfabetis sehingga kita dapat mengakses
    # setiap karakter berdasarkan posisi abjadnya.
    key_lst = sorted(list(key))

    # Buat matriks kosong untuk
    # menyimpan pesan terdekripsi
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]

    # Atur matriks kolom demi kolom sesuai
    # dengan urutan permutasi dengan menambahkannya ke matriks baru
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])

        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1

    # Ubah matriks pesan terdekripsi menjadi string
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("Program ini tidak dapat",
                        "menangani kata-kata berulang.")

    null_count = msg.count('_')

    if null_count > 0:
        return msg[: -null_count]

    return msg

def main():
    message = 'KRIPTOGRAFI'
    key_autokey = 'COBA'
    key_columnar = 'TES'

    key_new = generate_key(message, key_autokey)
    print("Teks Original =", message)
    print("Key Autokey = ",key_autokey)
    print("Key Columnar = ",key_columnar)
    print(" ")
    
    cipher_text = encryptMessageAutokey(message, key_new)
    print("Cipherteks hasil Autokey =", cipher_text)
    final_cipher_text = encryptMessageColumnar(cipher_text, key_columnar)
    print("Cipherteks hasil Autokey dan Columnar =", final_cipher_text)
    original_text = decryptMessageColumnar(final_cipher_text, key_columnar)
    print("Plainteks hasil dekripsi Columnar =", original_text)
    final_original_text = decryptMessageAutokey(original_text, key_new)
    print("Plainteks hasil dekripsi Columnar dan Autokey =", final_original_text)

# Executes the main function
if __name__ == '__main__':
	main()