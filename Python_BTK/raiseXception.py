# x = 10

# if x > 5:
#     raise Exception("X 5'ten büyük olamaz")




import re


def check_password(psw):


    if len(psw) < 8:
        raise Exception("Parola en az 8 karakter olmalıdır")

    elif not re.search("[a-z]" , psw):
        raise Exception ("Parola küçük harf içermelidir")
    elif not re.search("[A-Z]", psw):
        raise Exception("Parola büyük harf içermelidir")
    elif not re.search("[0-9]", psw):
        raise Exception("Parola rakam içermelidir")
    elif not re.search("[_@$]", psw):
        raise Exception("Parola alfa numerik harf içermelidir")
    elif  re.search("\s", psw):
        raise Exception("Parola boşluk içermemelidir")
    

password = "12345678"
try : 
    check_password(password)
except Exception as ex:
    print(ex)

    
    
    
    
