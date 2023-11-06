sayilar = [1,3,5,7,9,12,19,21]

# 1-) sayilar listesini while ile ekrana yazdırın.

i = 0
while i < len(sayilar):
    print(sayilar[i])
    i = i+1

# 2-) Başlangıç ve bitiş değerlerini kullanıcıdan alıp
# aradaki tüm tek sayıları ekrana yazdırın.

startIndex = int(input("Start : "))
endIndex = int(input("End : "))
currentIndex = startIndex
while currentIndex != endIndex:
    if(sayilar[currentIndex] % 2 == 1):
        print(sayilar[currentIndex])
    currentIndex+=1

# 3-) 1-100 arasındaki sayıları azalan şekilde yazdırın.

count = 100

while count >= 1:
    print(count)
    count-=1

# 4-) Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı yazdır.

count = 1
numbers = []
while count <= 5:
    number = int(input("Sayı giriniz : "))
    numbers.append(number)
    count += 1

numbers.sort()
print(numbers)

# 5-) Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesinde sakla.
#   ** ürün sayısını kullanıcıya sorun
#   ** dictionary listesi yapısı (name,price) olsun.
#   ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile gösterin.

urunSayisi = int(input("Ürün sayısı : "))
count = 0
urunler = []


while count < urunSayisi:
    name = input("Ürün ismini giriniz : ")
    price = input("Ürün fiyat : ")
    urunBilgi = {"name" : name, "price" : price}
    urunler.append(urunBilgi)
    count += 1
    print("Ürün Başarıyla Eklendi")

i = 0
while i<len(urunler):
    print(urunler[i]["name"])
    i+=1



