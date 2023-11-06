# 1-) Girilen 2 sayıdan hangisi büyüktür?

n1 = int(input("1. sayı : "))
n2 = int(input("2. sayı : "))
if(n1 > n2):
    print("1. sayı daha büyüktür")
elif (n2 > n1):
    print("2. sayı daha büyüktür")

# 2-) Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplatın.
# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
vize1 = float(input("1. Vize : "))
vize2 = float(input("2. Vize : "))
final = float(input("Final : "))

ort = (vize1*0.3 + vize2*0.3 + final*0.4) / 3
result = (ort >= 50)

# 3-) Girilen bir sayının tek mi çift mi oldğunu yazdırın

n = int(input("Sayı : "))




