<<<<<<< HEAD
from csv_parser import readFile, writeFile
=======
from csv_parser import save
>>>>>>> eea73a8dbb619481a7d9cc484f337aaadc650ec8
from Function import length

#Algoritma Utama
def ubah_game(folder):
    store_file=folder[0]
    count=length(store_file)

    #Meminta ID game yang akan diubah
    #Akan terus mengulang jika ID game tidak ditemukan
    while True:
        game_search=input("Masukkan ID game: ")
        valid=False
        i=0
        while i<count and valid==False:
            Temp=store_file[i]
            if (Temp[0]==game_search):
                valid=True
            i+=1
        if valid:
            break
        print("Game dengan ID '", game_search, "' tidak ditemukan! Silahkan coba lagi")
    game_Number=i-1 #Posisi/No. ID game
    print()

    #Meminta data baru untuk game
    #Akan terus mengulang jika input yang dimasukkan tidak valid atau sesuai
    valid=False
    while valid==False:
        try:
            flag=True

            ##Memasukkan input data baru ke dalam temporary variable
            print("Silahkan masukkan data game!")
            game_Name=input("Masukkan nama game: ")
            game_Genre=input("Masukkan kategori game: ")
            Temp_game_Release=input("Masukkan tahun rilis: ")
            Temp_game_Price=input("Masukkan harga: ")
            print()

            #Jika data tahun dan harga tidak kosong (akan diganti), 
            #perlu dicek apakah tipe data yang dimasukkan sesuai atau tidak dan valid atau tidak
            ##Jika tidak (ValueError), akan pindah ke except
            if Temp_game_Release!='' or Temp_game_Price!='':
                game_release=int(Temp_game_Release)
                game_Price=int(Temp_game_Price)

                #Mengecek apakah data yang data yang dimasukkan valid atau tidak, jika tidak maka akan mengulang
                if game_release <= 0 or game_Price < 0:
                    print("Mohon masukkan data yang valid!\n")
                    flag=False
            
            #Jika semua data valid, maka akan dimasukkan data baru (Jika kosong maka tidak akan diganti)
            #Jika ada yang tidak valid maka akan diulang
            if flag:
                if game_Name!='':
                    store_file[game_Number][1]=game_Name
                if game_Genre!='':
                    store_file[game_Number][2]=game_Genre
                if Temp_game_Release!='':
                    store_file[game_Number][3]=str(game_release)
                if Temp_game_Price!='':
                    store_file[game_Number][4]=str(game_Price)
                save(folder)
                valid=True

        #Menampilkan pesan error jika terjadi kesalahan tipe data
        except ValueError:
            print("Mohon masukkan data yang valid!\n")
"""
#Menggantikan SELURUH isi file csv dengan yang baru (Utk sekarang diimplementasikan langsung ke dalam csv karena blm ada save() dan load())
<<<<<<< HEAD
writeFile('game.csv', store_file, 6)
=======
replaceFile('game.csv', store_file, 6)
"""
>>>>>>> eea73a8dbb619481a7d9cc484f337aaadc650ec8
