# valtozasdtuma, atlagarliterb, atlagarliterg 
class Uzemanyag:
    def __init__(self, sor):
        valtozasdtuma, atlagarliterb, atlagarliterg = sor.strip().split(";")
        self.valtozasdtuma = valtozasdtuma
        self.atlagarliterb =  atlagarliterb
        self.atlagarliterg = atlagarliterg
        
with open("uzemanyag.txt", encoding="latin2") as f:
        lista = [Uzemanyag(sor) for sor in f]

#3.feladat:
print(f"3.feladat: Változások száma: {len(lista)}")

#4.feladat:
kulonbseg = [(int(sor.atlagarliterb) - int(sor.atlagarliterg)) for sor in lista if (int(sor.atlagarliterb) - int(sor.atlagarliterg)) ==  0]

print(f"4.feladat: A legkisebb különbség: {min(kulonbseg)}")

#5.feladat:
print(f"5.feladat: A legkisebb különbség előfordulása: {len(kulonbseg)}")

#6.feladat:
szokonap = [sor for sor in lista if int(sor.valtozasdtuma[:4]) % 4  == 0]
volt = "Volt" if szokonap else "Nem volt"
print(f"6.feladat: {volt} változás szökőévben.")

#7.feladat:

with open('euro.txt', 'w', encoding='latin2') as f:
    f.writelines(volt)     
















