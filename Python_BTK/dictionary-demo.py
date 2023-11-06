students = {}
students_info_1 = {}
students_info_2 = {}
students_info_3 = {}
no = input("Lütfen öğrenci numarasını giriniz : ")
name = input("Lütfen öğrenci adını giriniz : ")
students_info_1["ad"] = name
sname = input("Lütfen öğrenci soyadını giriniz : ")
students_info_1["soyad"] = sname
phone = input("Lütfen öğrenci telefonunu giriniz : ")
students_info_1["telefon"] = phone

students[no] = students_info_1

## ---
key = input("Lütfen öğrenci numarasını giriniz : ")
val1 = input("Lütfen öğrenci adını giriniz : ")
students_info_2["ad"] = val1
val2 = input("Lütfen öğrenci soyadını giriniz : ")
students_info_2["soyad"] = val2
val3 = input("Lütfen öğrenci telefonunu giriniz : ")
students_info_2["telefon"] = val3

students[key] = students_info_2

# ---

key = input("Lütfen öğrenci numarasını giriniz : ")
val1 = input("Lütfen öğrenci adını giriniz : ")
students_info_3["ad"] = val1
val2 = input("Lütfen öğrenci soyadını giriniz : ")
students_info_3["soyad"] = val2
val3 = input("Lütfen öğrenci telefonunu giriniz : ")
students_info_3["telefon"] = val3

students[key] = students_info_3

## 2. PART


inpNo = input("\nLütfen aramak istediğiniz öğrenci numarasını giriniz : ")

#print("Öğrenci Adı : " ,students[inpNo]["ad"])
#print("Öğrenci SoyAdı : " ,students[inpNo]["soyad"])
#print("Öğrenci Telefon : " ,students[inpNo]["telefon"])

ogrenci = students[inpNo]

print("Öğrenci Adı : {}\nÖğrenci Soyadı : {}\nÖğrenci Telefon : {}".format(ogrenci["ad"], ogrenci["soyad"],ogrenci["telefon"]))


