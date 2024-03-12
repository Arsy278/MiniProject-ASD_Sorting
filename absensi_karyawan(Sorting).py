from datetime import datetime
import os
from prettytable import PrettyTable

os.system('cls' if os.name == 'nt' else 'clear')

class Node:
    def __init__(self, nama_karyawan, waktu, tanggal):
        self.nama_karyawan = nama_karyawan
        self.waktu = waktu
        self.tanggal = tanggal
        self.next = None

class PendataanKehadiran:
    def __init__(self):
        self.head = None

    def lihatSemuaKehadiran(self):
        current = self.head
        if not current:
            print("Belum ada data kehadiran yang dicatat.")
            input("Tekan Enter untuk melanjutkan...")
            return
        nomor_awal = 1
        tabel = PrettyTable()
        tabel.field_names= ["No", "Nama Karyawan", "Jam", "Tanggal"]
        while current:
            tabel.title = "Daftar Kehadiran"
            tabel.add_row([nomor_awal, current.nama_karyawan, current.waktu, current.tanggal])
            nomor_awal += 1
            current = current.next
        print(tabel)
        input("Tekan Enter untuk kembali...")

    def perbaruiKehadiran(self, nama_karyawan, waktu, tanggal):
        current = self.head
        found = False
        while current:
            if current.nama_karyawan == nama_karyawan:
                current.waktu = datetime.now().strftime("%H:%M:%S")
                current.tanggal = datetime.now().strftime("%d-%m-%Y")
                print("\nAbsensi berhasil diperbarui!, berikut deskripsi absensi :")
                tabel = PrettyTable()
                tabel.title = "Daftar Kehadiran"
                tabel.field_names= ["Nama Karyawan", "Jam", "Tanggal"]
                tabel.add_row([current.nama_karyawan, current.waktu, current.tanggal])
                print(tabel)
                found = True
                break
            current = current.next
            return waktu, tanggal
        if not found:
            print("Karyawan tidak ditemukan dalam data kehadiran.")
        input("Tekan Enter untuk kembali...")

# menambah node
    def tambahNodeDiAwal(self, nama_karyawan, tanggal, waktu):
        new_node = Node(nama_karyawan, tanggal, waktu)
        new_node.next = self.head
        self.head = new_node
        print(f"Data ditambahkan di awal.")
        input("Tekan Enter untuk kembali...")

    def tambahNodeDiTengah(self, nama_karyawan, tanggal, posisi, waktu):
        if posisi <= 0:
            print("Index harus lebih besar dari 0.")
            return
        new_node = Node(nama_karyawan, tanggal, waktu)
        current = self.head
        count = 1
        while current and count < posisi:
            current = current.next
            count += 1
        if not current:
            print("Index melebihi panjang list.")
            return
        new_node.next = current.next
        current.next = new_node
        print(f"Data ditambahkan di tengah.")
        input("Tekan Enter untuk kembali...")

    def tambahNodeDiAkhir(self, nama_karyawan, tanggal, waktu):
        new_node = Node(nama_karyawan, tanggal, waktu)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

# menghapus node
    def hapusNodeDiAwal(self):
        if not self.head:
            print("List sudah kosong.")
            return
        self.head = self.head.next
        print("Data dihapus di awal list.")

    def hapusNodeDiTengah(self, posisi):
        if not self.head:
            print("List sudah kosong.")
            return
        if posisi <= 0:
            print("Index harus lebih besar dari 0.")
            return
        current = self.head
        if posisi == 1:
            self.head = current.next
            return
        count = 1
        prev = None
        while current and count < posisi:
            prev = current
            current = current.next
            count += 1
        if not current:
            print("Index melebihi panjang list.")
            return
        prev.next = current.next

    def hapusNodeDiAkhir(self):
        if not self.head:
            print("List sudah kosong.")
            return
        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        if prev:
            prev.next = None
        else:
            self.head = None
        print("Data terakhir pada list berhasil dihapus.")
    
    def hapusSemuaData(self):
        self.head = None
        print("Semua data kehadiran berhasil dihapus.")
        input("Tekan Enter untuk kembali...")

# sorting dengan menggunakan teknik merge sort
    def merge(self, left, right, sort_by='nama', ascending=True):
        result = []
        while len(left) > 0 and len(right) > 0:
            if sort_by == 'nama':
                if ascending:
                    if left[0].nama_karyawan[0] < right[0].nama_karyawan[0]:
                        result.append(left[0])
                        left.pop(0)
                    else:
                        result.append(right[0])
                        right.pop(0)
                else:  # dirutukan secara descending
                    if left[0].nama_karyawan[0] > right[0].nama_karyawan[0]:
                        result.append(left[0])
                        left.pop(0)
                    else:
                        result.append(right[0])
                        right.pop(0)
            elif sort_by == 'waktu':
                if ascending:
                    if left[0].waktu < right[0].waktu:
                        result.append(left[0])
                        left.pop(0)
                    else:
                        result.append(right[0])
                        right.pop(0)
                else:  # dirutukan secara descending
                    if left[0].waktu > right[0].waktu:
                        result.append(left[0])
                        left.pop(0)
                    else:
                        result.append(right[0])
                        right.pop(0)
        result += left
        result += right
        return result

    def merge_sort(self, data, sort_by='nama', ascending=True):
        if len(data) <= 1:
            return data

        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        left = self.merge_sort(left, sort_by, ascending)
        right = self.merge_sort(right, sort_by, ascending)

        return self.merge(left, right, sort_by, ascending)

    def lihatSemuaKehadiranSorted(self):
        current = self.head
        if not current:
            print("Belum ada data kehadiran yang dicatat.")
            input("Tekan Enter untuk melanjutkan...")
            return
        data = []
        while current:
            data.append(current)
            current = current.next
        while True:
            print("\nPilih metode pengurutan data:")
            print("1. Berdasarkan nama.")
            print("2. Berdasarkan jam kehadiran.")
            print("3. Kembali")
            opsi = input("Pilih metode (1/2/3): ")
            sort_by = 'nama'
            ascending = True
            if opsi == '1':
                print("\nUrutkan nama secara ascending(1) atau descending(2)?")
                opsi = input("Pilih (1/2): ")
                if opsi == '1':
                    ascending = True
                else:
                    ascending = False
                break
            elif opsi == '2':
                print("\nUrutkan jam kehadiran secara ascending(1) atau descending(2)?")
                opsi = input("Pilih (1/2): ")
                if opsi == '1':
                    sort_by = 'waktu'
                    ascending = True
                else:
                    sort_by = 'waktu'
                    ascending = False
                break
            else:
                print("Input tidak valid. Silakan pilih 1 atau 2.")

        sorted_data = self.merge_sort(data, sort_by, ascending)

        nomor_awal = 1
        tabel = PrettyTable()
        tabel.field_names= ["No", "Nama Karyawan", "Waktu" ,"Tanggal"]
        for node in sorted_data:
            tabel.add_row([nomor_awal, node.nama_karyawan, node.waktu, node.tanggal])
            nomor_awal += 1
        print("\nDaftar Kehadiran (Diurutkan):")
        print(tabel)
        input("Tekan Enter untuk melanjutkan...")

