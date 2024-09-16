print("hello")
print(2, type(2))
print(3.14159, type(3.14159))
print(3.1 + 1j, type(3.1 + 1j))
print(5 / 2)  #impartire
print(5 // 2)  #cat
print(5 % 2)  #rest
print(4 > 2 and 3 < 5)
print(4 > 7 or 3 < 5)
print(not True)
print('A' in 'mara' or 'a' in 'mara')  #cautarea in strings e case sensitive
nrMere = 5
variabila = "Ana are " + str(nrMere) + " mere"
print(variabila)
variabila = f"Ana are {nrMere} mere"
print(variabila)

lista = [8, 2, "ceva", 8, "reimon", 4.2, True, "ceva", "ceva"]
for  element in lista:
    print(element)
print(lista[1:7:2])
lista.append("ceva.ceva")
while "ceva" in lista:
    lista.remove("ceva")
print(lista)
lista.append(6646)
print(lista.index("ceva.ceva"))
lista.reverse()
lista.pop(1)
