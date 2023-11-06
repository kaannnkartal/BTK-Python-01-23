def changeName (n):
    n = "Kardelen"

name = "Kaan"

changeName(name)
print(name)

## Sonuç : Fonksiyona gönderilen isim Kardelen olarak değişmedi. Value type.

################################################

def change (n):
    n[0] = "İstanbul"

"""sehirler = ["Ankara","İzmir"]
change(sehirler)
print(sehirler)"""
## Fonksiyonun içinde listenin ilk elemanını İstanbul olarak değiştirdik. Çünkü Referece type.

sehirler = ["Ankara","İzmir"]
n = sehirler[:] ## BU DURUMDA Sehirler dizisinin içindeki elemanlar ayrı ayrı tek tek yeni diziye eklenir. Bu yüzden Reference type olmaz(Aynı adresi tutmazlar. Farklı bir dizi olur)
## Bu işleme slicing işlemi denir. Parçalama işlemidir.
n[0] = "İstanbul"

print(sehirler)
print(n) 

#################################################################
## FONKSIYON 2 PARAMETRE ALIYOR OLSUN AMA 3 4 5 6 PARAMETRE GÖNDERMEK İSTERSEM ?
## *parameters olarak kullanılır ve gönderilen çoklu parametre bir tuple listesinde tutulur.

def add(*params):
    return sum(params)

print(add(10,20,30))
print(add(10,20,30,40))
print(add(10,20,30,40,50))

## ADD FONKSIYONU STANDART DEĞİL MULTIPARAMETRELİ OLDU
#######################################################################
## **parameters ise yine multi-parametreler için kullanılır. Gönderilen çoklu parametre bir dictionary veri yapısında tutulur.


def displayUser(**params):

    for key,value in params.items():
        print(f"{key} is {value}")
    return 0


displayUser(name = "Çınar",age = 2, city = "İstanbul")
displayUser(name = "Ada",age = 12, city = "Kocaeli", phone = "12345")
displayUser(name = "Yiğit",age = 14, city = "Ankara", phone = "12345", email = "x@gmail.com")


###############################################################################
## Özet olarak tek bir fonksiyonda çeştili parametreler : 

def myFunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


myFunc(10,20,30,40,50,key1 = "Kaan", key2 ="Kartal")





