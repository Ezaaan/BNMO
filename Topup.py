from Function import length

def Topup(folder):
    userData = folder[3]
    usernameInput = str(input('Masukkan username: '))
    saldoInput = int(input("Masukkan saldo: "))
    while not isUsernameExist(userData, usernameInput) or not isSaldoValid(saldoInput):
        if (not isUsernameExist(userData, usernameInput)):
            print(f"Username “{usernameInput}” tidak ditemukan.")
            usernameInput = str(input('Masukkan ulang username: '))
        elif (not isSaldoValid(saldoInput)):
            print('Masukan saldo tidak valid.')

    id = getTopupId(userData, usernameInput)
    userData[id][5] = str(
        int(userData[id][5]) + saldoInput)

    return userData


def isUsernameExist(folder, usernameInput):
    userData = folder[3]
    usernameExist = False
    for i in range(length(userData) - 1):
        if (userData[i + 1][1] == usernameInput):
            usernameExist = True
            break
    return usernameExist


def getTopupId(folder, usernameInput):
    userData = folder[3]
    for i in range(length(userData) - 1):
        if (userData[i + 1][1] == usernameInput):
            id = i + 1
        else:
            pass
    return id


def isSaldoValid(saldoInput):
    if (saldoInput > 0):
        return True
    else:
        return False
