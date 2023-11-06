
for item in range(0,100,5):
    print(item)

print(list(range(5,100,10)))

index = 0
greeting = "Hello There"

for letter in greeting:
    print(letter)
    
# Enumarate : index , indexteki karakter şeklinde ayrı ayrı elemanları alır.
for item in enumerate(greeting):
    print(item)

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
list3 = [100,200,300,400,500]

# Zio : ayrı ayrı listelerin elemanları 1_1 2_1 , 1_2, 2_2 olarak eşleştirip birleştirir.
print(list(zip(list1,list2)))

for a,b,c in zip(list1,list2,list3):
    print(a,b,c)
