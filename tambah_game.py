from csv_parser import save
from Function import length

#Algoritma Utama
def tambah_game(folder):
    #Load csv file 
    File1 = folder[0]

    #Menentukan jumlah elemen (jumlah game) yang ada pada file
    count=length(File1)

    #Meminta input data game
    #Akan terus mengulang jika input yang dimasukkan kosong atau tidak sesuai
    valid=False
    while valid==False:
        try:
            #Memasukkan input ke dalam temporary variable
            print("Silahkan masukkan data game!")
            game_Name=input("Masukkan nama game: ")
            game_Genre=input("Masukkan kategori game: ")
            Temp_game_Release=input("Masukkan tahun rilis: ")
            Temp_game_Price=input("Masukkan harga: ")
            Temp_game_Stock=input("Masukkan stok awal: ")
            print()

            #Mengubah beberapa data menjadi int agar mengetahui apakah tipe data yang diinput sesuai
            #Jika tidak (ValueError), akan pindah ke except
            game_release=int(Temp_game_Release)
            game_Price=int(Temp_game_Price)
            game_Stock=int(Temp_game_Stock)

            #Menentukan apakah input yang dimasukkan kosong atau tidak dan jika data yang dimasukkan valid atau tidak
            if game_Name=='' or game_Genre=='' or Temp_game_Release=='' or Temp_game_Price=='' or Temp_game_Stock=='':
                print("Mohon lengkapi semua data!\n")
            elif game_release <= 0 or game_Price < 0 or game_Stock < 0:
                print("Mohon masukkan data yang valid!\n")
            else:
                valid=True

        #Mengeluarkan pesan error jika terjadi pemasukkan tipe data yang tidak sesuai (str pada int)
        except ValueError:
            print("Mohon masukkan data yang valid!\n")

    #Menentukan ID dari game
    if count < 9:
        game_id="GAME00"+ str(count+1)
    elif count < 99:
        game_id="GAME0"+ str(count+1)
    else:
        game_id="GAME"+str(count+1)

    #Memasukkan seluruh data baru yang diinput ke dalam suatu variabel
    new_Data=[game_id, game_Name, game_Genre, str(game_release), str(game_Price), str(game_Stock)]

    #Menampilkan pesan keberhasilan dalam penambahan game
    print("Selamat! Berhasil menambahkan '", game_Name, "'")
    save(folder)
    
"""
#Menambahkan variabel data baru game ke dalam csv file (Utk sekarang diimplementasikan langsung ke dalam csv karena blm ada save() dan load())
appendFile("game.csv", new_Data)
"""