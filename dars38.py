import datetime as dt
import re

# Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani konsolga chiqaring
today = dt.date.today()
two_weeks = dt.timedelta(weeks=2)
twa_day = today + two_weeks

# i = 0
# while i<=10:
#     twa_day += dt.timedelta(days=1)
#     print(twa_day)
#     i += 1

# Ramazon va qurbon hayitigacha qolgan kunlarni konsolga chiqaring
ramazon_day = dt.date(2023,3,23)
qurbon_day = dt.date(2023,6,28)
delta_r = ramazon_day - today
delta_q = qurbon_day - today

# print(f"Ramazon ga cha: {delta_r.days} kun qoldi!")
# print(f"Qurbon Hayit bayramigacha: {delta_q.days} kun qoldi!")


# Tug'ilgan kuningizdan bugungi sanagacha qancha yil, oy,
# kun o'tganini qaytaruvchi funksiya yozing

def get_live_time(birthday):

    delta_year = today.year - birthday.year
    delta_days = today - birthday
    delta_month = delta_year * 12
    print(f"Siz tugilgan kundan hozirgacha: {delta_year}-yil, {delta_month}-oy, {delta_days.days}-kun otdi.")

bd = dt.date(2003,9,14)
# get_live_time(bd)

# Foydalanuvchidan telefon raqamini kiritishni so'rang. Kiritlgan qiymatni andoza yordamida tekshiring
# while True:
#     phone_number = input("Enter phone number")
#     andoza = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
#     if re.match(andoza, phone_number):
#         break

# Berilgan matndan veb sahifa manzilini ajratib olyuvchi funksiya yozing.
# Quyidagi matndan namuna sifatida foydalanishingiz mumkin:


txt = "Assalom alaykum hurmatli dostlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni organamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"

def get_web(text):
    andoza = " https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*) "
    #!!! regular expression does not works in code, but wors in ihateregex.io
    web_site = re.findall(andoza, text)
    print(web_site)
# get_web(txt)
