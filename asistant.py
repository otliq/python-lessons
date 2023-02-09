
while True:
    text = input("Dardingizni aytvering yozyapman. [Boldi] deguningizcha")
    if text.lower()=="boldi": break
    with open('yozib_boruvchi_fayl','a') as file:
        file.writelines(text)


