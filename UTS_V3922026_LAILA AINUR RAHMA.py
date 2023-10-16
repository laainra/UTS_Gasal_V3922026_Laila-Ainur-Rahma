# Function untuk Vigenere Cipher
def generateKey(string, key): # mendefinisikan function generateKey dengan parameter string dan key untuk menghasilkan key yang akan digunakan untuk emkripsi/dekripsi
    key = key.upper() # Mengubah key dari yang diambil dari parameter menjadi huruf kapital dan disimpan lagi pada variabel key
    key_numbers = [ord(char) - ord('A') for char in key] # Pada variabel ini setiap karakter pada variabel key diubah menjadi i angka (0-25) dengan mengambil kode ASCII dari setiap karakter dalam key dan mengurangkan kode ASCII huruf nilai ASCII dari 'A' yang disimpan dalam list.
    key_string = "" # inisialisasi string kosong 
    string = ''.join(e for e in string if e.isalpha()).upper() # Pada variabel ini string yang menjadi parameter, hanya diambil karakter yang berupa huruf alfabet dengan loop for dicari setiap karakternya kemudian digabungkan lalu diubah menjadi kapital

    for i in range(len(string)): # melakukan prulangan sepanjang jumlah karakter pada string yang telah diproses
        key_string += chr(ord('A') + key_numbers[i % len(key_numbers)]) # variabel keystrng yang sebelumnya kosong diisikan dengan key yang akan diulangi jika panjang string melebihi panajang key

    return key_string # mengembalikan nilai key_string 

