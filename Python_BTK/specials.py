
mylist = [1,2,3]

myString = "my string"

print(len(mylist))
print(len(myString))


class Movie():
    
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie objesi oluşturuldu")
        
    def __str__(self):
        return f"{self.title} by {self.director} "


    def __len__(self):
        return self.duration

    def __delattr__(self):
        print("Movie silindi")


m = Movie("film adı","yönetmen adı ", 120)

print(str(m))

