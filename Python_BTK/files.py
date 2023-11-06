# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.

# Kullanımı : open(dosya_adi,dosya_erişme_modu)

# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w" : (write) yazma modu. Dosyayı konumda oluşturur.
# ** Var olan içeriği siler ve yeniden ekleme yapar.
# "a" : (Append) ekleme, Dosya konumda yoksa oluşturur
# "x" : (Create) oluşturma. Dosya zaten varsa hata verir.
# "r" : (Read) okuma, varsayılan. dosya konumda yoksa hata verir


# file = open("newfile.txt", "w", encoding="utf-8")

# #file.write("Sadık Turan")

# file.close()


