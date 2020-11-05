#Sistem Matematika
#Menghitung Luas dan Keliling Bangun Datar

def luas_persegi (s):
    luas = s*s
    return luas
def keliling_persegi (s):
    keliling = 2*(s+s)
    return keliling
def luas_persegipanjang (p,l):
    luas = p*l
    return luas
def keliling_persegipanjang (p,l):
    keliling = 2*(p+l)
    return keliling
def luas_segitiga (a,t):
    luas = (a*t)/2
    return luas
def keliling_segitiga (a,b,c):
    keliling = a+b+c
    return keliling
def luas_lingkaran (r):
    luas = 3,14*r*r
    return luas
def keliling_lingkaran (r):
    keliling = 2*3,14*r
    return keliling
def luas_jajargenjang (a,t):
    luas = a*t
    return luas
def keliling_jajargenjang (a,b):
    keliling = 2*(a+b)
    return keliling
pilihan = 1
while pilihan!=0:
    print("1. Luas persegi")
    print("2. Keliling persegi")
    print("3. Luas persegi panjang")
    print("4. Keliling persegi panjang")
    print("5. Luas segitiga")
    print("6. Keliling segitiga")
    print("7. Luas lingkaran")
    print("8. Keliling lingkaran")
    print("9. Luas jajar genjang")
    print("0. Keliling jajar genjang")
    
    pilihan = int(input("Masukkan pilihan : "))
    print('')
    if pilihan == 1:
        print ("Luas persegi ")
        print('')
        s = int (input("Masukkan nilai s : "))
        print("luasnya adalah :",luas_persegi (s))
    elif pilihan == 2 :
        print ("Keliling Persegi ")
        print('')
        s = int (input("Masukkan nilai s : "))
        print("Kelilingnya adalah :",keliling_persegi (s))
    elif pilihan == 3:
        print ("Luas persegi panjang")
        print('')
        p = int (input("Masukkan nilai p : "))
        l = int (input("Masukkan nilai l : "))
        print("luasnya adalah :",luas_persegipanjang (p,l))
    elif pilihan == 4 :
        print ("Keliling Persegi panjang ")
        print('')
        p = int (input("Masukkan nilai p : "))
        l = int (input("Masukkan nilai l : "))
        print("Kelilingnya adalah :",keliling_persegipanjang (p,l))
    elif pilihan == 5:
        print ("Luas segitiga ")
        print('')
        a = int (input("Masukkan nilai a : "))
        t = int (input("Masukkan nilai t : "))
        print("luasnya adalah :",luas_segitiga (a,t))
    elif pilihan == 6 :
        print ("Keliling segitiga ")
        print('')
        a = int (input("Masukkan nilai a : "))
        b = int (input("Masukkan nilai b : "))
        c = int (input("Masukkan nilai c : "))
        print("Kelilingnya adalah :",keliling_segitiga (a,b,c))
    elif pilihan == 7:
        print ("Luas lingkaran ")
        print('')
        r = int (input("Masukkan nilai r : "))
        print("luasnya adalah :",luas_lingkaran (r))
    elif pilihan == 8 :
        print ("Keliling lingkaran ")
        print('')
        r = int (input("Masukkan nilai r : "))
        print("Kelilingnya adalah :",keliling_lingkaran (r))
    elif pilihan == 9:
        print ("Luas jajar genjang ")
        print('')
        a = int (input("Masukkan nilai a : "))
        t = int (input("Masukkan nilai t : "))
        print("luasnya adalah :",luas_jajargenjang (a,t))
    elif pilihan == 0 :
        print ("Keliling jajar genjang ")
        print('')
        a = int (input("Masukkan nilai a : "))
        b = int (input("Masukkan nilai b : "))
        print("Kelilingnya adalah :",keliling_jajargenjang (a,b))
    else :
        print("Maaf Pilihan Anda Tidak Ada")
        print('')
