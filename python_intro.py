name = []
def hi(name):
    print("hej")
    print("pogadamy")
    print(name)
    print("jestes taki saksowny")

for i in range(1,3):
    print('podaj imie szmato')
    name.append(input("imie: "))

for imiona in name:
    hi(imiona)
