numbers = [1,10,5,16,4,9,10]
letters = ['a','g','s','b','y','a','s']

val = min(numbers)
val = max(numbers)
val = max(letters)

val = numbers[3:6]
numbers[4] = 40

numbers.append(49) ## Listenin sonuna ekleme yapar.
numbers.insert(3,78) ## Listenin belirli indexine ekleme yapar, indexten sonraki elemanları bir kaydırır.

##numbers.pop() ## En sondaki elemanı siler.
numbers.pop(0) ## Parameter olarak index alabilir.
numbers.remove(16) ## Parametre olarak silinecek nesneyi alır. Yani 16 sayısını arar bulur ve siler.

numbers.sort() ##Listeyi küçükten büyüğe sıralar.
letters.sort()

numbers.reverse() ## Listeyi tersine çevirir. Sondan başa reverse.

numbers.clear() ## Tüm elemanları siler.
print(numbers)