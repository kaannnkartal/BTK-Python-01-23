def square(num): return num**2 ## Aynı satıra yazabiliriz.


numbers = [1,3,5,9]

# Map kullanımı : 

map(square, numbers) ## Fonksiyon ve liste gönderdim.

result = map(square,numbers) ## Adres döndürür
result = list(map(square,numbers))

for item in map(square,numbers): ## Enumarate edildi, her bir indexi döndürdü.
    print(item)
print(result)

## Square' in yaptığı işi isimsiz bir fonksiyon ile yaptık.
## Bu işi lambda yaptı.
result = list(map(lambda num: num **2,numbers))
print(result)

## İsim de verebiliriz
square2 = lambda num : num **2

result = list(map(square2,numbers))
print(result)

result = square2(3)
print(result)

numbers = [1,3,5,9,10,4]

def check_even(num): return num %2 == 0

result = list(filter(check_even,numbers))
print(result)

result = list(filter(lambda num : num%2==0, numbers))
print(result)

check_even2 = lambda num : num %2==0
result = list(filter(check_even2,numbers))
print(result)

result = check_even2(numbers[2])
print(result)

## Genel olarak lambda fonksiyon kullanmadan yapılabilecek işlevleri yapar.
## Bunun yanında beraber kullanıldığı filter ve map methodları vardır.

