import os
os.system('cls')

from prettytable import PrettyTable

menuMakanan = PrettyTable(['Makanan','Harga'])
menuMakanan.add_row(['Indomie goreng', 5000])
menuMakanan.add_row(['Indomie rebus', 5000])
menuMakanan.add_row(['Indomie varian', 6000])
menuMakanan.add_row(['Pop mie', 8000])
menuMakanan.add_row(['Omelet', 10000])
menuMakanan.add_row(['Mie setan', 10000])
print(menuMakanan)

menuMinuman = PrettyTable(['Minuman','Harga'])
menuMinuman.add_row(['Es teh', 3000])
menuMinuman.add_row(['Es jeruk', 3000])
menuMinuman.add_row(['Nutrisari', 5000])
menuMinuman.add_row(['Es sirup', 5000])
menuMinuman.add_row(['Kopi hitam',4000])
menuMinuman.add_row(['Kopi susu',5000])
menuMinuman.add_row(['Extrajoss',5000])
print(menuMinuman)

#fungsi untuk menambah menu makanan
def tambah_menu_makanan():
    nama = input('Masukan nama menu makanan: ')
    harga = int(input('Masukan harga menu makanan:'))
    menuMakanan.add_row([nama, f'Rp. {harga:,.0f}'])
    print(f'{nama} telah ditambahkan ke menu makanan')

#fungsi untuk menambah menu minuman
def tambah_menu_minuman():
    nama = input('Masukan nama menu minuman: ')
    harga = int(input('Masukan harga menu minuman:'))
    menuMinuman.add_row([nama, f'Rp. {harga:,.0f}'])
    print(f'{nama} telah ditambahkan ke menu minuman')

#fungsi untuk menampilkan menu
def tampilkan_menu():
    print("Menu Makanan:")
    print(menuMakanan)
    print("Menu Minuman:")
    print(menuMinuman)

#fungsi untuk edit menu makanan
def edit_menu_makanan():
    nama = input('Masukan nama menu makanan: ')
    harga_baru = int(input('Masukan harga menu makanan:'))
    if nama in menuMakanan.get_string():
        menuMakanan.get_row(nama)['Harga'] = f'Rp. {harga_baru:,.0f}'
        print(f'Harga {nama} telah diubah menjadi Rp. {harga_baru}')
    else:
        print(f'{nama} tidak ditemukan dalam menu makanan')

#fungsi untuk edit menu minuman
def edit_menu_minuman():
    nama = input('Masukan nama menu makanan: ')
    harga_baru = int(input('Masukan harga menu makanan:'))
    if nama in menuMinuman.get_string():
        menuMinuman.get_row(nama)['Harga'] = f'Rp. {harga_baru:,.0f}'
        print(f'Harga {nama} telah diubah menjadi Rp. {harga_baru}')
    else:
        print(f'{nama} tidak ditemukan dalam menu minuman')

#fungsi untuk menghapus menu makanan
def hapus_menu_makanan(nama):
    if nama in menuMakanan.get_string():
        menuMakanan.del_row(menuMinuman.get_string().index(nama))
        print(f'{nama} telah dihapus dari menu makanan')
    else:
        print(f'{nama} tidak ditemukan dalam menu makanan')

#fungsi untuk menghapus menu minuman
def hapus_menu_minuman(nama):
    if nama in menuMinuman.get_string():
        menuMinuman.del_row(menuMinuman.get_string().index(nama))
        print(f'{nama} telah dihapus dari menu minuman')
    else:
        print(f'{nama} tidak ditemukan dalam menu minuman')

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print('\n=== MENU ===')
    print('Makanan:')
    print(menuMakanan)
    print('Minuman:')
    print(menuMinuman)

# Fungsi untuk memesan makanan atau minuman
def pesanan_menu(menu, jenis_menu, pesanan):
    tampilkan_menu()
    nama = input(f'\nMasukkan nama {jenis_menu} yang ingin dipesan : ')
    jumlah = int(input(f'Masukkan jumlah {nama} yang ingin dipesan: '))
    pesanan.append((nama, jumlah))


# Fungsi untuk menghitung total biaya pesanan
def hitung_total_biaya(pesanan, menu):
    total_biaya_makanan = sum([menuMakanan.get_row(item)['Harga'] * jumlah for item, jumlah in pesanan])
    total_biaya_minuman = sum([menuMinuman.get_row(item)['Harga'] * jumlah for item, jumlah in pesanan])
    total_biaya = total_biaya_makanan + total_biaya_minuman
    return total_biaya

    total_biaya = 0
    for nama, jumlah in pesanan:
        for row in menu:
            if nama in row:
                harga = int(row['Harga'].replace('Rp. ', '').replace(',', ''))
                total_biaya += harga[1] * jumlah

                break
    return total_biaya

# Fungsi untuk menampilkan struk pembayaran
def tampilkan_struk(pesanan_makanan, pesanan_minuman, total_biaya):
    print('\n=== STRUK PEMBAYARAN ===')
    if pesanan_makanan:
        print('Makanan:')
        for item, jumlah in pesanan_makanan:
            print(f"{item} * {jumlah}")
    if pesanan_minuman:
        print('Minuman:')
        for item, jumlah in pesanan_minuman:
            print(f"{item} * {jumlah}")
    print(f'Total Biaya: Rp. {total_biaya:,.0f}')


# Fungsi utama untuk pemilihan dan pemesanan menu oleh pelanggan
def kasir_sederhana_pelanggan():
    print('Selamat datang di warmindo!')
    
    # Inisialisasi list pesanan
    pesanan_makanan = []
    pesanan_minuman = []
    
    # Memanggil pesan_menu() untuk makanan dan minuman
    pesanan_menu(menuMakanan, 'makanan', pesanan_makanan)
    pesanan_menu(menuMinuman, 'minuman', pesanan_minuman)
    
    if pesanan_makanan or pesanan_minuman:
        total_biaya = hitung_total_biaya(pesanan_makanan, menuMakanan) + hitung_total_biaya(pesanan_minuman, menuMinuman)
        
        # Menampilkan struk pembayaran jika ada pesanan
        if pesanan_makanan or pesanan_minuman:
            tampilkan_struk(pesanan_makanan, pesanan_minuman, total_biaya)
            print('Terima kasih atas pesanan Anda!')

while True:
    print('1. Admin')
    print('2. Customer')
    sebagai =int(input('masuk sebagai: '))

    if sebagai == 1 :
        print('Silahkan pilih menu admin')
        print('1. Menambah menu')
        print('2. Menampilkan daftar menu')
        print('3. Mengubah menu')
        print('4. Menghapus menu')
        menuAdm = int(input('pilih menu admin (1/2/3/4): '))
        
        if menuAdm == 1:    
            tambah_menu_makanan()
            tambah_menu_minuman()
            print(menuMakanan)
            print(menuMinuman)
        elif menuAdm == 2: 
            tampilkan_menu()
        elif menuAdm == 3: 
            edit_menu_makanan()
            edit_menu_minuman()
        elif menuAdm == 4:
            hapus_menu_makanan()
            hapus_menu_minuman()
        else:
            exit_program = True
            break
    elif sebagai == 2:
        kasir_sederhana_pelanggan()
        
