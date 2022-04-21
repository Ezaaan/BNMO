
def addSaldo():
    data_user = [['25001yaaya', 'Daffa Muhammad Rasyid', 'rsydaf', 'lalala', 'user', 0],
                ['25002naans', 'Fauzan Nurul Huda', 'sansanee', 'sansan', 'user', 0],
                ['25003ieaik', 'Keira Gassani', 'keigassani', 'keikei', 'user', 0]
                ['25004masmn', 'Rahman Satya', 'rhmnsty', 'atangg', 'user', 0],
                ['25005daada', 'Saddam Annais', 'saddam', 'annais', 'user', 0]]
    li = 0
    sumsaldo = 0
    stop = False

    print('\n************************************************************\n')
    print("Untuk melakukan top up, Silahkan masukkan Username dan saldo Top Up")
    print("Masukan username Anda:")
    username = str(input())

    while not stop and li < len(data_user):
        if username == data_user[li][2]:
            stop = True
        elif username != data_user[li][2]:
            stop = False
        li += 1

    if stop:
        print("Masukkan saldo Top Up Anda:")
        saldo = int(input())
        if saldo > 0:
            sumsaldo = data_user[li-1][5] + saldo
            print("Selamat, top up yang anda lakukan berhasil. Saldo", username, "bertambah menjadi", sumsaldo)
            return True
        elif saldo < 0:
            if data_user[li-1][5] >= (-1 * saldo):
                sumsaldo = data_user[li-1][5] + saldo
                print("Saldo", username, "berkurang menjadi", sumsaldo)

            else:
                print("***Masukan saldo tidak valid\n")

        else:
            print("***Masukan saldo tidak valid***")


    elif not stop:
        print("***Username yang dimasukkan salah atau akun belum melakukan registrasi***")

    
    print('\n************************************************************\n')
