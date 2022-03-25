a = float(input("Adja meg az a oldalt."))
b = float(input("Adja meg a b oldalt."))
c = float(input("Adja meg a c oldalt."))

if a + c > b:
    print("Ezt a háromszöget meg lehet szerkeszteni.")
    if a**2 + b**2 == c**2:
        print("Ez a háromszög derékszögű.")
        print(f"háromszög terültete:")
        print(f"háromszög kerültete:{a + b + c}")

    elif a == b:
        print("Ez a háromszög egyenlőszárú")
        print(f"háromszög terültete:")
        print(f"háromszög kerültete:{a + b + c}")
   
    else:
        print(f"háromszög kerültete:{a + b + c}")

else:
    print("Ezt a háromszöget nem lehet megszerkeszteni.")
