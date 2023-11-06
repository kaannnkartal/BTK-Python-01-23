def not_hesapla(satir):

    pass



def ortalamalari_oku():

    with open ("notlar.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))


def not_gir():
    ad = input("Öğrenci adı : ")
    soyad = input("Öğrenci Soyad: ")
    not1 = input("Not 1 : ")
    not2 = input("Not 2 : ")
    not3 = input("Not 3 : ")

    with open("notlar.txt","a",encoding="utf-8") as file:
        file.write(ad + " " +  soyad + " : " + not1+","+not2+","+not3+"\n")




def notlari_kayit_et():

    pass



while True:

    islem = input("1- Notları Oku\n2- Not Gir\n3- Notları Kayıt Et\n4- Çıkış\n")

    if islem == "1":
        ortalamalari_oku()

    elif islem == "2":
        not_gir()
    elif islem == "3":
        notlari_kayit_et()
    else:
        break
