from bangun_datar.menu import menu

def persegi():
    print("Menghitung Luas Persegi Panjang")
    p = int(input("Masukan Panjang :"))
    l = int(input("Masukkan Lebar : "))
    luas = p*l
    print("Luas Persegi Panjang adalah ",luas)
    print
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()