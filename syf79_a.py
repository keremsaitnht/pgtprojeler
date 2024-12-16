sinav1 = int(input("Birinci sınav notunu giriniz: "))
sinav2 = int(input("İkinci sınav notunu giriniz: "))
performans = int(input("Performans notunu giriniz: "))

ortalama = (sinav1 + sinav2 + performans) / 3

if ortalama >= 50:
    print("Başarılı!")
else:
    print("Başarısız!")
