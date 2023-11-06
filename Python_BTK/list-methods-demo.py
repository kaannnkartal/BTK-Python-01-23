names = ["Ali","Yağmur","Hakan","Deniz"]
years = [1998,2000,1998,1987]

# 1-) "Cenk ismini listenin sonuna ekleyiniz."
names.append("Cenk") ## Insert kullanıp index de verebiliriz (-1)
print(names)

# 2-) "Sena değerini listenin başına ekleyiniz"
names.insert(0,"Sena")
print(names)

# 3-) "Deniz" isminin indeksi nedir?
print(names.index("Deniz"))

# 4-) "Deniz" ismini listeden siliniz.
names.remove("Deniz")
print(names)

# 5-) "Ali" listenin bir elemanı mıdır?
print("Ali" in names)

# 6-) Liste elemanlarını ters çevirin.
names.reverse()
print(names)

# 7-) Liste elemanlarını alfabetik olarak sıralayın.
names.sort()
print(names)

# 8-) years listesini rakamsal büyüklüğe göre sıralayın.
years.sort()
years.reverse()
print(years)

# 9-) str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet,Dacia"
brands = str.split(",")
print(brands)

# 10-) Years dizisinin en büyük ve en küçük elemanı?
max = max(years)
min = min(years)

# 11-) years dizisinde kaç tane 1998 değeri vardır?
print(years.count(1998))

# 12-) years dizisinin tüm elamnlarını siliniz.
years.clear()

# 13-) Kullanıcan alacağınız 3 tane marka bilgisini bir listede saklayınız

user_Brands = []
marka_1 = input("Lütfen 1. markayı giriniz")
user_Brands.append(marka_1)
marka_2 = input("Lütfen 2. marka ismini giriniz ")
user_Brands.append(marka_2)
marka_3 = input("Lütfen 3. marka ismini giriniz")
user_Brands.append(marka_3)

print(user_Brands)