def vigenere_encrypt(string, key): # Function dengan parameter string dan key  untuk mengenkripsi string menggunakan metode vigenere
    encrypt_text = "" # insiisalisasi variabel kosong  yang akan digunakan untuk menyimpan hasil enkripsi
    key = key.upper() #  Key yang diberikan sebagai parameter diubah menjadi huruf kapital 
    key = key * (len(string) // len(key)) + key[:len(string) % len(key)] # Key diulang sehingga panjangnya sama dengan panjang string yang akan dienkripsi

    for i in range(len(string)): # melakukan perulangan sepanjang julah karakter  dari string
        char_num = (ord(string[i]) - ord('A') + ord(key[i]) - ord('A')) % 26 # enkripsi  setiap karakter dari string dengan mengubah karakter menjadi kode ASCII dan dikurangkan dengan karakter A lalu dijumlahkan dengan key dan hasilnya dimodulus dengan 26
        char = chr(char_num + ord('A')) # ubah hasilnya ke karakter alfabet lagi  dengan menambah dengan kode ASCII huruf A
        encrypt_text += char # simpan karakter pada variabel encrypt_text

    return encrypt_text # mengmablikan nilai dari encrypt_text

def vigenere_decrypt(encrypt_text, key): # Function dengan parameter encrypt_text dan key  untuk mengenkripsi string menggunakan metode vigenere
    orig_text = "" # variabel kosong yang akan digunakan untuk menyimpan hasil dekripsi.
    key = key.upper()  #  Key yang diberikan sebagai parameter diubah menjadi huruf kapital 
    key = key * (len(encrypt_text) // len(key)) + key[:len(encrypt_text) % len(key)] # Key diulang sehingga panjangnya sama dengan panjang string yang akan dienkripsi

    for i in range(len(encrypt_text)): # melakukan perulangan sepanjang julah karakter dari encrypt_text
        char_num = (ord(encrypt_text[i]) - ord('A') - (ord(key[i]) - ord('A')) + 26) % 26
        char = chr(char_num + ord('A')) # enkripsi  setiap karakter dari string dengan mengubah karakter menjadi kode ASCII dan dikurangkan dengan karakter A lalu dikurangkan ldengan key dan hasilnya dimodulus dengan 26
        orig_text += char # simpan karakter pada variabel orig_text

    return orig_text # mengmablikan nilai dari orig_text

# Function untuk Affine Cipher
def egcd(a, b): #  Function egcd digunakan untuk menghitung Greatest Common Divisor (GCD) atau FPB dari dua bilangan a dan b
    x, y, u, v = 0, 1, 1, 0 #  # Inisialisasi variabel-variabel x dan y akan digunakan untuk menyimpan nilai x dan y pada setiap iterasi, sedangkan u dan v akan digunakan untuk menyimpan nilai sebelumnya
    while a != 0: # loop while yang akan terus berjalan selama a tidak sama dengan 0. 
        q, r = b // a, b % a # Menghitung hasil bagi b oleh a  yang disimpan pada variabel q dan sisa dari pembagian b oleh a yang disimpan pada variabel r.
        m, n = x - u * q, y - v * q # Menghitung nilai koefisien  m dan n berdasarkan nilai-nilai sebelumnya.
        b, a, x, y, u, v = a, r, u, v, m, n # Memperbarui variabel-variabel
    gcd = b  #Nilai terakhir dari b adalah gcd /fpb
    return gcd, x, y  # Mengembalikan gcd dan nilai koefisien invers modulo

def modinv(a, m): # function modinv digunakan untuk menghitung modular inverse dari sebuah bilangan a dalam modulo m
    gcd, x, y = egcd(a, m) # memanggil egcd(a, m) untuk menghitung GCD (gcd), x, dan y.
    if gcd != 1:# jika GCD (gcd) tidak sama dengan 1, itu berarti a dan m tidak saling prima, sehingga tidak ada modular inverse 
        return None # mengembalikan None.
    else:
        return x % m # Mengembalikan hasil inversi modulo dari a terhadap m
 
def affine_encrypt(text, key): # mendefinisisakn function enkripsi affine dengan dua paramete yaitu text yang akan dienkripsi dan key dalam bentuk tupel (a, b).
    text = text.upper().replace(' ', '') # Mengubah text menjadi huruf kapital dan menghapus spasi
    encrypted_characters = [(key[0] * (ord(char) - ord('A')) + key[1]) % 26 + ord('A') for char in text] # mengubah karakter menjadi angka yang mewakili posisinya dalam alfabet, mengalikannya dengan komponen a dari kunci, menambahkan komponen b dari kunci, mengambil hasil modulo 26, dan menggesernya ke dalam rentang huruf kapital dalam ASCII yang disimpan pada variabel ini
    encrypted_text = ''.join([chr(char) for char in encrypted_characters]) # Mengubah angka-angka kembali menjadi karakter
    return encrypted_text  # Mengembalikan pesan terenkripsi


def affine_decrypt(cipher, key): # mendefinisisakn function dekripsi affine dengan dua paramete yaitu text yang akan dienkripsi dan key dalam bentuk tupel (a, b).
    decrypted_characters = [(modinv(key[0], 26) * (ord(char) - ord('A') - key[1])) % 26 + ord('A') for char in cipher] # mendekripsi setiap karakter denganmenghitung karakter asli dalam teks terenkripsi dengan mengalikan modular inverse dari komponen a kunci dengan perbedaan antara posisi karakter dalam alfabet, mengurangkan komponen b kunci, dan mengambil hasilnya dalam modulo 26, kemudian menggesernya ke dalam rentang huruf kapital ASCII.
    decrypted_text = ''.join([chr(char) for char in decrypted_characters]) # Mengubah angka-angka kembali menjadi karakter
    return decrypted_text # Mengembalikan pesan terdekripsi


def main(): # Mendefinisikan function main untuk menjalankan Program Utama
    string = "Success is not final, failure is not fatal, it is the courage to continue that counts" # inisialisasi plaintext yang disimpan pada variabel string
    keyword_vigenere = "Laila Ainur Rahma Teknik Informatika psdku angkatan dua dua bisa dipanggil Lala" # inisisalisasi keyword untuk vigenere
    keyword_affine = [7, 3] # inisisalisasi keyword untuk affine

    string = string.replace(" ", "").replace(",", "").upper() # Mengubah string menjadi huruf kapital dan menghapus spasi dan tanda koma
    keyword_vigenere = keyword_vigenere.replace(" ", "").replace(",", "").upper() # Mengubah kunci Vigenere menjadi huruf kapital dan menghapus spasi dan tanda koma
    
    key_vigenere = generateKey(string, keyword_vigenere) # Membuat key  Vigenere dengan memanggil function generateKey
    encrypt_text_vigenere = vigenere_encrypt(string, key_vigenere) # Menenkripsi text dengan vigenere chiper dengan memanggil function vigenere_encrypt

    print("Vigenere Encrypted message:", encrypt_text_vigenere) # menampilkan hasil enkripsi vigenere

    # Enkripsi teks Vigenere kemudian enkripsi lagi dengan Affine
    encrypted_text = affine_encrypt(encrypt_text_vigenere, keyword_affine)
    print("Double Encrypted message:", encrypted_text)  # menampilkan hasil enkripsi dari kombinasi vigenere dan affine


    # Dekripsi teks dengan Affine kemudian dekripsi lagi dengan Vigenere
    decrypted_text_affine = affine_decrypt(encrypted_text, keyword_affine) # Mendekripsi pesan dengan Affine Cipher dengan memanggil fucntion affice_decrypt
    decrypted_text_vigenere = vigenere_decrypt(decrypted_text_affine, key_vigenere) # hasil dekripsi affine chiper didekripsi lagi dengan vigenere chiper dengan memanggil vigenere_chiper
    
    print("Decrypted message with Affine:", decrypted_text_affine) # menampilkan teks terdekripsi dari affine chiper
    print("Final Decrypted message with Vigenere:", decrypted_text_vigenere) # menampilkan teks asli yang telah didekripsi lagi dengan vigenere

# Menjalaankan program main
if __name__ == '__main__':
    main()
