# Contoh sederhana encapsulation, Inheritance, Getter dan Setter

# Kelas Induk (Parent Class)
class Kendaraan:
    def __init__(self, merk, tahun):
        self.__merk = merk # Atribut private
        self.__tahun = tahun # Atribut private

        #Getter untuk merk
        def get_merk(self):
            return self.__merk
        
        #Setter untuk merk
        def set_merk(self,merk):
            self.__merk= merk

        #Getter untuk tahun
        def get_tahun(self):
            return self.__tahun

        #Setter untuk tahun
        def set_tahun(self, tahun):
            if tahun > 0:
                self.__tahun = tahun
            else:
                print("Tahun tidak valid!")

# Kelas Turunan (Child Class) yang mewarisi dari kendaraan
class Mobil(kendaraan):
    def __init__(self, merk, tahun, tipe):
        super().__init__(merk, tahun) # Memanggil konstruktor kelas induk
        self.__tipe = tipe # Menambahkan atribut tipe mobil

        # Getter untuk tipe mobil
        def get_tipe(self):
            return self.__tipe

        # Setter untuk tipe mobil
        def set_tipe(self, tipe):
            self.__tipe = tipe

# Menggunakan class Mobil
mobil_saya = Mobil("Toyota", 2020, "SUV")

# Menampilkan informasi mobil menggunakan getter
print(f"merk mobil: {mobil_saya.get_merk()}")
print(f"Tahun mobil: {mobil_saya.get_tahun()}")
print(f"Tipe mobil: {mobil_saya.get_tipe()}")

# Mengubah data menggunakan setter
mobil_saya.set_merk("Honda")
mobil_saya._set_Tahun(2022)
mobil_saya.set_tipe("sedan")

# Menampilkan informasi mobil setelah perubahan
print(f"Merk mobil baru: {mobil_saya.get_merk()}")
print(f"Tahun mobil baru: {mobil_saya.get_tahun()}")
print(f"Tipe mobil baru: {mobil_saya.get_tipe()}")
