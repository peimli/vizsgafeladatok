import math
a = float(input("Add meg az [a] értékét."))
b = float(input("Add meg a [b] értékét."))
c = float(input("Add meg a [c] értékét."))
p = a**2 / c
q = b**2 / c
m = math.sqrt(p * q)
if a + c > b:
    print("Létezhet ez a háromszög ilyen oldalhosszokkal.")
    if a**2 - b**2 == c**2 or b**2 - a**2 == c**2:
        print("Ez a háromszög derékszögű.")
        print("Ez a háromszög NEM egyenlőszárú.")
        print(f"háromszög kerültete:{a + b + c}")
        print(f"háromszög terültete: {(a * m) / 2}")

    elif a == b:
        print("Ez a háromszög NEM derékszögű.")
        print("Ez a háromszög egyenlőszárú")
        print(f"háromszög kerültete:{a + b + c}cm ")
        print(f"háromszög terültete:{(a * m) / 2}cm^2 ")

    else:
        print("Ez a háromszög NEM derékszögű.")
        print("Ez a háromszög NEM egyenlőszárú.")
        print(f"háromszög kerültete:{a + b + c}")
        print(f"háromszög terültete:{(a * m) / 2} ")

else:
    print("Ezt a háromszöget nem lehet megszerkeszteni.")
