print('''
TOPLAMA İŞLEMİ YAPMAK İÇİN 1 'e BASIN.
ÇIKARMA İŞLEMİ YAPMAK İÇİN 2 'e BASIN.
ÇARPMA İŞLEMİ  YAPMAK İÇİN 3 'e BASIN.
BÖLME İŞLEMİ   YAPMAK İÇİN 4 'e BASIN.
ÇIKMAK İÇİN 5'e BASIN.

''')

islemYap = str(input("Yapmak İstediğiniz İslemi Seçiniz : "))

if islemYap == "1":
    sayi1 = int(input("1. Sayıyı Giriniz --> "))
    sayi2 = int(input("2. Sayıyıy Giriniz --> "))
    print("Bulunan Sonuç -->", sayi1 + sayi2)
elif islemYap == "2":
    sayi1 = int(input("1. Sayıyı Giriniz --> "))
    sayi2 = int(input("2. Sayıyı Giriniz --> "))
    print("Bulunan Sonuç --> ", sayi1 - sayi2)
elif islemYap == "3":
    sayi1 = int(input("1. Sayıyı Giriniz --> "))
    sayi2 = int(input("2. Sayıyı Giriniz --> "))
    print("Bulunan Sonuç -->", sayi1 * sayi2)
elif islemYap == "4":
    sayi1 = int(input("1. Sayıyı Giriniz --> "))
    sayi2 = int(input("2. Sayıyı Giriniz --> "))
    print("Bulunan Sonuç -->", sayi1 / sayi2)

elif islemYap == "5":
    print("Çıkış Yapıldı.")
else:
    print("Geçersiz bir işlem seçtiniz.")
    