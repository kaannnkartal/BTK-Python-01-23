# 1-) "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste olusturun.

brands = ["Bmw","Mercedes","Open","Mazda"]
print(brands)

# 2-) Liste kaç elemanlıdır?

print(len(brands))

# 3-) Listenin ilk ve son elemanı?

print(brands[0], brands[len(brands)-1]) ## Son eleman için -1 olabilirdi.


# 4-) Mazdanın değerini Toyota ile değiştirin.

brands[3] = "Toyota"
print(brands)

# 5-) Mercedes listenin bir elemanı mıdır?

##check = brands.__contains__("Mercedes")
# NOT: in operatörü kullanmaya karar verdim.
check = "Mercedes" in brands
print(check)

# 6-) Listenin -2 indeksindeki değer nedir?

print(brands[-2])

# 7-) Listenin ilk 3 elemanını alın.

print(brands[0:3])

# 8-) Listenin son 2 elemanı yerine "Toyota" ve Renault değerlerini ekleyin.

brands[-2:] = ["Toyota" , "Renault"]
print(brands)
"""brands.__add__(-2,"Toyota")
brands.__add__(-1,"Renault")
print(brands)"""

# 9-) Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
#Not : + operatörü ile sona ekleme yapılır.
brands = brands + ["Audi", "Nissan"]
print(brands)

"""brands.append("Audi")
brands.append("Nissan")
print(brands)"""

# 10-) Listenin son elemanını silin.

del brands[-1]
"""brands.pop(-1)"""
print(brands)

# 11-) Listenin elemanlarını tersten yazdırın.

print(brands[-1::-1])

# 12-) Aşağıdaki verileri bir liste içinde saklayınız.
    # studentA: Yiğit Bilgi 2010, (70,60,70)
    # studentB: Sena Turan 1999, (80,80,70)
    # studentC: Ahmet Turan 1998, (80,70,90)

studentA = ["Yiğit","Bilgi",2010,[70,60,70]]
studentB = ["Sena","Turan",1999,[80,80,70]]
studentC = ["Ahmet","Turan",1998,[80,70,90]]

students = [studentA] + [studentB] + [studentC]

print(students)

# 13-) Öğrencilerin notlarının ortalamasını yazdırın.

ortA = students[0][-1][0] 
print(ortA)