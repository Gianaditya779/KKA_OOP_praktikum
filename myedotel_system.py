from abc import ABC, abstractmethod

# ===== ABSTRACTION (KERANGKA DASAR) =====
class KamarHotel(ABC):
    """Abstract Class untuk mendefinisikan struktur kamar hotel"""
    
    def __init__(self, nama_kamar, harga_dasar):
        self.__nama_kamar = nama_kamar  # Private Attribute
        self.__harga_dasar = harga_dasar  # Private Attribute
        self.__stok = 0  # Private Attribute (jumlah kamar tersedia)
    
    # ===== ENCAPSULATION (KEAMANAN DATA) =====
    @property
    def nama_kamar(self):
        """Getter untuk nama kamar"""
        return self.__nama_kamar
    
    @property
    def harga_dasar(self):
        """Getter untuk harga dasar"""
        return self.__harga_dasar
    
    @property
    def stok(self):
        """Getter untuk melihat stok kamar"""
        return self.__stok
    
    def tambah_stok(self, jumlah):
        """Setter untuk menambah stok dengan validasi"""
        if jumlah < 0:
            print(f"❌ Gagal update stok {self.__nama_kamar}! Stok tidak boleh negatif ({jumlah}).")
            return False
        self.__stok += jumlah
        print(f"✓ Berhasil menambahkan stok {self.__nama_kamar}: {jumlah} unit.")
        return True
    
    # ===== ABSTRACT METHOD (HARUS DIIMPLEMENTASIKAN DI CHILD CLASS) =====
    @abstractmethod
    def tampilkan_detail(self):
        """Method untuk menampilkan detail kamar (OVERRIDE di child class)"""
        pass
    
    @abstractmethod
    def hitung_harga_total(self, jumlah_malam):
        """Method untuk menghitung harga total dengan pajak (OVERRIDE di child class)"""
        pass


# ===== INHERITANCE (PEWARISAN) =====
class KamarDeluxe(KamarHotel):
    """Class Kamar Deluxe - mewarisi dari KamarHotel"""
    
    def __init__(self, nama_kamar, harga_dasar, fasilitas):
        super().__init__(nama_kamar, harga_dasar)
        self.fasilitas = fasilitas  # Atribut tambahan
        self.pajak_persen = 10  # Pajak 10% dari harga dasar
    
    # ===== POLYMORPHISM (OVERRIDE METHOD) =====
    def tampilkan_detail(self):
        """Menampilkan detail Kamar Deluxe"""
        return f"[DELUXE] {self.nama_kamar} | Fasilitas: {self.fasilitas}"
    
    def hitung_harga_total(self, jumlah_malam):
        """Menghitung harga total untuk Kamar Deluxe (10% pajak)"""
        harga_per_malam = self.harga_dasar
        pajak_per_malam = harga_per_malam * (self.pajak_persen / 100)
        harga_per_malam_dengan_pajak = harga_per_malam + pajak_per_malam
        subtotal = harga_per_malam_dengan_pajak * jumlah_malam
        
        return {
            'harga_dasar': harga_per_malam,
            'pajak_per_malam': pajak_per_malam,
            'pajak_persen': self.pajak_persen,
            'jumlah_malam': jumlah_malam,
            'subtotal': subtotal
        }


class KamarStandard(KamarHotel):
    """Class Kamar Standard - mewarisi dari KamarHotel"""
    
    def __init__(self, nama_kamar, harga_dasar, kapasitas):
        super().__init__(nama_kamar, harga_dasar)
        self.kapasitas = kapasitas  # Atribut tambahan
        self.pajak_persen = 5  # Pajak 5% dari harga dasar
    
    # ===== POLYMORPHISM (OVERRIDE METHOD) =====
    def tampilkan_detail(self):
        """Menampilkan detail Kamar Standard"""
        return f"[STANDARD] {self.nama_kamar} | Kapasitas: {self.kapasitas}"
    
    def hitung_harga_total(self, jumlah_malam):
        """Menghitung harga total untuk Kamar Standard (5% pajak)"""
        harga_per_malam = self.harga_dasar
        pajak_per_malam = harga_per_malam * (self.pajak_persen / 100)
        harga_per_malam_dengan_pajak = harga_per_malam + pajak_per_malam
        subtotal = harga_per_malam_dengan_pajak * jumlah_malam
        
        return {
            'harga_dasar': harga_per_malam,
            'pajak_per_malam': pajak_per_malam,
            'pajak_persen': self.pajak_persen,
            'jumlah_malam': jumlah_malam,
            'subtotal': subtotal
        }


# ===== POLYMORPHISM (FITUR PEMESANAN) =====
def proses_transaksi(daftar_pemesanan):
    """
    Fungsi untuk memproses transaksi pemesanan kamar.
    Menerima list yang berisi tuple: (kamar, jumlah_malam)
    Menampilkan detail dan total biaya otomatis.
    """
    print("\n" + "="*60)
    print("--- PEMESANAN ---")
    print("="*60)
    
    total_tagihan = 0
    nomor_urut = 1
    
    for kamar, jumlah_malam in daftar_pemesanan:
        detail = kamar.tampilkan_detail()
        harga_info = kamar.hitung_harga_total(jumlah_malam)
        
        print(f"\n{nomor_urut}. {detail}")
        print(f"   Harga Dasar/Malam: Rp {harga_info['harga_dasar']:,} | Pajak ({harga_info['pajak_persen']}%): Rp {int(harga_info['pajak_per_malam']):,}")
        print(f"   Menginap: {jumlah_malam} malam | Subtotal: Rp {int(harga_info['subtotal']):,}")
        
        total_tagihan += harga_info['subtotal']
        nomor_urut += 1
    
    print("\n" + "-"*60)
    print(f"--- TOTAL TAGIHAN: Rp {int(total_tagihan):,} ---")
    print("-"*60)
    
    return total_tagihan


# ===== MAIN PROGRAM =====
if __name__ == "__main__":
    print("="*60)
    print("SISTEM MANAJEMEN KAMAR HOTEL - MyEdotel")
    print("="*60)
    
    # ===== 3) ALUR PROGRAM (USER STORY) =====
    # a) Admin membuat data kamar
    print("\n--- SETUP DATA KAMAR ---")
    
    kamar_deluxe = KamarDeluxe(
        nama_kamar="Kamar Deluxe Sea View",
        harga_dasar=1500000,
        fasilitas="Private Pool"
    )
    
    kamar_standard = KamarStandard(
        nama_kamar="Kamar Standard Superior",
        harga_dasar=500000,
        kapasitas="2 Orang"
    )
    
    # b) Admin mencoba mengisi stok kamar dengan angka negatif
    kamar_deluxe.tambah_stok(10)
    kamar_standard.tambah_stok(-5)  # Ini akan ditolak karena negatif
    kamar_standard.tambah_stok(20)
    
    # c) Tamu memesan 2 malam Kamar Deluxe dan 1 malam Kamar Standard
    daftar_pemesanan = [
        (kamar_deluxe, 2),      # 2 malam Kamar Deluxe
        (kamar_standard, 1)     # 1 malam Kamar Standard
    ]
    
    # d) Program menampilkan detail kamar dan total tagihan akhir
    proses_transaksi(daftar_pemesanan)
    
    print("\n" + "="*60)
    print("✓ Pemesanan selesai!")
    print("="*60)
