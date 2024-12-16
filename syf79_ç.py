urun1_fiyat = int(input("Birinci ürünün fiyatını giriniz: "))
urun2_fiyat = int(input("İkinci ürünün fiyatını giriniz: "))

toplam_fiyat = urun1_fiyat + urun2_fiyat

if toplam_fiyat <= 200:
    print("Ödenecek miktar =", toplam_fiyat, "TL")
else:
    indirimli_fiyat = toplam_fiyat * 0.75
    print("Ödenecek miktar, indirimden sonra =", indirimli_fiyat, "TL")
