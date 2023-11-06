
# 1-) Gönderilen bir kelimeyi belirtilen kez ekran gösteren fonksiyonu yazın.

def printWord(word, number):
    for x in range(number):
        print(word)

printWord("Kaan",3)

# 2-) Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon yazın

def myFunc(*params):
    liste = []

    for param in params:
        liste.append(param)
    return liste

myList = myFunc(1,2,3,"Kaan")
print(myList)

# 3-) Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

def primes(n1,n2):
    
    for x in range(n1,n2+1):
        flag = False
        for y in range(2,x):
            if (x % y ==0):
                flag = True
                break
        if(not flag):
            print(x)

primes(5,17)

# 4-) Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyon.

def tamBolen(n):
    bolens = []
    """for sayi in range(1,n+1):
        if(n % sayi == 0):
            bolens.append(sayi)

    return bolens"""
    bolens = [sayi for sayi in range(1,n+1) if n % sayi == 0]
    return bolens

print(tamBolen(20))