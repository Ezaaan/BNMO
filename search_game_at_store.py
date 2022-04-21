from search_my_game import isInputValid
from Function import length

#####################################################################################################

# PROGRAM UTAMA 
# F11
def search_game_at_store(folder) :
# prosedur ini berfungsi untuk mencari game dengan kriteria tertentu di toko
    # inisiasi input 
    game = folder[0]
    game_id = input("Masukkan ID Game: ")
    nama_game = input("Masukkan Nama Game: ")
    harga_game = input("Masukkan Harga Game: ")
    kategori = input("Masukkan Kategori Game: ")
    tahun_rilis = input("Masukkan Tahun Rilis Game: ")
    print()
    # semua input valid/terdefinisi
    if (isInputValid(game_id) == True) and (isInputValid(nama_game) == True) and (isInputValid(harga_game) == True) and (isInputValid(kategori) == True) and (isInputValid(tahun_rilis) == True) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][0] == game_id and game[i][1] == nama_game and game[i][4] == harga_game and game[i][2] == kategori and game[i][3] == tahun_rilis : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")
            
    # input game_id tidak terdefinsi       
    elif (isInputValid(game_id) == False) and (isInputValid(nama_game) == True) and (isInputValid(harga_game) == True) and (isInputValid(kategori) == True) and (isInputValid(tahun_rilis) == True) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][1] == nama_game and game[i][4] == harga_game and game[i][2] == kategori and game[i][3] == tahun_rilis : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")
            
    # input nama_game tidak terdefinsi              
    elif (isInputValid(game_id) == True) and (isInputValid(nama_game) == False) and (isInputValid(harga_game) == True) and (isInputValid(kategori) == True) and (isInputValid(tahun_rilis) == True) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][0] == game_id and game[i][4] == harga_game and game[i][2] == kategori and game[i][3] == tahun_rilis : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")
            
    # input harga_game tidak terdefinsi
    elif (isInputValid(game_id) == True) and (isInputValid(nama_game) == True) and (isInputValid(harga_game) == False) and (isInputValid(kategori) == True) and (isInputValid(tahun_rilis) == True) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][0] == game_id and game[i][1] == nama_game and game[i][2] == kategori and game[i][3] == tahun_rilis : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")

    # input kategori tidak terdefinsi
    elif (isInputValid(game_id) == True) and (isInputValid(nama_game) == True) and (isInputValid(harga_game) == True) and (isInputValid(kategori) == False) and (isInputValid(tahun_rilis) == True) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][0] == game_id and game[i][1] == nama_game and game[i][4] == harga_game and game[i][3] == tahun_rilis : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")

    # input tahun_rilis tidak terdefinsi
    elif (isInputValid(game_id) == True) and (isInputValid(nama_game) == True) and (isInputValid(harga_game) == True) and (isInputValid(kategori) == True) and (isInputValid(tahun_rilis) == False) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][0] == game_id and game[i][1] == nama_game and game[i][4] == harga_game and game[i][2] == kategori : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria") 
            
    # input game_id dan nama_game tidak terdefinsi
    elif (isInputValid(game_id) == False) and (isInputValid(nama_game) == False) and (isInputValid(harga_game) == True) and (isInputValid(kategori) == True) and (isInputValid(tahun_rilis) == True) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][4] == harga_game and game[i][2] == kategori and game[i][3] == tahun_rilis : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")

    # input game_id dan harga_game tidak terdefinsi
    elif (isInputValid(game_id) == False) and (isInputValid(nama_game) == True) and (isInputValid(harga_game) == False) and (isInputValid(kategori) == True) and (isInputValid(tahun_rilis) == True) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][1] == nama_game and game[i][2] == kategori and game[i][3] == tahun_rilis : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")
    
    # input game_id dan kategori tidak terdefinsi                
    elif (isInputValid(game_id) == False) and (isInputValid(nama_game) == True) and (isInputValid(harga_game) == True) and (isInputValid(kategori) == False) and (isInputValid(tahun_rilis) == True) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][1] == nama_game and game[i][4] == harga_game and game[i][3] == tahun_rilis : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")
    
    # input game_id dan tahun_rilis tidak terdefinsi
    elif (isInputValid(game_id) == False) and (isInputValid(nama_game) == True) and (isInputValid(harga_game) == True) and (isInputValid(kategori) == True) and (isInputValid(tahun_rilis) == False) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][1] == nama_game and game[i][4] == harga_game and game[i][2] == kategori : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")
    
    # input nama_game dan harga_game tidak terdefinsi                
    elif (isInputValid(game_id) == True) and (isInputValid(nama_game) == False) and (isInputValid(harga_game) == False) and (isInputValid(kategori) == True) and (isInputValid(tahun_rilis) == True) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][0] == game_id and game[i][2] == kategori and game[i][3] == tahun_rilis : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")
    
    # input nama_game dan kategori tidak terdefinsi                 
    elif (isInputValid(game_id) == True) and (isInputValid(nama_game) == False) and (isInputValid(harga_game) == True) and (isInputValid(kategori) == False) and (isInputValid(tahun_rilis) == True) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][0] == game_id and game[i][4] == harga_game and game[i][3] == tahun_rilis : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria") 

    # input nama_game dan tahun_rilis tidak terdefinsi  
    elif (isInputValid(game_id) == True) and (isInputValid(nama_game) == False) and (isInputValid(harga_game) == True) and (isInputValid(kategori) == True) and (isInputValid(tahun_rilis) == False) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][0] == game_id and game[i][4] == harga_game and game[i][2] == kategori : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria") 

    # input harga_game dan kategori tidak terdefinsi  
    elif (isInputValid(game_id) == True) and (isInputValid(nama_game) == True) and (isInputValid(harga_game) == False) and (isInputValid(kategori) == False) and (isInputValid(tahun_rilis) == True) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][0] == game_id and game[i][1] == nama_game and game[i][3] == tahun_rilis : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")   

    # input harga_game dan tahun_rilis tidak terdefinsi 
    elif (isInputValid(game_id) == True) and (isInputValid(nama_game) == True) and (isInputValid(harga_game) == False) and (isInputValid(kategori) == True) and (isInputValid(tahun_rilis) == False) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][0] == game_id and game[i][1] == nama_game and game[i][2] == kategori  : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")

    # input kategori dan tahun_rilis tidak terdefinsi 
    elif (isInputValid(game_id) == True) and (isInputValid(nama_game) == True) and (isInputValid(harga_game) == True) and (isInputValid(kategori) == False) and (isInputValid(tahun_rilis) == False) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][0] == game_id and game[i][1] == nama_game and game[i][4] == harga_game  : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")

    # hanya input kategori dan tahun_rilis terdefinsi 
    elif (isInputValid(game_id) == False) and (isInputValid(nama_game) == False) and (isInputValid(harga_game) == False) and (isInputValid(kategori) == True) and (isInputValid(tahun_rilis) == True) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][2] == kategori and game[i][3] == tahun_rilis : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")

    # hanya input harga_game dan tahun_rilis terdefinsi 
    elif (isInputValid(game_id) == False) and (isInputValid(nama_game) == False) and (isInputValid(harga_game) == True) and (isInputValid(kategori) == False) and (isInputValid(tahun_rilis) == True) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][4] == harga_game and game[i][3] == tahun_rilis : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")

    # hanya input harga_game dan kategori terdefinsi 
    elif (isInputValid(game_id) == False) and (isInputValid(nama_game) == False) and (isInputValid(harga_game) == True) and (isInputValid(kategori) == True) and (isInputValid(tahun_rilis) == False) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][4] == harga_game and game[i][2] == kategori : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")

    # hanya input nama_game dan tahun_rilis terdefinsi
    elif (isInputValid(game_id) == False) and (isInputValid(nama_game) == True) and (isInputValid(harga_game) == False) and (isInputValid(kategori) == False) and (isInputValid(tahun_rilis) == True) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][1] == nama_game and game[i][3] == tahun_rilis : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")

    # hanya input nama_game dan kategori terdefinsi
    elif (isInputValid(game_id) == False) and (isInputValid(nama_game) == True) and (isInputValid(harga_game) == False) and (isInputValid(kategori) == True) and (isInputValid(tahun_rilis) == False) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][1] == nama_game and game[i][2] == kategori : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")

    # hanya input nama_game dan harga_game terdefinsi
    elif (isInputValid(game_id) == False) and (isInputValid(nama_game) == True) and (isInputValid(harga_game) == True) and (isInputValid(kategori) == False) and (isInputValid(tahun_rilis) == False) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][1] == nama_game and game[i][4] == harga_game : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")
    
    # hanya input game_id dan tahun_rilis terdefinsi
    elif (isInputValid(game_id) == True) and (isInputValid(nama_game) == False) and (isInputValid(harga_game) == False) and (isInputValid(kategori) == False) and (isInputValid(tahun_rilis) == True) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][0] == game_id and game[i][3] == tahun_rilis : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")

    # hanya input game_id dan kategori terdefinsi
    elif (isInputValid(game_id) == True) and (isInputValid(nama_game) == False) and (isInputValid(harga_game) == False) and (isInputValid(kategori) == True) and (isInputValid(tahun_rilis) == False) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][0] == game_id and game[i][2] == kategori : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")

    # hanya input game_id dan harga_game terdefinsi
    elif (isInputValid(game_id) == True) and (isInputValid(nama_game) == False) and (isInputValid(harga_game) == True) and (isInputValid(kategori) == False) and (isInputValid(tahun_rilis) == False) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][0] == game_id and game[i][4] == harga_game  : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0  : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")

    # hanya input game_id dan nama_game terdefinsi
    elif (isInputValid(game_id) == True) and (isInputValid(nama_game) == True) and (isInputValid(harga_game) == False) and (isInputValid(kategori) == False) and (isInputValid(tahun_rilis) == False) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][0] == game_id and game[i][1] == nama_game : 
                while j < length(game) :
                    print(str(j+1)+".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0 : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")

    # hanya input tahun_rilis yang terdefinsi         
    elif (isInputValid(game_id) == False) and (isInputValid(nama_game) == False) and (isInputValid(harga_game) == False) and (isInputValid(kategori) == False) and (isInputValid(tahun_rilis) == True) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][3] == tahun_rilis : 
                while j < length(game) :
                    print(str(j+1) +".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3])
                    j += 1
                    break
        if j == 0 : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")

    # hanya input nama_game yang terdefinsi          
    elif (isInputValid(game_id) == False) and (isInputValid(nama_game) == True) and (isInputValid(harga_game) == False) and (isInputValid(kategori) == False) and (isInputValid(tahun_rilis) == False) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][1] == nama_game :
                while j < length(game) :
                    print(str(j+1) +".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3])
                    j += 1
                    break
        if j == 0 : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")

    # hanya input harga_game yang terdefinsi         
    elif (isInputValid(game_id) == False) and (isInputValid(nama_game) == False) and (isInputValid(harga_game) == True) and (isInputValid(kategori) == False) and (isInputValid(tahun_rilis) == False) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][4] == harga_game :
                while j < length(game) :
                    print(str(j+1) +".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3])
                    j += 1
                    break
        if j == 0 : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")
    
    # hanya input kategori yang terdefinsi         
    elif (isInputValid(game_id) == False) and (isInputValid(nama_game) == False) and (isInputValid(harga_game) == False) and (isInputValid(kategori) == True) and (isInputValid(tahun_rilis) == False) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][2] == kategori : 
                while j < length(game) :
                    print(str(j+1) +".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3])
                    j += 1
                    break
        if j == 0 : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")
     
    # hanya input game_id yang terdefinsi        
    elif (isInputValid(game_id) == True) and (isInputValid(nama_game) == False) and (isInputValid(harga_game) == False) and (isInputValid(kategori) == False) and (isInputValid(tahun_rilis) == False) :
        print("Daftar game pada toko yang memenuhi kriteria:")
        j = 0
        for i in range (length(game)) : # proses pengecekan dan output
            if game[i][0] == game_id  : 
                while j < length(game) :
                    print(str(j+1) +".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                    j += 1
                    break
        if j == 0 : # jika tidak ada input yang cocok
            print("Tidak ada game pada toko yang memenuhi kriteria")
            
    else : # semua input tidak valid/tidak terdefinisi
        print("Daftar game pada toko yang memenuhi kriteria:")
        i = 1
        j = 0
        while i < (length(game)) : # proses pengecekan dan output
            while j < length(game) :
                print(str(j+1) +".",game[i][0] , "|", game[i][1], "|", game[i][4], "|" , game[i][2] , "|", game[i][3], "|", game[i][5])
                j += 1
                i += 1
                break
# perbaiki dekomposisi