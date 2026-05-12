class Urun:
    def __init__(self, ad, fiyat, stok):
        self.ad = ad
        self.fiyat = fiyat
        self.stok = stok

    def bilgi_goster(self):
        print(f"Ürün Adı: {self.ad}")
        print(f"Fiyat: {self.fiyat} TL")
        print(f"Stok: {self.stok}")
        print("-" * 25)


urunler = []


while True:

    print("\n--- MARKET STOK SİSTEMİ ---")
    print("1- Ürün Ekle")
    print("2- Ürünleri Listele")
    print("3- Ürün Sat")
    print("4- Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":

        ad = input("Ürün adı: ")
        fiyat = float(input("Ürün fiyatı: "))
        stok = int(input("Stok adedi: "))

        yeni_urun = Urun(ad, fiyat, stok)
        urunler.append(yeni_urun)

        print("Ürün başarıyla eklendi.")

    elif secim == "2":

        if len(urunler) == 0:
            print("Henüz ürün eklenmedi.")

        else:
            for urun in urunler:
                urun.bilgi_goster()

    elif secim == "3":

        satilacak_urun = input("Satılacak ürün adı: ")

        bulundu = False

        for urun in urunler:

            if urun.ad.lower() == satilacak_urun.lower():

                bulundu = True

                adet = int(input("Satılacak adet: "))

                if adet <= urun.stok:

                    urun.stok -= adet

                    kazanc = adet * urun.fiyat

                    print("Satış başarılı.")
                    print(f"Kazanç: {kazanc} TL")
                    print(f"Kalan stok: {urun.stok}")

                else:
                    print("Yeterli stok yok.")

        if bulundu == False:
            print("Ürün bulunamadı.")

    elif secim == "4":

        print("Program kapatıldı.")
        break

    else:
        print("Geçersiz seçim yaptınız.")
