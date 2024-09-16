dictionar = {
    1: "Ana",
    "2": "Mere",
    3: "Pere",
    4: "prune",
    "1": "Mara"

}
print(type(dictionar))
print(dictionar.get(22, "Nu gaseste nimic"))
print(dictionar["2"])
dictionar.update({"2": "new val"})
dictionar[22] = "some new data"
print(dictionar[22])
print(dictionar.keys())
print(dictionar.values())
print(dictionar.items())