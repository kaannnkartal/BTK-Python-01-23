fruits = {"orange","apple","banana"}

## print(fruits[0]) !!! INDEXLENEMEZ

for x in fruits: # Döngü şeklinde ulaşmak zorundayız.
    print(x)

fruits.add("cherry")
fruits.update(["mango","grape","apple"]) ## APPLE ZATEN VAR. VAR OLAN NESNE BİR DAHA EKLENMEZ


print(fruits)


fruits.remove("mango")
print(fruits)


## Tekrarlanamyacağının kanıtı : 

myList = [1,2,5,4,4,2,1]

print(set(myList))