#class color
class color:
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  END = '\033[0m'

# fungsi,rumus data
def rumus():
  global anak,gajipokok,gajikotor,persen,jumlahanak,hitunganak,gaji
  hitunganak = 100000
  anak = jumlahanak * hitunganak
  gajikotor = gajipokok + anak
  persen = (gajikotor * 5) / 100
  gaji = gajikotor - persen
def kesejahteraan():
  global keadaan
  if gaji > 2000000:
    keadaan =("Sejahtera")
  else :
    keadaan =("Belum Sejahtera")
def cetak ():
  print("Jabatan  :",jabatan)
  print("Gaji     : Rp.",gaji)
  print("Keadaan  :",keadaan)
  print('')

#Memasukkan data karyawan
print("==================")
print(color.BOLD + color.BLUE +"PT. POLINES JAYA" + color.END)
print(color.BOLD + color.GREEN + "Data Karyawan" + color.END)
print("==================")
print('')
print(color.BOLD + "Masukkan data :" + color.END)
nama =(input("Nama     : "))
#jabatan:
#1. Direktur = Rp.8000000
#2. Supervisor = Rp.4000000
#3. Operator = Rp.2000000
#4. Lainnya = Rp.2000000
golongan =int(input("golongan : "))
jumlahanak =int(input("Jumlah anak( jika tidak punya: 0 ) : "))


if golongan == 1:
  jabatan ="Direktur"
  gajipokok = 8000000
  rumus()
  kesejahteraan()
  cetak()
elif golongan == 2:
  jabatan ="Supervisor"
  gajipokok = 4000000
  rumus()
  kesejahteraan()
  cetak()
elif golongan == 3:
  jabatan ="Operator"
  gajipokok = 2000000
  rumus()
  kesejahteraan()
  cetak()
else:
  jabatan ="Karyawan"
  gajipokok == 2000000
  rumus()
  kesejahteraan()
  cetak()
