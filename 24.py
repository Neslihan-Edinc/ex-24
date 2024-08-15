def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):#Eğer sayı 2 veya daha büyükse, bu sayı 2'den başlayarak kendisinden bir eksik olana kadar tüm sayılara bölünür mü diye kontrol eder.
        if num % i == 0:           # range fonksiyonu 0'dan başlayıp stop değerine kadar sayı üretir NUM-1 E KDR
            return False
    return True
# Kullanıcıdan sınır değeri al
limit = int(input("enter a number (Prime numbers up to this number): "))

# 2'den başlayarak sınır değerine kadar olan sayıları kontrol et
print(f"{limit} Prime numbers up to the number:")
for n in range(2, limit + 1):
    if is_prime(n):
        print(n)


