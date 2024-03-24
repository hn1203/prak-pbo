class Persegi:
  def __init__(self, sisi):
    self.sisi = sisi

  def HitungLuas(self):
    return self.sisi ** 2

class Lingkaran:
  def __init__(self, Jari):
    self.Jari = Jari

  def HitungLuas(self):
    return 3.14 * self.Jari * self.Jari

persegi = Persegi(5)
lingkaran = Lingkaran(3)

print(f"Luas Persegi: {persegi.HitungLuas()}")
print(f"Luas Lingkaran: {lingkaran.HitungLuas()}")
