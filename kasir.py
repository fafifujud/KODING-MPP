
class Barang:
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

    def hitung_total(self):
        return self.harga * self.jumlah

    def tampilkan_barang(self):
        print("Nama Barang:", self.nama)
        print("Harga Barang: Rp", self.harga)
        print("Jumlah:", self.jumlah)
        print("Total Harga: Rp", self.hitung_total())
        print("------------------------")


barang1 = Barang("Buku", 5000, 3)
barang2 = Barang("Pulpen", 3000, 2)

barang1.tampilkan_barang()
barang2.tampilkan_barang()

total_belanja = barang1.hitung_total() + barang2.hitung_total()
print("Total Belanja: Rp", total_belanja)
