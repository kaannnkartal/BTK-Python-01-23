import random

# Randrange
luckyN = random.randrange(1,100)
guess = -1
point = 100

limit = int(input("Can sayınızı giriniz : "))

reduce = point / limit

while(point >=0):
    print("Güncel Can Sayınız : ",limit)
    guess = int(input("Tahmin : "))
    
    if guess > luckyN:
        print("Daha küçük")
    elif guess < luckyN:
        print("Daha büyük")
    else:
        break
    limit -= 1
    point -= reduce

if point >= 0:
    print("Tebrikler bildiniz!\nPuanınız : ", point)
else:
    print("Kaybettiniz!")    


