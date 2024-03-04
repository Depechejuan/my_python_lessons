weight = input("Introduce your weight: ")
unity = input("(L)bs or (K)g: ")
unity.lower()
if unity == "k":
    total = int(weight) / 0.45
    print(f"You are {total} pounds")
elif unity == "l":
    total = int(weight) * 0.45
    print(f"You are {total} kilos")

##
peso = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    converted = peso * 0.45
    print(f"You are {converted} kilos")
else:
    converted = peso / 0.45
    print(f"You are {converted} pounds")