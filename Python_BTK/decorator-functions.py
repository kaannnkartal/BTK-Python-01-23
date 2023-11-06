# Neden ? : Bir fonksiyona bir özellik eklemek
# Bir özelliği bir kaç yerde kullanmak istiyorsak
# Bir decorator fonksiyonu birden fazla yerde kullanabiliriz.

def my_decorator(func):
    def wrapper(name):
        print("Fonksiyondan önceki işlemler")
        func(name)
        print("Fonksiyondan sonraki işlemler")
    return wrapper

@my_decorator ## my_decorator fonksiyonuna çağırmadan gönderir.
def sayHello(name):
    print("hello",name)

# def sayGreeting():
#     print("Greeting")


# sayHello = my_decorator(sayHello)
sayHello("ali")
# sayGreeting = my_decorator(sayGreeting)
# sayGreeting()


import math
import time


def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)

        func(*args,**kwargs)

        finish = time.time()
        print("fonksiyon " + func.__name__+ " " + str(finish - start) + " saniye sürdü")
    return inner


@calculate_time
def usAlma(a,b):

    print(math.pow(a,b))

@calculate_time
def factorial(num):

    print(math.factorial(num))



usAlma(2,3)

factorial(4)