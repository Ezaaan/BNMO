from Function import length
def adagame (user_id_login, kepemilikan) :
# proses untuk mengecek terdapat game yang dibeli atau tidak
# I.S user id yang login
# F.S Boolean True/False
    # inisiasi
    i = 0
    found = False
    # pengecekan user id di data kepemilikan
    while (i < length(kepemilikan)) and (found == False) :
        if (kepemilikan[i][1] == (user_id_login)) :
            found = True
        else : 
            i += 1
    # jika valid, akan mereturn True 
    if found == True : 
        return True
    else : 
        return False
    
def arraykosong(array) :
# prosedur arraykosong berfungsi untuk menghitung jumlah element yang bukan kosong("")
    count = 0
    for i in range (length(array)) :
        if array[i] != "" : # jika element tidak sama dengan ("")
            count += 1
    return count

def arraybaru(array) :
# prosedur arraybaru berfungsi untuk menghapus element kosong("") di dalam array
    # deklarasi array baru yang kosong dengan panjang jumlah array yang bukan kosong ("") 
    arraybaru = ["" for i in range (arraykosong(array))]
    
    # proses memasukkan element array bukan kosong ke dalam arraybaru
    i = 0
    while i  < (length(arraybaru)) : 
        for j in range (length(array)) :
            if array[j] != "" :
                arraybaru[i] = array[j]
                i += 1
    return arraybaru

####################################################################################

# Program UTAMA 
# F09
def list_game(folder, user_id) :
# prosedur list_game adalah prosedur untuk melihat game yang dimiliki oleh user
    kepemilikan = folder[1]
    game = folder[0]
    # cek apakah user memiliki game atau tidak
    valid1 = adagame(user_id, kepemilikan)
    
    if valid1 == True : # user memiliki game
        print("Daftar Game : ")
        
        # Deklarasi Array Kosong yang akan diisi oleh game yang dimiliki
        game_user = ["" for i in range (length(kepemilikan))]
        for a in range (length(kepemilikan)) : 
            if kepemilikan[a][1] == (user_id) : # user cocok dengan data kepemilikan
                game_user[a] = kepemilikan[a][0] # game yang dimiliki oleh user dimasukkan kedalam array 
        
        # proses membersihkan element dengan nilai ("") agar array menjadi bersih
        game_user_b = arraybaru(game_user)
        
        # mencocokan game id yang ada di dalam array game_user_b dengan data di game.csv dan dikeluarkan ouputnya
        i = 0
        while (i < length(game_user_b)) :
            for j in range(length(game)) :
                if game_user_b[i] == game[j][0] :
                    print(str(i+1)+".", game[j][0], " | ", game[j][1], ' | ' , game[j][4], ' | ' , game[j][2], ' | ', game[j][3])
                    i += 1 
                    if i == length(game_user_b) : # jika i == panjang array game_user_b
                        break
                    else : # jika i < panjang array game_user_b
                        continue
                    
    elif valid1 == False : # user tidak memiliki game
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli")