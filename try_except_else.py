# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit():
#         yosh = int(yosh)
#         break
#     else:
#         print("Butun son kiriting")
# print(f"Siz {2023-yosh} yilda tug'ilgansiz")

# x,y=5,10
# try:
#    print(y/(x-5))
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")

# mevalar = ['olma','anor','anjir','uzum']
# try:
#     print(mevalar[3])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")

# user = {"username":"otliq",
#         "status":"admin",
#         "email":"otliq@.ru",
#         "phone":"9999999999"}
#
# while True:
#     key = input("Kalitni kiriting: ")
#     if key in user.keys():
#         print(f'Foydalanuvchi: {user[key]}')
#         break
#     else:
#         print("Bunday kalit mavjud emas")


# while True:
#     filename = input("File nomini shu qorinishta kirting: data.txt")
#     try:
#         with open(filename) as file:
#             text = file.read()
#             break
#     except FileNotFoundError:
#         pass
# print(text)


# while True:
#     n = input("Butun son kiriting: ")
#     if n.isdigit() and n != 0:
#         n = int(n)
#         x=20/n
#         print(f"x={x}")
#         break
#     else:
#         print("Butun son kiritmadingiz yoki 0 kiritdingiz")

