boy = int(input("Lütfen Boyunuzu Giriniz (CM cinsinden):"))
kilo = int(input("Lütfen Kilonuzu Giriniz:"))

vki = kilo/((boy/100)**2)
print("Vücud Kitle Endeksiniz {}".format(round(vki,2)))

if (vki <= 18.5):
    print("Zayıf")
    print("{} kilogram almanız gerekiyor".format(round(18.5*((boy/100)**2)-kilo,2)))
elif (vki <=24.9):
    print("Normal")
elif (vki<=29.9):
    print("Fazla kilolu")
    print("{} kilogram vermeniz gerekiyor".format(round(kilo-24.9*((boy / 100) ** 2)),2))
elif (vki<=39.9):
    print("Obez")
    print("{} kilogram vermeniz gerekiyor".format(round(kilo - 24.9 * ((boy / 100) ** 2)), 2))
else:
    print("Aşırı obez")
    print("{} kilogram vermeniz gerekiyor".format(round(kilo - 24.9 * ((boy / 100) ** 2)), 2))