pendataan = PendataanKehadiran()

def ambil_input():
    while True:
        nama_karyawan = input("Masukkan Nama: ")
        if nama_karyawan.isdigit():
            print("Data hanya boleh diisi oleh abjad, silahkan coba lagi.")
        else: 
            break
    tanggal = datetime.now().strftime("%d-%m-%Y")
    waktu = datetime.now().strftime("%H:%M:%S")
    print("\nAbsensi berhasil!, berikut deskripsi waktu absensi :")
    
    tabelAbsensi = PrettyTable()
    tabelAbsensi.field_names = ["Nama Karyawan", "Jam", "Tanggal"]
    tabelAbsensi.add_row([nama_karyawan, waktu, tanggal])
    print(tabelAbsensi)
    return nama_karyawan, waktu, tanggal

def perbaruiAbsen():
    nama_karyawan = input("Masukkan nama karyawan yang ingin diubah: ")
    return nama_karyawan

while True:
    print(f"{'-'*40:^40}")
    print(f"{'Program Pendataan Kehadiran Karyawan':^40}")
    print(f"{'-'*40:^40}")
    print("Pilihan Menu:")
    print("1. Isi Absensi")
    print("2. Lihat Data Absensi")
    print("3. Perbarui Data Absensi")
    print("4. Hapus Absensi")
    print("5. Urutkan data absensi")
    print("6. Keluar")
    pilihan = input("Pilih menu (1/2/3/4/5/6): ")
    if pilihan == '1':
        opsi = input("\nDimana data ingin ditaruh ? \n1. Awal \n2. Tengah \n3. Akhir \n(1/2/3): ")
        if opsi in ['1', '2', '3']:
            if opsi == '1':
                nama_karyawan, tanggal, waktu = ambil_input()
                pendataan.tambahNodeDiAwal(nama_karyawan, tanggal, waktu)
            elif opsi == '2':
                posisi= int(input("Masukkan posisi(index) data: "))
                nama_karyawan, tanggal, waktu = ambil_input()
                pendataan.tambahNodeDiTengah(nama_karyawan, tanggal, posisi, waktu)
            elif opsi == '3':
                nama_karyawan, tanggal, waktu = ambil_input()
                pendataan.tambahNodeDiAkhir(nama_karyawan, tanggal, waktu)
                print(f"Data ditambahkan di akhir.")
                input("Tekan Enter untuk kembali...")
        else:
            print("Input tidak benar. Data tidak berhasil ditambahkan.")
    elif pilihan == '2':
        pendataan.lihatSemuaKehadiran()
    elif pilihan == '3':
        nama_karyawan = perbaruiAbsen()
        pendataan.perbaruiKehadiran(nama_karyawan, waktu ,tanggal)
    elif pilihan == '4':
        opsi = input("\nData mana yang ingin dihapus ? \n1. Awal \n2. Tengah \n3. Akhir \n4. Hapus semua data \n(1/2/3): ")
        if opsi in ['1', '2', '3', '4']:
            if opsi == '1':
                pendataan.hapusNodeDiAwal()
            elif opsi == '2':
                posisi = int(input("Masukkan posisi data yang akan dihapus: "))
                pendataan.hapusNodeDiTengah(posisi)
                print(f"Data dihapus pada posisi ke-{posisi}.")
            elif opsi == '3':
                pendataan.hapusNodeDiAkhir()
            elif opsi == '4':
                pendataan.hapusSemuaData()
        else:
            print("Input tidak valid. Node tidak dihapus.")
    elif pilihan == '5':
        while True:    
            pendataan.lihatSemuaKehadiranSorted()
            kembali = input("Ketik x untuk kembali ke menu utama.")
            if kembali.lower() == 'x':
                break
    elif pilihan == '6':
        print("┌───────────────────────────────────────────────┐")
        print("│                                               │")
        print("│               Terima kasih !                  │")
        print("│                                               │")
        print("│         Semoga harimu menyenangkan.           │")
        print("│                                               │")
        print("│                                      -arsy    │")
        print("└───────────────────────────────────────────────┘")
        break
    else:
        print("Input tidak valid. Silakan pilih menu yang sesuai.")