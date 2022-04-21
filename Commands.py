from csv_parser import appendMatrix,cari,save
from Function import length

def register(folder):
    print("Daftarkan akun Anda")
    userfile = folder[3]
    id = length(userfile)
    nama = str(input("Masukkan nama : "))
    username = str(input("Masukkan username : "))
    password = str(input("Masukkan password : "))
    role = "user"
    saldo = 0
    cekUsername = cari(userfile, "username", username, "id")
    if cekUsername == "x":
        folder[3] = appendMatrix(userfile, [str(id),username,nama,password,role,str(saldo)])
        save(folder)
    else:
        print("Username sudah terpakai. Silakan ganti username.")
        register(folder)

def login(folder):
    print("Selamat datang kembali.")
    file = folder[3]
    inputUsername = str(input("Masukkan username : "))
    inputPassword = str(input("Masukkan password : "))
    password = cari(file, "username", inputUsername, "password")
    id = cari(file, "username", inputUsername, "id")
    if password == inputPassword:
        return id
    else:
        print("Password atau username salah atau tidak ditemukan.")
        login(folder)

"""def gantiPassword():
    file = readFile("user.csv")
    changevalue(file, "password", "3", "143")
    print(file)
    writeFile("user.csv", file, 6)"""
