print("""

KULLANICI GİRİŞ EKRANI


""")

sys_username = "webgelistiricim"
sys_password = "123"

kullanici_adi = input("Kullanıcı Adını Giriniz: ")
sifre = input("Şifre'yi Giriniz: ")

if (kullanici_adi == sys_username) and (sifre != sys_password):
    print("Şifre yanlış..")

elif (kullanici_adi != sys_username) and (sifre == sys_password):
    print("Kullanıcı adı yanlış..")

elif (kullanici_adi != sys_username) and (sifre != sys_password):
    print("Kullanıcı adı ve şifre yanlış..")
else:
    print("Giriş yapıldı!")
    bakiye = 1000

    while True:
        islem = input("Yapmak İstediğiniz İşlemi Seçiniz:")
        if (islem == "q"):
            print("Yine Bekleriz...")
            break
        elif (islem == "1"):
            islem = input("Bakiyeniz: {}".format(bakiye))

        elif (islem == "2"): 
            miktar = int(input("Yatırmak İstediğiniz Tutar'ı Giriniz:"))
            bakiye += miktar

        elif (islem == "3"):
            miktar = int(input("Çekmek İstediğiniz Miktar'ı Giriniz:"))
            if (bakiye - miktar < 0):
                print("Geçersiz İşlem Yaptınız.")
                print("Hesabınızda ki Bakiye {}".format(bakiye))
                continue
            bakiye -= miktar
        else:
            print("Geçersiz İşlem Yaptınız Yeniden Deneyiniz.")





    
