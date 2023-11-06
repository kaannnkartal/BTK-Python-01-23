# key - value

# 41 => Kocaeli, 34 => İstanbul

plakalar = {'Kocaeli':41 , "İstanbul" : 34}

print(plakalar["Kocaeli"])

plakalar["Ankara"] = 6

print(plakalar["Ankara"])


users = {
    "sadikturan" : {
        "age" : 36,
        "roles" : ["user"],
        "email" : "sadik@gmail.com",
        "address" : "Kocaeli",
        "phone" : "123321"
    },
    "cinarturan" : {
        "age" : 2,
        "roles" : ["admin","user"],
        "email" : "cinar@gmail.com",
        "address" : "Kocaeli",
        "phone" : "123321"
    }
}

print(users["cinarturan"]["age"])
print(users["cinarturan"]["email"])
print(users["cinarturan"]["address"])

print(users["cinarturan"]["roles"][0])

## YANİ KEY- VALUE AMA VALUE DICT OLABİLİR.
## DICT = KEY : DICT (DICT YİNE BİR KEY VALUE) YANİ:
# DICT = KEY : [KEY : VALUE] BURADAKİ VALUE YERİNE DE DICT
# DICT = KEY : [KEY : DICT] SEKLINDE OLABİLİR.