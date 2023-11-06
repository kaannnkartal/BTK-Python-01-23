
def usalma(number):

    def inner_us(power):

        return number ** power
    
    return inner_us


copy_inner1 = usalma(3) 

print(copy_inner1(4))

copy_inner2 = usalma(5)

print(copy_inner2(2))



def yetki_sorgu(page):
    
    def inner_rank_access(role):

        if role == "admin":
            print("{0} rolü {1} sayfasına erişebilir".format(role,page))
        else :
            print("{0} rolü {1} sayfasına erişemez".format(role, page))

    
    return inner_rank_access



user1 = yetki_sorgu("CONTROL PANEL")

user2 = yetki_sorgu("CONTROL PANEL")

user1("admin")
user2("user")




def islem(islem_adi):


    def toplama(*args):

        toplam = 0
        for numbers in args:
            toplam += numbers

        return toplam
    
    
    def carpma(*args):

        carpma = 1

        for numbers in args:
            carpma *= numbers

        return carpma
    
    if islem_adi == "toplama":
        return toplama
    elif islem_adi == "carpma":
        return carpma

        
toplama = islem("toplama")

print(toplama(1,2,3,4,5,6,7))

carpma = islem("carpma")

print(carpma(1,2,3,4,5))





