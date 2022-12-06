import re
szoveg="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
#1
print("Karakterek száma: ",len(szoveg))

#2
mondat=re.split(r'[.!?]+', szoveg)
print("Mondatok száma: ",len(mondat))

#3
#for lorem in szoveg:


#4
Lszam=[]
Lbetuk=[]
for szam in szoveg:
    if(szam.isalpha()):
        Lbetuk.append(szam)
    elif(szam.isalnum()):
        Lszam.append(int(szam))

print("Számok: ",Lszam)


#for szam in szoveg:
#    if(szam.isalnum()):
#        Lszam.append(int(szam))
#        print("Számok: ", Lszam)
#    else:
#        print("A szövegben nincsenek betük: ")

#5
#print("Szeretnél keresni a szövegben?")
#keres=input("Ha igen írd be azt a szót amit keresel: ")
#if keres in szoveg:
#    print("A szó előfordulásain száma: ", len(keres))





