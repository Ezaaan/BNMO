from csv_parser import readFile, writeFile
from Function import length

#Kumpulan Fungsi dan Prosedur 

#Memutarbalikkan urutan list
def reversed(X, count):
    Y=[[0 for i in range (2)] for i in range (count)]
    for i in range (count):
        Y[i]=X[count-(i+1)]
    return Y

#Mengurutkan elemen pada list
def sort_list(X,count):
    for i in range (count-1):
        if int(X[i][1]) > int(X[i+1][1]):
            X+=[X[i]]
            temp=X[0:i+1]
            if length(temp)==1:
                X=X[i+1:]
            else:
                X=temp[:length(temp)-1] + X[i+1:]
            X=sort_list(X, count)
            break
    X=sort_ID(X, count)
    return X

#Menampilkan elemen berdasarkan urutan ID
def asc_ID(X, count):
    for i in range (count):
        print(str(i+1)+".", end=" ")
        for j in range (6):
            if j!=5:
                print(X[i][j], "|", end=" ")
            else:
                print(X[i][j])

#Mengurutkan elemen list berdasarkan ID (Pengurutan kedua)
def sort_ID(X, count):
    for i in range (count-1):    
        if int(X[i][1])==int(X[i+1][1]) and (X[i][0]>X[i+1][0]):
            temp1=X[i]
            temp2=X[i+1]
            X[i]=temp2
            X[i+1]=temp1
            X=sort_ID(X, count)
            break
    return X

#Menampilkan list game berdasarkan skema sorting tertentu
def show_list(X, Y, store_files, count):
    if Y=="asc":
        sorted=sort_list(X, count)
    else:
        sorted=sort_ID(reversed(sort_list(X, count), count), count)
    for i in range (count):
        print(str(i+1)+".", end=" ")
        for j in range(6):
            if j!=5:
                print(store_files[(sorted[i][0]-1)][j], "|", end=" ")
            else:
                print(store_files[(sorted[i][0])-1][j])

##################################################################################

#Algoritma Utama
def list_game_toko(folder):
#Load csv file
    store_files=folder[0]
    count=0
    for i in store_files:
        count+=1

    #Membuat dan mengisi matriks temporary berisi No. ID dan data tahun atau harga
    thn=[[0 for i in range (2)] for i in range (count)]
    harga=[[0 for i in range (2)] for i in range (count)]
    for i in range (count):
            thn[i][0]=i+1
            harga[i][0]=i+1
            thn[i][1]=store_files[i][3]
            harga[i][1]=store_files[i][4]

    #Menentukan pilihan skema sorting yang diinput
    sort_type=input("Skema sorting: ")
    print()
    print("ID | Name | Kategori | Tahun | Stok")
    if sort_type=="":
        asc_ID(store_files, count)
    elif sort_type.lower()=="tahun+":
        show_list(thn, "asc", store_files, count)
    elif sort_type.lower()=="tahun-":
        show_list(thn, "des", store_files, count)
    elif sort_type.lower()=="harga+":
        show_list(harga, "asc", store_files, count)
    elif sort_type.lower()=="harga-":
        show_list(harga, "des", store_files, count)
    else:
        print("Skema sorting tidak valid!")

# pakai limitcharacter di history