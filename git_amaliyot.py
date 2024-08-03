"""“raqamlar” nomli tekst fayl ichiga 1 dan 10 gacha 
sonlarni kiritib, ularning yig'indisini ekranga 
chiqaruvchi dastur yarating."""

#faylga yozish
try:
    with open("raqamlar.txt", "w") as fayl:
        fayl.write("1 2 3 4 5 6 7 8 9 10")
except FileNotFoundError:
    print("Fayl ochishda xatolik!")

#fayldan o'qish
try:
    with open("raqamlar.txt", "r") as fayl:
        mylist = fayl.read().split()
        mylist2 = list(map(lambda x: int(x), mylist))
        result = sum(mylist2)
except FileNotFoundError:
    print("Fayl ochishda xatolik!")
#demo uchun ushbu comment qo'shildi
print(result)
