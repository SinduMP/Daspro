



# MATRIKS 
R = int(input("Masukkan jumlah Baris:")) 
C = int(input("Masukkan jumlah Kolom:"))  
# Menganalisis data
matrix = [] 
print("Masukkan anggota (urut dari baris awal):") 
# input 
for i in range(R):          # looping Baris
    a =[] 
    for j in range(C):      # Looping kolom
         a.append(int(input("anggota :"))) 
    matrix.append(a) 
# Cetak
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print()
