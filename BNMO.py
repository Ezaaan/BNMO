import argparse
import UI
import os
from Commands import register,login
from csv_parser import readFile, save, cari
from Function import length
from ubah_stok import ubah_stok
from tambah_game import tambah_game
from ubah_game import ubah_game
from list_game_toko import list_game_toko
from search_game_at_store import search_game_at_store
from search_my_game import search_my_game
from list_game import list_game
from buy_game import buy_game
from exit import Exit, isExitConfirmed
from help import help
from Topup import Topup
from history import history

# start the program : python BNMO.py csvfolder

def admin(folder,id):
    UI.adminmenu(folder,id)
    choice = str(input("Masukkan perintah : "))
    if choice == "tambah_game":
        tambah_game(folder)
        admin(folder)
    elif choice == "ubah_stok":
        ubah_stok(folder)
        admin(folder)
    elif choice == "ubah_game":
        ubah_game(folder)
        admin(folder)
    elif choice == "list_game_toko":
        list_game_toko(folder)
        admin(folder)
    elif choice == "search_game_at_store":
        search_game_at_store(folder)
        admin(folder)
    elif choice == "help":
        help()
        admin(folder)
    elif choice == "save":
        save(folder)
    elif choice == "exit":
        isExitConfirmed()
        if isExitConfirmed:
            Exit()
        else:
            Exit()
    elif choice == "topup":
        Topup(folder)
        admin(folder)
    else:
        print("Perintah tak diketahui. Hanya bisa memasukkan perintah yang tertera.")
        admin(folder)

def user(folder,id):
    UI.usermenu(folder,id)
    choice = str(input("Masukkan perintah : "))
    if choice == "buy_game":
        buy_game(folder,id)
        user(folder,id)
    elif choice == "list_game":
        list_game(folder,id)
        user(folder,id)
    elif choice == "search_my_game":
        search_my_game(folder,id)
        user(folder,id)
    elif choice == "list_game_toko":
        list_game_toko(folder)
        user(folder,id)
    elif choice == "search_game_at_store":
        search_game_at_store(folder)
        user(folder,id)
    elif choice == "help":
        help()
        user(folder,id)
    elif choice == "save":
        save(folder)
        user(folder,id)
    elif choice == "exit":
        isExitConfirmed()
        if isExitConfirmed:
            Exit()
        else:
            Exit()
    elif choice == "riwayat":
        history(folder,id)
        user(folder,id)
    else:
        print("Perintah tak diketahui. Hanya bisa memasukkan perintah yang tertera.")
        user(folder,id)


def main(matrix):
    print("Selamat datang di BNMO!")
    UI.startmenu()
    choice = str(input("Masukkan perintah : "))
    if choice == "register":
        register(matrix)
        main(matrix)
    elif choice == "log in":
        id = login(matrix)
        role = cari(matrix[3], "id",str(id), "role")
        if role == "user":
            user(matrix, id)
        elif role == "admin":
            admin(matrix, id)
    elif choice == "exit":
        isExitConfirmed()
        if isExitConfirmed:
            Exit()
        else:
            Exit()
    
loaded = False
parser = argparse.ArgumentParser()
parser.add_argument('foldername', type=str)
args = parser.parse_args()
for (root,dirs,files) in os.walk(args.foldername, topdown=True):
    matrix = [0 for j in range (length(files))]
    for i in range (length(files)):
        matrix[i] = readFile(f"{args.foldername}/{files[i]}")
    loaded = True

if loaded :
    main(matrix)
else :
    print(f"Folder '{args.foldername}' tidak ditemukan")


# harus ada validasi
