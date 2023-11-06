# Girilen bir sayının asal olup olmadığını bulun

number = int(input("Sayı girin : "))

flag = False
for i in range(2,number):
    if (number % i == 0):
        print("Sayı asal değil")
        flag = True
        break
    else:
        continue

if(not flag):
    print("Sayı asal!")