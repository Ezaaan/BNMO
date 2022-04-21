from Function import length
import os

#Membaca data file dan dirubah menjadi array matriks
# X: nama file csv (str; Ex: "game.csv")
def readFile(X):
    with open(X, "r+") as file1:
        #Inisialisasi
        isi=file1.readlines()
        category=1

        #Menghitung jumlah rows/baris
        rows=length(isi)

        #Menghitung jumlah karakter tiap baris
        size=[-1 for i in range (rows)]
        for i in range (rows):
            for j in isi[i]:
                size[i]+=1
            if i==(rows-1):
                size[i]+=1

        #Menghitung jumlah kategori
        for i in range (size[0]):
            if ((isi[0])[i])==";":
                category+=1
        
        #Memisah setiap kategori pada tiap baris
        for x in range (rows):
            Temp=["" for i in range (category)]
            baris=isi[x]
            for i in range (category):
                if i==0:
                    j=0
                else:
                    j+=1
                while j < size[x]:
                    if baris[j]==";":
                        break
                    Temp[i]+=baris[j]
                    j+=1
            isi[x]=Temp
    return isi

#Menambah atau meng-append data baru ke file dan dirubah dari bentuk matriks menjadi semicolon-seperated-value
# X: Nama file csv (str; File harus ada; Ex: "game.csv");   Y=Data yang ingin dimasukkan (dalam bentuk array 1D)
def appendFile(X, Y):
    with open(X, "a+") as file1:
        file1.write("\n")
        category=length(Y)
        
        for i in range (category):
            file1.write(Y[i])
            if i!=(category-1):
                file1.write(";")

#Mengganti SELURUH data/meng-overwrite data pada file dengan yang baru JIKA FILE SUDAH ADA (Dipakai ketika ingin merubah suatu data yang sudah ada)
#Membuat file baru berisi data JIKA FILE TIDAK ADA
def writeFile(X, Y, Z): # X: Nama file csv (str; File boleh ada dan tidak; Ex: "game.csv");Y=Data yang ingin dimasukkan (Harus dalam bentuk matriks 2D); Z=Jumlah kategori (int)
    #Menghitung jumlah baris
    count=length(Y)

    with open(X, 'w+') as file1:
        for i in range (count):
            for j in range (Z):
                file1.write(Y[i][j])
                if j!=(Z-1):
                    file1.write(";")
            if i!=(count-1):
                file1.write("\n")  

# def cari digunakan untuk mencari elemen pada suatu file csv
# contoh : cari(readFile(user.csv), "id", "3", "username")
# artinya : pada file user.csv, ingin dicari username milik pengguna dengan id "3"
def cari(file, kategori, cari, hasil):
    kategoriFound = False
    while kategoriFound == False:
        for j in range(length(file[0])):
            if file[0][j] == kategori:
                x = j
                kategoriFound = True
    hasilFound = False
    while hasilFound == False:
        for k in range(length(file[0])):
            if file[0][k] == hasil:
                y = k
                hasilFound = True
    found = False
    for i in range(length(file)):
        if file[i][x] == cari:
            result = file[i][y]
            found = True
            return result
        elif file[i][x] != cari:
            pass

    if not found:    
        return "x"
    else:
        return result

# Mengganti suatu value
# file : matrix file tujuan, misal "readFile(user.csv)"
# kategori : kategori yang ingin diganti, misal "saldo"
# id : id, misal "GAME001", "1"
# newvalue : value baru
def changevalue(file, kategori, id, newvalue):
    kategoriFound = False
    while kategoriFound == False:
        for j in range(length(file[0])):
            if file[0][j] == kategori:
                x = j
                kategoriFound = True
    for i in range (length(file)):
        if file[i][0] == id:
            file[i][x] = newvalue

# Menambahkan data pada matrix file
# file : matrix file yang ingin ditambahkan, misal "readFile(user.csv)"
# stuff : data yang ingin ditambahkan dalam bentuk array
def appendMatrix(file, stuff):
    matrix = [0 for i in range (length(file)+1)]
    for j in range(length(matrix)-1):
        matrix[j] = file[j]
    matrix[length(matrix)-1] = stuff
    return matrix


def save(stuff):
    choice = str(input("Apakah perubahan ingin disimpan? (Y/N) : "))
    if choice == "Y":
        folder = str(input("Masukkan nama folder : "))
        if not os.path.exists(folder):
            os.mkdir(folder)
        writeFile(f"{folder}/game.csv", stuff[0], 6)
        writeFile(f"{folder}/kepemilikan.csv", stuff[1], 2)
        writeFile(f"{folder}/riwayat.csv", stuff[2], 5)
        writeFile(f"{folder}/user.csv", stuff[3], 6)
        
        print("Perubahan berhasil tersimpan.")
        return True
    elif choice == "N":
        print("Perubahan tidak tersimpan.")
        return False
        
