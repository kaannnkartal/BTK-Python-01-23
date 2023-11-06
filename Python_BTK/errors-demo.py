# liste = ["1","2","5a","10b","abc","10","50"]

# # 1-) Liste elemanları içindeki sayısal değerleri bulunuz

# for item in liste:
#     try:
#         result = int(item)
#         print(result)
#     except:
#         pass


# # 2-) Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı olduğundan emin olun
# # Aksi halde hata mesajı yazın.


# while True:
#     for item in liste:
#         try:
#             result = int (item)
#             print(result)
#         except Exception as ex:
#             print(ex)
        
#         finally:
#             inp = input("Çıkış 'q' : ")

#             if inp == "q":
#                 break


# 3-) Girilen parola içinde türkçe karakter hatası veriniz.

turkce_karakterler = "şçğüöıİ"

psw = input("Parola : ")

for letter in psw:
    if letter in turkce_karakterler:
        raise Exception("Türkçe karakter girdiniz!")
    
