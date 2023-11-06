message = "Hello  There. My name is Kaan Kartal"

message = message.upper() # ALL LETTERS CAPITAL.
message = message.lower() # all letters lowest.
message = message.title() # All Letters Title.
message = message.capitalize() #First letter capital.

message = message.strip() # Baş ve sondaki boşlukları siler.
message = message.split() # Mesaj kelimeleri string array olarak atanır.Ayrı ayrı
## Split fonksiyonu parametre alabilir. Parametresiz default boşluğa göre split eder.
## Parametre verirsek mesela ',' gibi bu sefer virgüle göre split eder.
## Örnek :
##message = "Selam,ben,kaan,kartal,nasılsınız,umarım,iyisinizdir."
##message = message.split(',')

## Join fonksiyonu : Split ile kelimeleri dizi haline getirdiğimiz stringi tekrar string hale çevirir.
message = ' '.join(message)

index = message.find("kaan") ## Stringdeki kelimeyi bulur. Ve onun ilk harfinin indexini döndürür.
print(index)
isFound = message.startswith('H') ## Başlangıç karakter kontrolü
isFound = message.endswith('l') ##Bitiş karakter kontrolü
print(isFound)
message = message.replace("kaan","mecit") ## Replace : İlk parametre old string, ikinci parametre yerine gelen new string.
##message = message.replace(" ",'*')


print(message)