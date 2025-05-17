'''
Studi Kasus: Sistem Pendaftaran Kursus Online
Deskripsi Masalah:

Sebuah platform kursus online ingin membuat sistem pendaftaran sederhana. 
Data yang perlu ditangani mencakup informasi peserta, kursus yang diambil, dan status pendaftaran. 
Kamu diminta untuk menyusun representasi data menggunakan tipe data Python yang tepat.

Tugas
Buatlah program Python yang:

1. Menyimpan informasi peserta, meliputi:
    Nama lengkap (string)
    Umur (integer)
    Sudah membayar atau belum (boolean)

2. Menyimpan daftar kursus yang tersedia, yang berisi:
    Nama kursus (string)
    Durasi (dalam jam, float)
    Harga (integer)

3. Menyimpan data pendaftaran, yang menghubungkan peserta ke kursus yang mereka ambil.

4. Menampilkan informasi ringkasan pendaftaran dalam format berikut:
    Nama: Andi Setiawan
    Umur: 25
    Status Pembayaran: Sudah bayar
    Kursus yang diambil: Python Dasar
    Durasi: 10.5 jam
    Harga: Rp300000

== Petunjuk: ==
    Gunakan dictionary untuk menyimpan data peserta.
    Gunakan list atau tuple untuk menyimpan daftar kursus.
    Gunakan dictionary atau list of dicts untuk data pendaftaran.
    Gunakan if dan bool untuk mengatur status pembayaran.

'''

# print("===== SISTEM PENDAFTARAN KURSUS ONLINE =====")

# print("Informasi Peserta : ") 
# namaLengkap = "Jaya Wijaya"
# print("Nama Lengkap: ", namaLengkap)
# Umur = 25
# print("Umur: ", Umur)
# print("Sudah Membayar atau Belum?")
# Bayar = True
# print(Bayar)

# print("============================================")

# print("Daftar kursus yang tersedia: ")
# namaKursus1 = "Pemrograman Web"
# durasi1 = 3.5 
# harga1 = 50000
# print("[1] Nama Kursus: ", namaKursus1)
# print("\t Durasi: ", durasi1, "Jam")
# print("\t Harga: ", harga1)

# namaKursus2 = "Pemrograman Mobile"
# durasi2 = 3.5 
# harga2 = 60000
# print("[2] Nama Kursus: ", namaKursus2)
# print("\t Durasi: ", durasi2, "Jam")
# print("\t Harga: ", harga2)

# namaKursus3 = "Robotika"
# durasi3 = 3.5 
# harga3 = 120000
# print("[3] Nama Kursus: ", namaKursus3)
# print("\t Durasi: ", durasi3, "Jam")
# print("\t Harga: ", harga3)

print("===== Selamat Datang =====")

# print("\n")

print("Silahkan memilih kursus yang anda inginkan!")

namaKursus1 = "-> Kursus 1"
print(namaKursus1)
kursusWeb = "Pemrograman Web"
durasikursusWeb = 1
hargakursusWeb = float(50.000)
print("Nama Kursus: ", kursusWeb)
print("Durasi: ", durasikursusWeb, "Jam")
print("Harga: ", "Rp.", hargakursusWeb)

namaKursus2 = "-> Kursus 2"
print(namaKursus2)
kursusMob = "Pemrograman Mobile"
durasikursusMob = 1
hargakursusMob = float(100.000)
print("Nama Kursus: ", kursusWeb)
print("Durasi: ", durasikursusWeb, "Jam")
print("Harga: ", "Rp.", hargakursusWeb)

print("------------------------------------------")

# print("\n")

# print("Masukkan pilihan anda: ")
pilihanKursus = int(input("Masukkan pilihan anda: "))
'''
jika user mengisi inputan dua akan memunculkan kursus dua begitu juga
jika user mengisi inputan satu akan memunculkan kursus satu
setelah memunculkan kursus yang dipilih
tampilkan perintah untuk user mengisi data diri dan juga pembayaran yang dilakukan
'''
# print(pilihanKursus)
if (pilihanKursus == 1):
    print(
        
        namaKursus1, 
        "\nNama Kursus: ", kursusWeb, 
        "\nDurasi: ", durasikursusWeb,"Jam", 
        "\nHarga: ","Rp.", hargakursusWeb, 
        "\nSilahkan mengisi data diri anda untuk proses pemesanan kursus anda!"
        "\n------------------------------------------"
        )
        
    # dataDiri = "Silahkan isi data diri anda: "
    namaPengguna = input("Nama: ")
    umurPengguna = int(input("Umur: "))
    statusPembayaran = input("Status Pembayaran: ")
    print(
        "Kursus yang dipilih:", kursusWeb, 
        "\nDurasi: ", durasikursusWeb, "Jam", 
        "\nHarga: ", "Rp.", hargakursusWeb
        )
    
    # print(dataDiri)
    print("------------------------------------------")
    print("Data berhasil dimasukkan!")
    print("Nama: ", namaPengguna)
    print("Umur", umurPengguna, "Tahun")
    print("Status Pembayaran: ", statusPembayaran)
    print(
        "Kursus yang dipilih:", kursusWeb, 
        "\nDurasi: ", durasikursusWeb, "Jam",
        "\nHarga: ", "Rp.", hargakursusWeb
        )
    print("\nTerima kasih dan Selamat Belajar!")
    
elif (pilihanKursus == 2):
    print(
        
        namaKursus2, 
        "\nNama Kursus: ", kursusMob, 
        "\nDurasi: ", durasikursusMob,"Jam", 
        "\nHarga: ","Rp.", hargakursusMob, 
        "\nSilahkan mengisi data diri anda untuk proses pemesanan kursus anda!"
        "\n------------------------------------------"
        )
        
    # dataDiri = "Silahkan isi data diri anda: "
    namaPengguna = input("Nama: ")
    umurPengguna = int(input("Umur: "))
    statusPembayaran = input("Status Pembayaran: ")
    print(
        "Kursus yang dipilih:", kursusMob, 
        "\nDurasi: ", durasikursusMob, "Jam", 
        "\nHarga: ", "Rp.", hargakursusMob
        )
    
    # print(dataDiri)
    print("------------------------------------------")
    print("Data berhasil dimasukkan!")
    print("Nama: ", namaPengguna)
    print("Umur", umurPengguna, "Tahun")
    print("Status Pembayaran: ", statusPembayaran)
    print(
        "Kursus yang dipilih:", kursusMob, 
        "\nDurasi: ", durasikursusMob, "Jam",
        "\nHarga: ", "Rp.", hargakursusMob
        )
    print("\nTerima kasih dan Selamat Belajar!")
else:
    print("Pilihlah sesuai dengan pilihan yang tersedia!")

#Selesai
'''
Tapi, bagaimana kalau untuk inputan pembayarannya ditentukan oleh user yang menginput?
Jadinya jika user memasukkan sesuai dengan nominal yang ada pada menu kursus maka akan dinyatakan "Sudah Membayar" dll.
'''