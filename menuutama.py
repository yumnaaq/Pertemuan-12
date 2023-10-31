from bangun_datar.menu import menu
from bangun_datar.menu import lingkaran
from bangun_datar.menu import persegi
from bangun_datar.menu import segitiga

menu()
while True:
    menu_choice = input("Pilih bentuk 2D (1/2/3/4): ")
    if menu_choice == "1":
        persegi()
    elif menu_choice == "2":
        lingkaran()
    elif menu_choice == "3":
        segitiga()
    elif menu_choice == "4":
        exit()
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")
