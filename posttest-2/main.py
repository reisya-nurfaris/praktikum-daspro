from prettytable import PrettyTable
toko = PrettyTable()
daftar_item = [
    ["Tenda camping", 500000],
    ["Sleeping bag", 200000],
    ["Backpack besar", 700000],
    ["Sepatu hiking", 300000],
    ["Swiss army knife", 300000],
    ["Karabiner", 50000]
]
toko.title = "Daftar Barang"
toko.field_names = ["No", "Barang", "Harga"]
def refresh_toko():
    toko.clear_rows()
    for i in range(len(daftar_item)):
        toko.add_row([i+1, daftar_item[i][0], f"Rp. {daftar_item[i][1]}"])

refresh_toko()

keranjang = []

tampilan_keranjang = PrettyTable()
tampilan_keranjang.title = "Keranjang"
tampilan_keranjang.field_names = ["Barang", "Harga", "Jumlah", "Total"]

username = "admoon"
password = "admidiamidin"

def menu_awal():
    print("\nToko Perlengkapan Outdoor Egear")
    print("1. Lanjut sebagai pembeli")
    print("2. Menu admin")
    print("3. Keluar")
    menu = input("Pilihan: ")

    if menu == '1':
        menu_pembeli()
    elif menu == '2':
        menu_admin()
    elif menu == '3':
        exit()

def menu_admin():
    input_username = input("\nusername: ")
    input_password = input("password: ")
    if input_username == username and input_password == password:
        print("\nBerhasil login sebagai admin")
        while True:
            print("\nMenu Admin")
            print("1. Lihat daftar barang")
            print("2. Tambah barang")
            print("3. Edit barang")
            print("4. Hapus barang")
            print("5. Kembali")
            pilihan = input("Pilihan: ")
            if pilihan == '1':
                print(toko)
            if pilihan == '2':
                nama_barang = input("Masukkan nama barang: ")
                while True:
                    harga_barang = input("Masukkan harga barang: ")
                    if harga_barang.isdigit() == False:
                        print("\nInput hanya bisa berupa angka\n")
                    else:
                        print("\nBarang berhasil ditambah\n")
                        break

                daftar_item.append([nama_barang, int(harga_barang)])
                toko.add_row([len(daftar_item), nama_barang, f"Rp. {harga_barang}"])
                print(toko)

            elif pilihan == '3':
                print(toko)
                no = int(input("Masukkan nomor barang yang akan diubah: ")) 
                nama_barang = input("Masukkan nama barang: ")
                while True:
                    harga_barang = input("Masukkan harga barang: ")
                    if harga_barang.isdigit() == False:
                        print("\nInput hanya bisa berupa angka\n")
                    else:
                        print("\nBarang berhasil diubah\n")
                        break
                
                daftar_item[no-1] = [nama_barang, int(harga_barang)]
                refresh_toko()
                print(toko)
            elif pilihan == '4':
                print(toko)
                no = int(input("\nMasukkan nomor barang yang ingin dihapus: "))
                konfirmasi = input(f"Apakah anda yakin ingin menghapus {daftar_item[no-1][0]}? (y/n): ")
                if konfirmasi == 'y':
                    daftar_item.pop(no - 1)
                    refresh_toko()
                    print("\nBarang berhasil dihapus\n")
                    print(toko)
                else:
                    print("\nOperasi dibatalkan\n")
                    break
            elif pilihan == '5':
                menu_awal()
    else:
        print("\nusername atau password salah\n")
        menu_awal()

def menu_pembeli():
    while True:
        print(f"\n{toko}")
        pilihan = input("Ketik nomor barang untuk memasukkannya ke keranjang: ")
        if pilihan.isdigit():
            if int(pilihan)-1 < len(daftar_item):
                barang = daftar_item[int(pilihan)-1]
                nama_barang = barang[0]
                harga_barang = barang[1]
                sudah_ada = False
                for isi_keranjang in keranjang:
                    if isi_keranjang[0] == nama_barang:
                        isi_keranjang[2] += 1  # Tingkatkan jumlah jika barang sudah ada
                        isi_keranjang[1] = harga_barang
                        isi_keranjang[3] = harga_barang * isi_keranjang[2]  # Hitung ulang total harga
                        sudah_ada = True
                        break
                
                if sudah_ada == False:
                    keranjang.append([nama_barang, harga_barang, 1, harga_barang])
                
                harga_total = 0
                total_pembelian = 0
                for isi_keranjang in keranjang:
                    harga_total = int(isi_keranjang[3])+harga_total
                    total_pembelian = isi_keranjang[2]+total_pembelian

                tampilan_keranjang.clear_rows()
                for i in range(len(keranjang)):
                    tampilan_keranjang.add_row([keranjang[i][0], f"Rp. {keranjang[i][1]}", keranjang[i][2], f"Rp. {keranjang[i][3]}"])
                
                tampilan_keranjang.add_rows([
                    ["-"*10,"-"*10,"-"*10, "-"*10],
                    [f"{total_pembelian} item",'',"Total harga", f"Rp. {harga_total}"],
                ])
                print(f"\n{nama_barang} ditambahkan ke keranjang\n")
                print(tampilan_keranjang,"\n")

                print("1. Tambah barang")
                print("2. bayar")
                pilihan = input("Pilihan: ")
                if pilihan == '1':
                    continue
                elif pilihan == '2':
                    while True:
                        uang = int(input("\nMasukkan jumlah uang anda: "))
                        if uang >= harga_total:
                            tampilan_keranjang.title = "Pembayaran"
                            tampilan_keranjang.add_rows([
                                ['', '', "Tunai", f"Rp. {uang}"],
                                ['', '', "Kembali", f"Rp. {uang - harga_total}"]
                            ])
                            print(f"\n{tampilan_keranjang}")
                            print("\nTerima kasih telah berbelanja di toko kami")
                            exit()
                        else:
                            print("Uang anda tidak cukup")
            else:
                print("Pilihan tidak valid!\n")
        else:
            print("Input hanya bisa berupa angka!\n")

menu_awal()
