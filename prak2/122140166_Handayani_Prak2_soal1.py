class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa

    def get_nim(self):
        return self.__nim
        
    def set_nim(self, nim):
        self.__nim = nim

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def informasi_mahasiswa(self):
        return f"NIM: {self.__nim}, Nama: {self.__nama}, Angkatan: {self.angkatan}, Mahasiswa: {self.isMahasiswa}"

    def status_keaktifan(self):
        if self.isMahasiswa:
            return "Mahasiswa Aktif"
        else:
            return "Bukan Mahasiswa"

    def tahun_kelulusan(self):
        return self.angkatan + 4 if self.isMahasiswa else "Tidak teridentifikasi"

nim=str(input("Masukkan Nim: "))
nama=str(input("Input Nama: "))
angkatan=int(input("Input Angkatan: "))
mahasiswa1 = Mahasiswa(nim,nama,angkatan)

print(f"Nama mahasiswa1: {mahasiswa1.get_nama()}, NIM mahasiswa1: {mahasiswa1.get_nim()}")

mahasiswa1.set_nim("122140166")
mahasiswa1.set_nama("ANI")

print(mahasiswa1.informasi_mahasiswa())
print(mahasiswa1.status_keaktifan())
print(f"Tahun kelulusan mahasiswa1: {mahasiswa1.tahun_kelulusan()}")
