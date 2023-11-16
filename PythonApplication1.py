#1
print("Tere mailm")
nimi=input("Mis on sinu nimi on?")
print("Tere mailm! Tervitan sind{0}!".format(nimi))
vanus=int(input("Kui vana sa oled?"))
print("Tere, maailm! Tervitan sind {0}! aastat vana.".format(nimi, vanus))

#2

vanu=18 #type(vanus) -> int
eesnimi ="Jääk" #type(eesnimi) -> str
pikkus=16.5 #type(pikkkus) -> float
kas_käib_koolis= True #type(kas_käib_koolis) -> bool
#3
candy=int(input("Laual olevate kommide ar:"))
print("Laua peal on{0}".format(candy))
mitu=int(input("Mitu kommi sa soovid süüa:"))
candy-=mitu
print("Nüüd laua peal on {0}".format(candy))

#4
D=float(input("dlinna okruzhnosti "))
print("diametr on {0}".fromat(D/3.14))

#5















print   ("Tere tulemast!".center(50))
kool=input("\tMis koolis sa õpid?: ").capitalize #str Kool
kursus=int(input("\tMis kursusel?: ")) #int kursus

print("Tere tulemast kooli "+kool.upper()+"!\nOle hea"+str(kursus)+".kuursuse õpilaseks!") #kool on KOOl

print("Tere tulemst kooli", kool.lower(),"!\nOle hea",kursus,".kuursuse õpilaseks!") #Kool on kool
print("Tere tulemast kooli {0}!\nOle hea {1}.kuursuse õpetajaks!". format(kool,kursus))#kool on Kool
print(type(kool))
print(type(kursus))
arv1=float(input("Arv 1: "))
arv2=float(input("Arv 2:"))
print(" {0 + {1}={2}".format(arv1,arv2,arv1+arv2)) #summa
print(" {0 - {1}={2}".format(arv1,arv2,arv1-arv2)) #lahutamine
print(" {0 * {1}={2}".format(arv1,arv2,arv1*arv2)) #korrutis
print(" {0 / {1}={2}".format(arv1,arv2,arv1/arv2)) #jagamine
print(" {0 ** {1}={2}".format(arv1,arv2,arv1**arv2)) #astendamine
print(" {0 ja {1} jääk={2}".format(arv1,arv2,arv1%arv2)) #jagamisjääk
print(" {0 ja {1} jagamise täis osa {2}".format(arv1,arv2,arv1//arv2)) #jagamise täis osa

tehe=input("Mida teha: ")
v=eval(str(arv1)+tehe+str(arv2))
print(v)