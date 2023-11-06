x,y,z = 2,5,10

numbers = 1,5,7,10,6


# 1-) Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?

n1 = int(input("Lütfen 1. sayıyı giriniz : "))
n2 = int(input("Lütfen 2. sayıyı giriniz : "))

result = (n1*n2) - (x+y+z)
print(result)

# 2-) y'nin x'e kalansız bölümünü hesaplayınız

result = y//x
print(result)

# 3-) (x,y,z) toplamının mod 3ü nedir?

result = (x+y+z) % 3 
print(result)

# 4-) y'nin x. kuvvetini hesaplayınız

result = y**x
print(result)

# 5-) x, *y, z = numbers işlemine göre z' küpü kaçtır?

x, *y, z = numbers  ## numbers bir tuppledır. *y ifadesi y'yi alabileceği değer kadar array yapar.
result = z**3
print(result)

# 6-) x, *y, z = numbers işlemine göre y nin değerleri toplamı nedir?

x,*y,z = numbers
result = 0
for value in y:
    result += value

print(result)
