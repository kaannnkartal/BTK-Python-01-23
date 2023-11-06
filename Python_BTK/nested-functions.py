


# Encapsulation : Kapsülleme var. İçteki fonksiyon kendisine yeni bir çalışma alanı tanır.
# Dıştaki olaylar inner'ı etkilemiyor.
def outer (num1):
    print("outer")
    def inner_increment(num1):
        print("inner")
        return num1 + 1
    
    num2 = inner_increment(num1)
    print(num1,num2)


outer(10)

#inner_increment(10)  >>> Böyle erişelemez. Çünkü sadece outer kapsamında erişilebilir.



def factorial(number):
    if not isinstance(number,int):
        raise TypeError("number must be an integer")
    
    if not number >= 0:
        raise ValueError("number must be greater than 0 ")
    def inner_factorial(number):
        if number <= 1:
            return 1
        
        return number * inner_factorial(number - 1)

    return inner_factorial(number)


try: 

    print(factorial(-2))

except Exception as ex:
    print(ex)

