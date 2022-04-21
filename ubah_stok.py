from csv_parser import save
from Function import length

#ALgoritma Utama
def ubah_stok(folder):
    #Inisialisasi
    store_files= folder[0]
    count=length(store_files)

    #Meminta ID game yang akan diubah
    #Akan terus mengulang jika ID game tidak ditemukan
    while True:
        game_search=input("Masukkan ID game: ")
        i=0
        valid=False
        while i < count and valid==False:
            if store_files[i][0]==game_search:
                valid=True
            else:
                i+=1
        
        if valid:
            break
        print("Tidak ada game dengan ID tersebut!\n")
    game_ID=i

    #Meminta data baru untuk game
    #Akan terus mengulang jika input yang dimasukkan tidak valid atau sesuai
    while True:
        try:
            stock_change=input("Masukkan jumlah: ")
            
            #Menentukan apakah jumlah ditambah atau dikurang
            if int(stock_change)>=0:
                change="ditambah"
            else:
                change="dikurangi"

            #Menentukan apakah jumlah stok setelah diubah akan valid atau tidak
            if ((int(store_files[game_ID][5])) + int(stock_change))<0:
                print("Stok game '", store_files[game_ID][1], "' gagal dikurangi karena stok kurang. Stok sekarang: ", store_files[game_ID][5], " (<", -1*int(stock_change), ")\n")
            else:
                current_stock= int(store_files[game_ID][5]) + int(stock_change)
                store_files[game_ID][5]=str(current_stock)
                print("Stok game '", store_files[game_ID][1], "' berhasil ", change + ". Stok sekarang: ", store_files[game_ID][5])
                save(folder)
                break
        
        #Menampilkan pesan jika tipe data yang diinput tidak sesuai
        except ValueError:
            print("Mohon masukkan jumlah yang valid!\n")
            
"""
    #Menggantikan SELURUH isi file csv dengan yang baru (Utk sekarang diimplementasikan langsung ke dalam csv karena blm ada save() dan load())
    replaceFile("game.csv", store_files, 6)    
"""
