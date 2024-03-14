class Dagangan:
    jumlah_barang = 0
    list_barang = []

    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga
        Dagangan.jumlah_barang += 1
        Dagangan.list_barang.append((nama, stok, harga))

    @classmethod
    def lihat_barang(cls):
        print("Jumlah barang dagangan pada toko:", cls.jumlah_barang, "buah")
        for i, barang in enumerate(cls.list_barang, start=1):
            print(f"{i}. {barang[0]} seharga Rp {barang[2]} (stok: {barang[1]})")

    def __del__(self):
        Dagangan.jumlah_barang -= 1
        hapus_item = None
        for i, barang in enumerate(Dagangan.list_barang):
            if barang[0] == self.__nama:
                hapus_item = Dagangan.list_barang.pop(i)
                break
        if hapus_item:
            print(f"{hapus_item[0]} dihapus dari toko!")
            print()
        else:
            print(f"{self.__nama} tidak ditemukan di toko.")


# Contoh penggunaan
Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)
Dagangan.lihat_barang()

del Dagangan1
Dagangan.lihat_barang()
