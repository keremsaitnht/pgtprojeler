bagaj_agirligi = float(input("Bagajınızın ağırlığını kilogram cinsinden giriniz: "))

bagaj_agirligi = int(bagaj_agirligi)

if bagaj_agirligi <= 20:
    print("Herhangi bir ücret ödemeniz gerekmiyor.")
else:
    fazla_bagaj = bagaj_agirligi - 20
    ek_ucret = fazla_bagaj * 10
    print("Fazla bagaj için", ek_ucret, "TL ödemelisiniz.")
