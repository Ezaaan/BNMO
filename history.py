#length
def length(object):
    count = 0
    for i in object:
        count += 1
    return count

#append
def listAppend(listIn, elmt):
    n=0
    for i in listIn:   # Menghitung panjang list
        n+=1
    listOut=[0 for i in range(n+1)]  # Inisialisasi list baru
    for i in range(n+1):  # Mengisi list baru dengan elemen dari list lama + elemen tambahan baru 
        if i==n:
            listOut[i]=elmt
        else:
            listOut[i]=listIn[i]
    return listOut
# ditaro di file terpisah

#csv to list
def csvToList(fileName):
    with open(fileName, 'r') as f:
        lines=f.readlines()    # Membuka dan membaca file
        results = []           # Inisialisasi list akhir
        for line in lines:
            tempList=[]
            kata=str()
            if line!=lines[0]:  # Tidak memasukkan header csv file ke dalam list
                for alphabet in line:
                    if alphabet==';' or alphabet=='\n' or alphabet==',' : # Memisahkan antara ';' atau ',' atau new line
                        tempList=listAppend(tempList, kata)
                        kata=str()
                    else :
                        kata+=alphabet
                results=listAppend(results, tempList)
    return results

#convert game id
def convertGameIdtoInt(id): #GAME001 -> 001
    number = id[4] + id[5] + id[6]
    return str(int(number))

# split
def seperate(string, word):
    elements = 1
    for i in range(length(string)):
        if (string[i] == word):
            elements += 1

    list = ["" for i in range(elements)]
    listIndex = 0
    for i in range(length(string)):
        if (string[i] == word):
            listIndex += 1
        else:
            list[listIndex] += string[i]

#mencari game id yang dimiliki
def myGameId(kepemilikan,user_id):
    game_id = []
    for i in range(length(kepemilikan)):
        if user_id == kepemilikan[i][1]:
            game_id = listAppend(game_id, kepemilikan[i][0])
    return game_id

#is user
def isUser(data,user_id):
    user_id = str(user_id)
    flag = False
    for i in range(length(data)):
        if user_id == data[i][0]:
            if data[i][4] == "user":
                flag = True
    return flag

#membaca game.csv
def game():
    game = csvToList("game.csv")
    return game
                 
def limitCharacters(string, pjg): #Membatasi karakter sebanyak "pjg" (spasi dihitung satu huruf) huruf sesuai yang diminta
    finalString = ""
    if (length(string) > pjg):
        for i in range(pjg - 3):
            finalString += string[i]
        finalString += "..."
    else:
        nSpace = pjg - length(string)
        finalString = string
        for i in range(nSpace):
            finalString += " "
    return finalString

def history(folder,user_id):
    user_id = str(user_id)
    userdata = folder[3]
    riwayat = folder[2]
    if not isUser(userdata,user_id):
        return print("Hanya untuk user")
    else:
        history = [["ID", "Nama Game", "Harga", "Tahun Pembelian"]]        
        Nomor = 0
        for i in range(length(riwayat)):
            if user_id == riwayat[i][2]:
                history = listAppend(history, riwayat[i])
        if length(history) == 0:
            return print("Mohon maaf kamu belum memiliki game, lakukan pembelian game dengan perintah buyGame untuk menggunakan perintah ini.")
        else:
            print(f"   {limitCharacters(history[0][0],7)} | {limitCharacters(history[0][1],15)} | {limitCharacters(history[0][2],12)} | {limitCharacters(history[0][3],16)}")
            data = ''
            for j in range(1,length(history)):
                listTemp = history[j]
                gameId = listTemp[0]
                gameName = listTemp[1]
                gameHarga = listTemp[2]
                gameBeli = listTemp[3]
                print(f"{Nomor+1}. {limitCharacters(gameId,7)} | {limitCharacters(gameName,16)}| {limitCharacters(gameHarga,12)} | {limitCharacters(gameBeli,12)}")
                Nomor += 1
                listTemp = []
            return print(data)