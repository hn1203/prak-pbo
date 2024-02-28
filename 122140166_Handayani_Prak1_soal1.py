lower = int(input("batas bawah: "))
upper = int(input("batas atas: "))

def bil_ganjil(lower, upper):
    if lower < 0 or upper < 0:
        print("Batas bawah dan atas yang dimasukkan tidak boleh di bawah Nol")
        return
    
    total=0
    for bil in range(lower, upper):
        if bil % 2 != 0:
            print (bil)
        
            total+=bil
           
    print ("Total:", total)

bil_ganjil(lower, upper)

