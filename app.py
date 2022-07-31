# Program data mahasiswa
import function

# List of dictionary
daftar_kontak = []
daftar_kontak.append

# Menu program
while True:
    print("Menu")
    print("1. Daftar Mahasiswa")
    print("2. Tambah Data Mahasiswa")
    print("3. Hapus Data Mahasiswa")
    print("4. Cari Data Mahasiswa")
    print("0. Keluar Program")

    menu = input("Pilih menu : ")

    if menu == "0":
        break
    elif menu == "1":
        function.display_kontak(daftar_kontak)
    elif menu == "2":
        kontak = function.new_kontak()
        daftar_kontak.append(kontak)
    elif menu == "3":
        function.hapus_kontak(daftar_kontak)
    elif menu == "4":
        function.cari_kontak(daftar_kontak)
    else:
        print("Menu tidak tersedia")

print("Program selesai berjalan, sampai jumpa :) ")