def vigenere_encrypt_verbose(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = plaintext.upper().replace(" ", "").replace("\n", "")
    key = key.upper().replace(" ", "")
    ciphertext = ""
    key_index = 0

    print("{:<5} {:<5} {:<5} {:<5} {:<15} {:<5}".format(
        "P", "K", "Pi", "Ki", "(Pi+Ki)%26", "Ci"))
    print("=" * 45)

    for char in plaintext:
        if char in alphabet:
            p = alphabet.index(char)
            k = alphabet.index(key[key_index % len(key)])
            c = (p + k) % 26
            cipher_char = alphabet[c]
            ciphertext += cipher_char
            key_index += 1
            print("{:<5} {:<5} {:<5} {:<5} {:<15} {:<5}".format(
                char, key[(key_index - 1) % len(key)], p, k, f"({p}+{k})%26", cipher_char))
        else:
            ciphertext += char

    print("\nCiphertext:")
    print(ciphertext)


# Teks plaintext
plaintext = """DI SEBUAH DESA PEGUNUNGAN, KABUT PAGI MASIH MENYELIMUTI ATAP-ATAP RUMAH KAYU. SEORANG
WANITA TUA DUDUK DI TERAS, MENIUP ASAP TEH HANGATNYA SAMBIL MENIKMATI UDARA SEGAR. DI JALAN
SETAPAK, SEORANG ANAK KECIL BERJALAN SAMBIL MEMBAWA KERANJANG PENUH SAYURAN DARI LADANG.
BEBERAPA PETANI MULAI TURUN KE SAWAH, MENCANGKUL TANAH YANG MASIH LEMBAP OLEH EMBUN. DI
KEJAUHAN, TERDENGAR SUARA LONCENG SAPI YANG DIGEMBALAKAN MENUJU PADANG RUMPUT. MATAHARI
PERLAHAN MUNCUL DARI BALIK BUKIT, MENYINARI LADANG HIJAU YANG LUAS. HARI BARU DIMULAI DENGAN
KESIBUKAN YANG TELAH MENJADI BAGIAN DARI KEHIDUPAN DESA INI."""

# Kunci
key = "RAHMAT WILDAN SUDRAJAT"

# Jalankan enkripsi dengan langkah
vigenere_encrypt_verbose(plaintext, key)
