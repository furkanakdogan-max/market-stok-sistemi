class Sale:

    def sell_product(self, product, amount):

        if product.stock >= amount:

            total_price = product.price * amount
            product.stock -= amount

            print("\nSatış başarılı.")
            print(f"Toplam Tutar: {total_price} TL")

        else:
            print("Yeterli stok yok!")
