sayilar = [1,3,5,7,9,12,19,21]

# 1-) Sayilar listesindeki hangi sayılar 3'ün katıdır?
for sayi in sayilar:
    if(sayi % 3 == 0):
        print(sayi)

# 2-) Sayilar listesinde sayıların toplamı kaçtır?
sum = 0
for sayi in sayilar:
    sum += sayi
print(sum)

# 3-) Sayilar listesindeki tek sayıların karesini alınız.
for sayi in sayilar:
    if(sayi % 2 == 1):
        print(sayi**2)

# 4-) Şehirlerden hnagiler en fazla 5 karakterlidir?
sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]
for sehir in sehirler:
    if(len(sehir) <= 5):
        print(sehir)

urunler = [
    {"name" : "samsung S6", "price" : "3000"},
    {"name" : "samsung S7", "price" : "4000"},
    {"name" : "samsung S8", "price" : "5000"},
    {"name" : "samsung S9", "price" : "6000"},
    {"name" : "samsung S10", "price" : "7000"}
]

# 5-) Ürünlerin fiyatları toplamı nedir?
sum = 0
for urun in urunler:
    sum += int(urun["price"])
print(sum)

# 6-) Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz
for urun in urunler:
    if(5000 >= int(urun["price"])):
        print(urun["name"])

