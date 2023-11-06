numbers = []

for x in range (10):
    print(x)


# Diziye böyle atama da yapılabilir.
# DÖngü kullanarak x'in elemanları değişir ve listeye atılır.

numbers = [x for x in range(10)]
print(numbers)

## Sadece 3'ün katı olan sayıların karesini aldık.
numbers = [x*x for x in range(10) if x%3 ==0]
print(numbers)

myString = "Hello"
myList = []

for letter in myString:
    myList.append(letter)

print(myList)

# Aynı seyi böyle de yapabiliriz : 
# Dizi oluşturulurken için elemanları for döngüsü ve if idasi kullanarak atabiliriz.

myList = [letter for letter in myString]
print(myList)

years = [1992,1999,2008,1956,1986]

# Yaşları hesaplayıp age dizisine attık wow!
ages = [2023 - year for year in years]
print(ages)

results = [x if x%2 == 0 else "TEK" for x in range(1,10)]
print(results)

result = []
for x in range(3):
    for y in range(3):
        result.append((x,y))

print(result)

numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers)