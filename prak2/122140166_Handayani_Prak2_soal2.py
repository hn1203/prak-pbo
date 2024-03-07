def beli_baju (func):
    def wrapper (*args):
        print("Pesanan Anda adalah:")
        func(*args)
    return wrapper

class Baju:
    
    def __init__(self, merk, harga):
        self.brand = merk
        self.harga = harga
    
    @beli_baju
    def pesanan (self):
        print (f"Baju dengan brand {self.brand} \ndengan harga {self.harga}")
        
    def __del__ (self):
        print("Baju telah dibayar")
        
uniqlo = Baju("Uniqlo", "Rp299000")
uniqlo.pesanan()