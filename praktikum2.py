
# Superclass
class Kendaraan:
    def __init__(self, merk, kecepatan):
        self.merk = merk
        self.kecepatan = kecepatan

# Subclass Mobil
class Mobil(Kendaraan):
    def info(self):
        print(f"Mobil {self.merk} melaju {self.kecepatan} km/jam.")

# Subclass Motor
class Motor(Kendaraan):
    def info(self):
        print(f"Motor {self.merk} melaju {self.kecepatan} km/jam.")

# Membuat objek
m1 = Mobil("SUPRA BAPAK", 9000)
mo1 = Motor("MIO RESING", 700)

# Menampilkan informasi
m1.info()
mo1.info()