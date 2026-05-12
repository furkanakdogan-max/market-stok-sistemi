class Stock:
    def add_stock(self, product, amount):
        product.stock += amount
        print(f"--- Stok Eklendi ---")
        print(f"{product.name} urunune {amount} adet eklendi. Guncel stok: {product.stock}")

    def reduce_stock(self, product, amount):
        if product.stock >= amount:
            product.stock -= amount
            print("--- Stok Azaltildi ---")
            print("{product.name} urununden {amount} adet cikarildi. Guncel stok: {product.stock}")
        else:
            print("Hata: Yetersiz stok! Mevcut {product.name} stoğu: {product.stock}")

# --- ÇIKTI ALMAK İÇİN GEREKLİ KISIM BURASI ---

# 1. Önce bir ürün sınıfı taklidi yapalım (Product dosyan ayrıysa bu basit hali iş görür)
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

# 2. Deneme verilerini oluşturalım
laptop = Product("Laptop", 15000, 10)
depo = Stock()

# 3. İşlemleri yapalım ve çıktıları görelim
depo.add_stock(laptop, 5)    # 5 tane ekle
depo.reduce_stock(laptop, 3) # 3 tane çıkar
