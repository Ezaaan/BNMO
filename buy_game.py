import datetime 
from Function import length
from datetime import date
from csv_parser import save
today = date.today()
tahun = today.year
#
def isGameValid (game_id, game) :
# fungsi yang digunakan untuk mencari game
# I.S game id 
# F.S Boolean True/False
    # deklarasi
    i     = 0
    found = False
    # proses validasi
    while ((i < (length(game))) and (found == False)): 
        if (game[i][0] == (game_id)) : # jika game_id sama/ada di dalam data game.csv
            found = True
        else : 
            i = i+1
            
    # Jika valid, fungsi ini akan me return True        
    if (found == True) :
        return True
    else:
        return False

def isSaldoCukup (user_id_login, game_id, user, game) :
# fungsi yang digunakan untuk cek saldo cukup
# I.S id user yang login dan id game
# F.S Boolean True/False
    # Inisiasi
    saldouser = 0
    i     = 0
    found = False
    # pencarian saldo user
    while ((i < length(user)) and (found == False)):
        if (user[i][0] == (user_id_login)) :
            saldouser = int(user[i][5])
            found = True
        else : 
            i += 1
    # inisiasi 
    j = 0 
    found1 = False
    # pengecekan saldo user cukup atau tidak
    while ((i < length(game))) and (found1 == False) : 
        if (game[i][0] == game_id) and (int(saldouser) >= int(game[i][4])) :
            found1 = True
        else : 
            j += 1
    # jika cukup, akan mereturn true
    if found1 == True :
        return True
    elif found1 == False :
        return False

def isSudahBeli (user_id_login, game_id, kepemilikan) :
# fungsi yang mengecek apakah barang sudah dimiliki
# I.S id user yang login dan id barang
# F.S Boolean True/False 
    i     = 0
    found = False
    while ((i < length(kepemilikan)) and (found == False)):
        if (kepemilikan[i][0] == game_id) and (kepemilikan[i][1] == user_id_login):
            found = True
        else : 
            i += 1
    
    # jika valid, akan mereturn True
    if (found == True) :
        return True
    else:
        return False
    
def hargagame (game_id, game) :
# fungsi yang digunakan untuk mengeluarkan harga game
# I.S id user yang login dan id game
# F.S harga game
    # Proses Validasi
    i     = 0
    found = False
    while ((i < length(game)) and (found == False)):
        if (game[i][0] == (game_id)) :
            found = True
        else : 
            i += 1
    # Jika valid, fungsi ini akan return True        
    if (found == True) :
        return game[i][4]

     
def isStockValid (game_id, game) :
# fungsi yang digunakan untuk cek stock barang
# I.S id barang
# F.S Boolean True/False
    i = 0
    found = False
    # proses Validasi
    while (i < length(game) and (found == False)) : 
        if (game[i][0] == game_id) and (int(game[i][5]) > 0) :
            found = True
        else :
            i += 1
    # jika stok ada akan me return True
    if found == True :
        return True
    else : 
        return False

def ubahstock(game_id, game) :
# prosedur ubahstock berfungsi untuk mengurangi stock game setelah user membeli game tsb.
# I.S game id terdefinisi
# F.S jumlah stock game berkurang
    # deklarasi
    i = 0 
    found = False
    # proses validasi
    while (i < length(game)) and found == False:
        if game[i][0] == game_id :
            found = True
        else : 
            i += 1
            
    # akan mereturn stock game yang telah berkurang
    if found == True : 
        total = int(game[i][5]) - 1
        game[i][5] = str(total)
        return game

def ubahsaldo(user_id,game_id,game, user) :
# prosedur ubahsaldo berfungsi untuk mengubah saldo user setelah membeli game
# I.S user id dan game id terdefinisi
# F.S jumlah saldo user berkurang sebanyak harga game
    # deklarasi game id 
    i = 0 
    found = False
    # proses validasi game id
    while (i < length(game)) and found == False:
        if game[i][0] == game_id :
            found = True
        else : 
            i += 1
    # deklarasi user id 
    j = 0
    found1 = False
    # proses validasi user 
    while (j < length(user)) and found1 == False :
        if user[j][0] == user_id :
            found1 = True
        else : 
            j += 1
    # akan mereturn jumlah saldo user yang telah berkurang    
    if found == True and found1 == True: 
        total = int(user[j][5]) - int(game[i][4])
        user[j][5] = str(total)
        return user

