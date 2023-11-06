

## Burada boş çağırılırsa default name'i unknown atadık.
def sayHello(name = "Unknown"):
    print("Hello " + name)


sayHello("Kaan")
sayHello()

print(help(sayHello))