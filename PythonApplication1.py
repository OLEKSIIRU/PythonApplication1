print   ("Tere tulemast!".center(50))
kool=input("\tMis koolis sa õpid?: ") #str kool
kursus=int(input("\tMis kursusel?: ")) #int kursus
print("Tere tulemast kooli "+kool+"!\nOle hea"+str(kursus)+".kuursuse õpilaseks!")
print("Tere tulemst kooli", kool,"!\nOle hea",kursus,".kuursuse õpilaseks!")
print("Tere tulemast kooli {0}!\nOle hea {1}.kuursuse õpetajaks!". format(kool,kursus))
