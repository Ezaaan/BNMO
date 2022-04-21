from csv_parser import cari

def startmenu():
    print("Commands : \n    register\n    log in\n    exit")

def usermenu(folder,id):
    nama = cari(folder[3], "id", id, "nama")
    print("  \n==================================================================")
    print(f"Halo, {nama}!\n")
    print(" __    __    ___  _        __   ___   ___ ___    ___      ______   ___       ____   ____   ___ ___   ___   __ \n|  |__|  |  /  _]| |      /  ] /   \ |   |   |  /  _]    |      | /   \     |    \ |    \ |   |   | /   \ |  |\n|  |  |  | /  [_ | |     /  / |     || _   _ | /  [_     |      ||     |    |  o  )|  _  || _   _ ||     ||  |\n|  |  |  ||    _]| |___ /  /  |  O  ||  \_/  ||    _]    |_|  |_||  O  |    |     ||  |  ||  \_/  ||  O  ||__|\n|  `  '  ||   [_ |     /   \_ |     ||   |   ||   [_       |  |  |     |    |  O  ||  |  ||   |   ||     | __ \n \      / |     ||     \     ||     ||   |   ||     |      |  |  |     |    |     ||  |  ||   |   ||     ||  |\n  \_/\_/  |_____||_____|\____| \___/ |___|___||_____|      |__|   \___/     |_____||__|__||___|___| \___/ |__|\n                                                                                                              ")
    print("Commands : \n     buy_game : membeli game baru\n     list_game : melihat game yang dimiliki\n     search_my_game : mencari game yang dimiliki")
    print("     list_game_toko : melihat game di toko\n     search_game_at_store : mencari game di toko\n     riwayat : lihat riwayat pembelian\n     help : bantuan")
    print("     save : simpan data\n     exit : keluar BNMO")

def adminmenu(folder,id):
    nama = cari(folder[3], "id", id, "nama")
    print("  \n==================================================================")
    print(f"Halo, {nama}!\n")
    print(" __    __    ___  _        __   ___   ___ ___    ___      ______   ___       ____   ____   ___ ___   ___   __ \n|  |__|  |  /  _]| |      /  ] /   \ |   |   |  /  _]    |      | /   \     |    \ |    \ |   |   | /   \ |  |\n|  |  |  | /  [_ | |     /  / |     || _   _ | /  [_     |      ||     |    |  o  )|  _  || _   _ ||     ||  |\n|  |  |  ||    _]| |___ /  /  |  O  ||  \_/  ||    _]    |_|  |_||  O  |    |     ||  |  ||  \_/  ||  O  ||__|\n|  `  '  ||   [_ |     /   \_ |     ||   |   ||   [_       |  |  |     |    |  O  ||  |  ||   |   ||     | __ \n \      / |     ||     \     ||     ||   |   ||     |      |  |  |     |    |     ||  |  ||   |   ||     ||  |\n  \_/\_/  |_____||_____|\____| \___/ |___|___||_____|      |__|   \___/     |_____||__|__||___|___| \___/ |__|\n                                                                                                              ")
    print("Commands : \n     tambah_game : tambah game baru\n     ubah_game : mengubah detil game\n     ubah_stok : mengubah stok game")
    print("     list_game_toko : melihat game di toko\n     search_game_at_store : mencari game di toko\n     top_up : top up saldo user\n     help : bantuan")
    print("     save : simpan data\n     exit : keluar BNMO")
