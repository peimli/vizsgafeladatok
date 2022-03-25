class Bolygok:
    def __init__(self, sor):
        bolygo, holdjai, terfogatarany = sor.strip().split(';')
        self.bolygo = bolygo
        self.holdjai = holdjai
        self.terfogatarany = terfogatarany
        
with open('solsys.txt', encoding='UTF-8') as f:
    lista = [Bolygok(sor) for sor in f]
    
    
#1.feladat:
print(f"{len(lista)} bolygó van a naprendszerben.")

#2.feladat:
holdakszama = [int(sor.holdjai) for sor in lista]
print(f"A naprendszer bolygóinak átlagosan {sum(holdakszama) / len(holdakszama)} holdja van.")

#3.feladat:
terfogat = [float(sor.terfogatarany) for sor in lista]
legnagyobbterfogatarany = max(terfogat)
legnagyobbterfogataranyubolygo = [sor.bolygo for sor in lista if float(sor.terfogatarany) == 1321.0]

print(f"A legnagyobb térfogatarányú bolygó a {legnagyobbterfogataranyubolygo[0]}.")

#4.feladat:
bolygonev = input("Írd be a keresett bolygó nevét.")
bolygon = [sor.bolygo for sor in lista if sor.bolygo == bolygonev]
uzenet = "Van " if bolygon else "Nincs "

print(f"{uzenet} ilyen bolygo.")

#5.feladat:
szam = int(input("Adjon meg egy számot."))
tobbhold = [sor.bolygo for sor in lista if int(sor.holdjai) > szam]
print(f"A következő bolygóknak van {szam}-nál több holdja")
print(tobbhold)