def ubahriwayat (riwayat,arraybaru) :
# prosedur ini berfungsi untuk menambahkan array baru kedalam riwayat yang bersifat sementara
# hingga prosedur save dilakukan
    # Deklarasi array kosong dengan panjang array riwayat + 1
    x = ["" for i in range (length(riwayat)+1)]
    i = 0
    # proses memasukkan array riwayat ditambah array baru
    while i < length(x) :
        x[i] = [riwayat[i][0],riwayat[i][1],riwayat[i][2],riwayat[i][3],riwayat[i][4]]
        i += 1
        if i == length(riwayat) : # jika array x sampai element terakhir
            x[i] = arraybaru # ditambahkan array baru
            break
    return x

def ubahkepemilikan (kepemilikan,arraybaru) :
# prosedur ini berfungsi untuk menambahkan array baru kedalam kepemilikan yang bersifat sementara
# hingga prosedur save dilakukan
    # Deklarasi array kosong dengan panjang array kepemilikan + 1
    x = ["" for i in range (length(kepemilikan)+1)]
    i = 0
    # proses memasukkan array kepemilikan ditambah array baru
    while i < length(x) :
        x[i] = [kepemilikan[i][0],kepemilikan[i][1]]
        i += 1
        if i == length(kepemilikan) : # jika array x sampai element terakhir
            x[i] = arraybaru # ditambahkan array baru
            break
    return x

def Game_name(game_id, game) :
# fungsi untuk merubah game id menjadi nama game
# I.S game id tervalidasi
# F.S nama game
    i = 0
    found = False
    while ((i < length(game)) and (found == False)):
        if (game[i][0] == (game_id)) :
            found = True
        else : 
            i = i+1
    # dapat dipastikan bahwa game id valid jadi kondisi yang ditulis hanya True saja         
    if (found == True) :
        return game[i][1]

#####################################################################################################

# Program utama
# F08
def buy_game(folder, user_id) :
# prosedur buy game berfungsi untuk membeli game 
# I.S user id terdefinisi
# F.S file data diupdate
    riwayat = folder[2]
    kepemilikan = folder[1]
    game = folder[0]
    user = folder[3]
    # input game id yang akan dibeli
    game_id = input("Masukkan ID Game: ")
    
    # validasi
    valid1 = isGameValid (game_id, game) # cek game id valid atau tidak
    valid2 = isSudahBeli(user_id, game_id, kepemilikan) # cek game sudah dipunyai oleh user atau tidak
    valid3 = isSaldoCukup(user_id, game_id, user, game) # cek saldo user cukup atau tidak
    valid4 = isStockValid(game_id, game)  # cek stock game 
    
    if (valid1 == True) and (valid2 == False) and (valid3 == True) and (valid4 == True) : # jika terdapat kondisi seperti ini maka dapat dilaksanakan proses pembelian        
        # simpan ke dalam memori sementara (ntar klo dah ada save tinggal di replace file aja game.csv + user.csv nya)
        ubahstock(game_id, game) # ubah stock game di dalam memori sementara
        ubahsaldo(user_id, game_id, game, user) # ubah saldo user di dalama memori sementara
        
        # Proses pengisian data2 baru ke dalam list kosong (new_data_riwayat)
        new_data_riwayat = [game_id, Game_name(game_id, game), hargagame(game_id, game), user_id, tahun]
        
        # proses pengisian data2 baru ke dalam list kosong (new_data_kepemilikan)
        new_data_kepemilikan = [game_id, user_id]
        
        # menambahkan data baru ke dalam array sementara (ntar klo dah ada save tinggal di replace file aja riwayat.csv + kepemilikan.csv nya)
        ubahriwayat(riwayat,new_data_riwayat)
        ubahkepemilikan(kepemilikan,new_data_kepemilikan)
        
        # mencari nama game (untuk keperluan output)
        namagame = Game_name(game_id, game)
        
        # jika berhasil dibeli, maka program akan mengeluarkan seperti yang ada di bawah ini
        print("Game " + namagame + " berhasil dibeli!") 
        save(folder)
        
    elif valid1 == False : # jika game id tidak ada
        print ("Game tidak ditemukan")
    elif valid1 == True and valid2 == True : # jika game sudah pernah dibeli
        print("Anda sudah memiliki Game tersebut!")
    elif valid1 == True and valid2 == False and valid3 == False : # jika saldo tidak mencukupi
        print("Saldo anda tidak cukup untuk membeli Game tersebut!")
    elif valid1 == True and valid2 == False and valid3 == True and valid4 == False : # jika stok game habis
        print("Stok Game tersebut sedang habis!")
