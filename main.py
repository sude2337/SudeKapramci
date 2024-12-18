a = int(input("cupcake fiyatı (dolar): "))
b = int(input("cupcake fıyatı (cent): "))
n = int(input("cupcake sayısı: "))

toplam_cent = (a * 100 + b) * n
toplam_dolar = toplam_cent // 100
kalan_cent = toplam_cent % 100

print(toplam_dolar,kalan_cent)
