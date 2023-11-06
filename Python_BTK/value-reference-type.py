x = 5
y = 25

x=y

y = 10

print(x,y)

## String, number
## Y nin sonradan değişmesi daha önce x e atanan y değerined bir değişikliğine neden olmadı.
## Bundan dolayı value typedır.
## Bellekte x ' in ayrı bir lokasyonu y'nin ayrı bir lokasyonu vardır.

############### REFERENCE TYPE ##################

a = ["apple","banana"]
b = ["apple","banana"]

a = b

b[0] = "grape"

print(a,b)

## Adresler birbirleriyle eşitlenmiş olur.
## 