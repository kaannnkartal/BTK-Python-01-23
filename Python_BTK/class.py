# # Object = Instance

# class Person:
#     # attributes
#     address = "no information"
#     #constructor (yapıcı metod)

#     def __init__(self,name,year):
#         self.name = name
#         self.year = year
#         print("İnit methodu çalıştı")
        
#     # intance methods
#     def intro(self):
#         print("Hello There. I am " + self.name)

#     def calculateAge(self):
#         return 2023 - self.year

# p1 = Person(name = "Kaan", year = 2000)
# p2 = Person("Kardelen",2004)


# print(f"Name : {p1.name} year : {p1.year} address : {p1.address}" )
# print(p1)
# print(p2)

# print(type(p1))
# print(type(p2))

# p1.intro()
# p2.intro()

# print(f"Yaşım : {p1.calculateAge()}")
# print(f"Yaşım : {p2.calculateAge()}")

class Circle:

    pi = 3.14

    def __init__(self,yaricap = 1):
        self.yaricap = yaricap

    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap

    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)



c1 = Circle()
c2 = Circle(yaricap = 5)

print(f"C1 objesinin çevresi {c1.cevre_hesapla()} Alanı : {c1.alan_hesapla()}")
print(f"C2 objesinin çevresi {c2.cevre_hesapla()} Alanı : {c2.alan_hesapla()}")