class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa

    # Getter untuk mendapatkan nilai nim
    def get_nim(self):
        return self.__nim

    # Setter untuk mengubah nilai nim
    def set_nim(self, nim):
        self.__nim = nim

    # Getter untuk mendapatkan nilai nama
    def get_nama(self):
        return self.__nama

    # Setter untuk mengubah nilai nama
    def set_nama(self, nama):
        self.__nama = nama

    # Method 1: Mengembalikan informasi lengkap mahasiswa
    def informasi_mahasiswa(self):
        return f"NIM: {self.__nim}, Nama: {self.__nama}, Angkatan: {self.angkatan}, Mahasiswa: {self.isMahasiswa}"

    # Method 2: Mengembalikan status keaktifan mahasiswa
    def status_keaktifan(self):
        if self.isMahasiswa:
            return "Mahasiswa Aktif"
        else:
            return "Bukan Mahasiswa"

    # Method 3: Mengembalikan tahun kelulusan
    def tahun_kelulusan(self):
        return self.angkatan + 4 if self.isMahasiswa else "Tidak dapat diprediksi"


# Inisialisasi dua objek Mahasiswa
nim=str(input("Masukkan Nim: "))
nama=str(input("Input Nama: "))
angkatan=int(input("Input Angkatan: "))
mahasiswa1 = Mahasiswa(nim,nama,angkatan)


# Menggunakan getter untuk mendapatkan nilai nim dan nama
print(f"Nama mahasiswa1: {mahasiswa1.get_nama()}, NIM mahasiswa1: {mahasiswa1.get_nim()}")

# Menggunakan setter untuk mengubah nilai nim dan nama
mahasiswa1.set_nim("654321")
mahasiswa1.set_nama("Alice Wonderland")

# Menggunakan method pada objek
print(mahasiswa1.informasi_mahasiswa())
print(mahasiswa1.status_keaktifan())
print(f"Tahun kelulusan mahasiswa1: {mahasiswa1.tahun_kelulusan()}")
