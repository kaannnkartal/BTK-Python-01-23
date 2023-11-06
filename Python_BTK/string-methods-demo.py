website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
# 1-) ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin
message = " Hello World "
message = message.strip()
## Sadece soldaki boşluk için lstrip ya da sadece sağdaki boşluk için rstrip yazılabilir.

print(message)

# 2-) 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.

##website = website.replace(website, website[7:])
## Left strip kullanarak nasıl yaparız?
website = website.lstrip("htp:/") ## her bir karakteri 1 defa yazmamız yeterlidir.
print(website)


# 3-) 'course' karakter dizisinin tüm karakterlerini küçük harf yapın

course = course.lower()

# 4-) 'website' içinde kaç tane a karakteri vardır

count_a = website.count('a')
print(count_a)

## NOT : count methodu string.count('x',startIndex,endIndex) şeklinde belirli aralıkta arayabilir.

# 5-) 'website' wwww" ile başlayıp com ile bitiyor mu?

checkStart_End = website.startswith("www") and website.endswith(".com")
print(checkStart_End)

# 6-) website içinde '.com' ifadesi var mı?
## Find methodu da kullanabilir. İlk indexi verecektir.
check = website.__contains__(".com")
print(check)

# 7-) 'course' içindeki karaktelrerin hepsi alfabetik mi? (isAlpha, isDigit)

check = course.isalpha() ## false sayısal değerler de var 40 saat.
check = "hello".isalpha()
print(check)

# 8-) 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

message = "Contents"
message = message.center(50,'*')
print(message)

# 9-) 'course' karkater dizisindeki tüm boşlukları '-' ile değiştirin.

course = course.replace(" ", '-')
print(course)

# 10-) 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin.

message = "Hello World"
message = message.replace("Hello","There")
print(message)

# 11-) 'course karakter dizisinin '-' karakterlerinden ayırın.

course = course.split('-')
print(course)

