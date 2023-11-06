

SadikHesap = {
    "ad": "Sadık Turan",
    "hesapNo": "12345",
    "bakiye": 3000,
    "ekHesap": 2000
}


AliHesap = {
    "ad": "Ali Turan",
    "hesapNo": "123456",
    "bakiye": 2000,
    "ekHesap": 1000
}


def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print("Paranızı alabilirsiniz.")
    else:
        toplamMiktar = hesap['bakiye'] + hesap['ekHesap']

        if toplamMiktar >= miktar:
            ekHesapKullanimi = input("Ek Hesap Kullanılsın Mı? (e/h)")

            if ekHesapKullanimi == "e":
                hesap['bakiye'] -= miktar
                print("Paranızı alabilirsiniz")

            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")

        else:
            print("Üzgünüz bakiye yetersiz!")


paraCek(SadikHesap, 5100)


