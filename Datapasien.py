# Tugas UTS Dasar Dasar Pemrograman
# Nama  : Sindu Masri Priandana
# Kelas : IK-1E
# Politeknik Negeri Semarang

# Program data pasien:

i=n=0
n==1
#fungsi
def cetak():
    def ulang():
        ulang = input("Apa anda ingin melihat data lain ( y / t ): ")
        if ulang == 'y':
          cetak()
        elif ulang == 't':
          exit
        else:
          print("Maaf yang anda masukkan salah")
        return ulang
    print("="*112)
    print("Daftar: ")
    print("1.Nama Pasien")
    print("2.Data Pasien")
    print("="*112)
    data = input("Melihat data: (1 atau 2): ")
    if data == '1' :
        print('')
        print("="*112)
        print("Daftar Nama Pasien: ")
        i = len(nama)
        for n in range(i):
            print(n+1,'.',nama[n])
        print("="*112)
        print('')
        ulang()
    elif data == '2':
        print('')
        print("Data Pasien: ")
        print("="*112)
        print ("No \t| Nama \t\t\t| Umur \t\t\t| Alamat(daerah) \t\t\t| Gejala ")
        print("-"*112)
        i = len(nama)
        for n in range(i):
            print(n+1,'.\t|',nama[n][0:11],'\t\t|',umur[n],'\t\t\t|',alamat[n][0:15],'\t\t\t\t|',gejala[n],'')
        print("="*112)
        ulang()
    else:
        print("Maaf yang anda masukkan salah")
        cetak()

#aplikasi tentang pendataan

nama   = []
umur   = []
alamat = []
gejala = []
#pengulangan
stop = False
i = 1
#mengisi data
while (not stop):
    print("Pengisian data pasien:")
    nama_seseorang = input(" {}.Nama   : ".format(i))
    umur_seseorang = input("   Umur   : ")
    alamat_seseorang = input("   Alamat : ")
    gejala_seseorang = input("   Gejala : ")
    nama.append(nama_seseorang)
    umur.append(umur_seseorang)
    alamat.append(alamat_seseorang)
    gejala.append(gejala_seseorang)

    #peningkatan i
    i+=1
    tanya = input("Mau isi lagi? ( y / t ): ")
    
    if(tanya=='t'):
      stop = True
    
#cetak data

cetak()
