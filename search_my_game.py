from list_game import adagame, arraybaru, arraykosong, list_game
from Function import length

def isInputValid (thing) :
# prosedur isInputValid berfungsi untuk mengecek apakah input kosong/tidak
# menghasilkan True jika ada input dan False jika tidak ada input
# I.S input Sembarang
# F.S Boolean True
    Cek = False
    if thing != "" : 
        Cek = True
    else :
        Cek = False
    return Cek 

def gamecocok(user_id,game_id, kepemilikan) :
# proses untuk mencari apakah suatu game dipunyai oleh seorang user
# I.S user id dan game id terdefenisi
# F.S Boolean True/False
    i = 0
    found = False
    while (i < length(kepemilikan)) and (found == False) :
        if (kepemilikan[i][1] == (user_id)) and (kepemilikan[i][0]) ==(game_id) :
            found = True
        else : 
            i = i + 1
    if found == True : 
        return True
    else : 
        return False

def tahun_game_cocok(game_id,tahun, game):
# prosedur tahun_game_cocok berfungsi untuk mencocokan game id dengan tahun
# I.S game id dan tahun terdefinsi
# F.S Boolean True/False
    i = 0
    found = False
    while (i < length(game)) and (found == False) :
        if (game[i][3] == (tahun)) and (game[i][0]) ==(game_id) :
            found = True
        else : 
            i = i + 1
    if found == True : 
        return True
    else : 
        return False

#####################################################################################################

# PROGRAM UTAMA 
# F10
def search_my_game(folder, user_id) :
# prosedur search_my_game berfungsi untuk melihat game yang dimiliki oleh user dengan input game id 
# dan tahun rilis game (salah satu boleh kosong)
    game = folder[0]
    kepemilikan = folder[1]
    # input game id dan tahun rilis
    game_id = input("Masukkan ID Game: ")
    tahun_rilis = input("Masukkan Tahun Rilis Game: ")
    print()
    # pengecekan input ada/tidak
    game_id_ada = isInputValid(game_id)
    tahun_rilis_ada = isInputValid(tahun_rilis)

    # jika game id dan tahun rilis terdefenisi
    if (game_id_ada == True) and (tahun_rilis_ada == True) : 
        # cek user memiliki game atau tidak
        valid1 = adagame(user_id, kepemilikan)
        
        # user tidak memiliki game
        if valid1 == False :
            print()
        elif valid1 == True : # user memilki game
            print("Daftar game pada inventory yang memenuhi kriteria:")
            
            # cek input game id dimiliki oleh user atau tidak
            valid2 = gamecocok(user_id,game_id, kepemilikan)
            valid3 = tahun_game_cocok(game_id,tahun_rilis, game)
            
            # game dimiliki user dan tahun rilis cocok
            if (valid2 == True) and (valid3 == True):
                j = 0
                while j < 1 : 
                    for i in range (length(game)) :
                        if game[i][0] == (game_id) and game[i][3] == (tahun_rilis) :
                            print(str(j+1)+".", game[i][0], " | ", game[i][1], ' | ' , game[i][4], ' | ' , game[i][2], ' | ', game[i][3])  
                            j += 1
            else : # game tidak dimiliki user
                print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
                
    # hanya tahun rilis yang terdefinisi                 
    elif ((game_id_ada) == (False)) and ((tahun_rilis_ada) == True) : 
        # cek user memiliki game atau tidak
        valid1 = adagame(user_id)
        
        # user tidak memiliki game 
        if valid1 == False :
            print()
        elif valid1 == True : # user memiliki game 
            # deklarasi array kosong dengan panjang data game.csv
            game_tahun = ["" for i in range (length(game))]
            
            # proses memasuki game yang dengan tahun rilis yang diinginkan ke dalam array game_user
            a = 0
            while (a < length(game)) :
                if game[a][3] == (tahun_rilis) :
                    game_tahun[a] = game[a][0]
                    a += 1
                else :
                    a += 1
                    
            # membersihkan array game_tahun dari element kosong ("")
            game_tahun_baru = arraybaru(game_tahun)
            
            # Deklarasi array kosong dengan panjang array game_user
            game_user = ["" for i in range(length(game_tahun_baru))]
            
            # proses memasuki game yang dimiliki oleh user dari array game_tahun ke dalam array game_user
            for j in range (length(game_tahun_baru)) :
                for i in range (length(kepemilikan)) :
                    if game_tahun_baru[j] == kepemilikan[i][0] and kepemilikan[i][1] == user_id :
                        game_user[j] = game_tahun_baru[j]
                        
            # membersihkan array game_user dari element kosong ("")
            game_user_baru = arraybaru(game_user)
            
            # cek jika array game_user_baru terdapat element / bukan array kosong 
            if arraykosong(game_user_baru) != length(game_user_baru) : # array game_user_baru terdapat element
                # proses pencocokan data game id dalam game_user_baru dengan data game.csv dan dilakukan output data nya
                print("Daftar game pada inventory yang memenuhi kriteria:")
                b = 0
                while (b < length(game_user_baru)) :
                    for i in range (length(game)) :
                        if game_user_baru[b] == game[i][0] :
                            print(str(b+1)+".", game[i][0], " | ", game[i][1], ' | ' , game[i][4], ' | ' , game[i][2], ' | ', game[i][3])  
                            b += 1
                            if b == length(game_user_baru) :
                                break
            else : # array game_user_baru kosong
                print()
                        
    # hanya game id yang terdefinisi                                                 
    elif ((game_id_ada) == (True)) and (tahun_rilis_ada) == False :
        # pengecekan user memiliki game atau tidak
        valid1 = adagame(user_id)
        if valid1 == False : # user tidak memiliki game
            print()
        elif valid1 == True : # user memiliki game
            print("Daftar game pada inventory yang memenuhi kriteria:")
            
            # pengecekan user memiliki game yang dicari atau tidak
            valid2 = gamecocok(user_id,game_id, kepemilikan)
            if valid2 == True : # jika user memiliki game yang dicari
                # proses pengecekan data id dengan data game.csv dan dilakukan output data nya 
                b = 0
                while (b < 1) :
                    for i in range (length(game)) :
                        if game_id == game[i][0] :
                            print(str(b+1)+".", game[i][0], " | ", game[i][1], ' | ' , game[i][4], ' | ' , game[i][2], ' | ', game[i][3])  
                            b += 1
                            if b == 1 :
                                break
            else : # user tidak memiliki game yang dicari
                print()
    else : # game id dan tahun rilis tidak terdefinisi
        print(list_game())