website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1-) Course dizisinde kaç karakter bulunmaktadır.
print("Course karakter dizisinde {} karakter bulunmaktadır.".format(len(course)))
# 2-) website içinden 'www' karakterini alın.
print(website[7:10])
# 3-) website içinden 'com' karakterlerini alın.
print(website[-3::1])
# 4-) course içinden ilk 15 ve son 15 karakteri alın.
print(course[0:15], "and", course[-15:])
# 5-) course'u tersten yazdırın.
print(course[-1::-1])

name,surname,age,job = 'Kaan','Kartal', 22, 'mühendis'

# 6-) Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın
#       'Benim adım Kaan Kartal, Yaşım 22 ve mesleğim mühendis.'

print("Benim adım {} {}, Yaşım {} ve mesleğim {}.".format(name,surname,age,job))

# 'Hello world' ifadesindeki w harfiin 'W' ile değiştirin.
S = "Hello world"
S = S[0:6] + 'W' + S[7:]
print(S)

# 8-) 'abc' ifadesini yan yana 3 defa yazdırın

print("abc"*3)
