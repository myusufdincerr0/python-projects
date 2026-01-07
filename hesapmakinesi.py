import math

def menu():
    print("\n--- Hesap Makinesi ---")
    print("1 - Toplama")
    print("2 - Çıkarma")
    print("3 - Çarpma")
    print("4 - Bölme")
    print("5 - Üs Alma")
    print("6 - Karekök")
    print("7 - Mod Alma")
    print("8 - Sinüs")
    print("9 - Kosinüs")
    print("10 - Tanjant")
    print("11 - Logaritma (10 tabanında)")
    print("12 - Faktöriyel")
    print("0 - Çıkış")

while True:
    menu()
    secim = input("Seçiminizi girin: ")

    if secim == "0":
        print("Hesap makinesi kapatıldı.")
        break

    try:
        if secim in ["1", "2", "3", "4", "5", "7"]:
            a = float(input("1. sayı: "))
            b = float(input("2. sayı: "))

            if secim == "1":
                print("Sonuç:", a + b)
            elif secim == "2":
                print("Sonuç:", a - b)
            elif secim == "3":
                print("Sonuç:", a * b)
            elif secim == "4":
                if b == 0:
                    print("Hata: Sıfıra bölünemez!")
                else:
                    print("Sonuç:", a / b)
            elif secim == "5":
                print("Sonuç:", a ** b)
            elif secim == "7":
                print("Sonuç:", a % b)

        elif secim == "6":
            x = float(input("Sayı: "))
            print("Sonuç:", math.sqrt(x))

        elif secim == "8":
            x = float(input("Açı (derece): "))
            print("Sonuç:", math.sin(math.radians(x)))

        elif secim == "9":
            x = float(input("Açı (derece): "))
            print("Sonuç:", math.cos(math.radians(x)))

        elif secim == "10":
            x = float(input("Açı (derece): "))
            print("Sonuç:", math.tan(math.radians(x)))

        elif secim == "11":
            x = float(input("Sayı: "))
            print("Sonuç:", math.log10(x))

        elif secim == "12":
            x = int(input("Sayı: "))
            print("Sonuç:", math.factorial(x))

        else:
            print("Geçersiz seçim!")

    except ValueError:
        print("Hatalı giriş! Lütfen sayı girin.")
