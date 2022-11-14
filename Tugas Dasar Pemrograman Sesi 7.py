def Luas_Segitiga():
    print("🔺Hitung Luas Segitiga🔻")
    alas = int(input('Masukan alasnya: '))
    tinggi = int(input('Masukan tingginya: '))
    Luas = 1/2 * (alas * tinggi)
    print("Luas Segitiga Adalah: ", Luas, ("cm2"))

def Luas_Persegi_Panjang():
    print('⬛Hitung Luas Persegi Panjang⬜')
    panjang = float(input('Masukan tingginya: '))
    lebar = float(input('Masukan lebarnya: '))
    Luas = (panjang * lebar)
    print("Luas Persegi Panjang Adalah: ", Luas, ("cm2"))

def Bilangan_Ganjil_Genap():
    print('🚗Menentukan Bilangan Ganjil dan Genap🚓')
    x = int(input('Masukkan Angka: '))
    print('adalah bilangan', 'genap' if (x % 2 == 0) else 'ganjil')

while True:
    try:
        userInput = int(input(
            "MENU : \n1. Luas Segitiga\n2. Luas Persegi Panjang\n3. Menentukan Angka Ganjil Genap\n4. Quit\nPilih Nomer: "))
    except ValueError:
        print("Inputan harus berupa number")
    else:
        if (userInput == 1):
            Luas_Segitiga()
        elif (userInput == 2):
            Luas_Persegi_Panjang()
        elif (userInput == 3):
            Bilangan_Ganjil_Genap()
        else:
            break