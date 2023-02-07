import random

print('SON TOPISH OYINIGA HUSH KELIBSIZ!')


def son_top(son=10):
    taxmin_men = 0
    os_pc = random.randint(1, son)
    print(f"1 dan {son} gacha son oyladim.'\nTopa olasizmi?")
    while True:
        taxmin_men += 1
        kson = int(input(">>>"))
        if kson > os_pc:
            print(f"Men oylagan son {kson} dan kichikrog")
        elif kson < os_pc:
            print(f"Men oylagan son {kson} dan kattarog")
        else:
            print(f"TOPTINGIZ\n{taxmin_men} ta taxmin bilan.")
            return  taxmin_men
            break

def son_top_pc(son):
    taxmin_pc = 0
    input(f"1 dan {son} ga cha son oylang va istalgan tugmani bosing \nmen topishga harakat qilaman")
    n_gran = 1
    v_gran = son
    while True:
        taxmin_pc += 1
        if n_gran != v_gran:
            guess = random.randint(n_gran,v_gran)
        else:
            guess = n_gran
        answer = input(f"Siz {guess} sonini oyladingiz: togri - [h]\n kattarog - [+] kichikrog -[-]".lower())
        if answer == "-":
            v_gran = guess - 1
        elif answer == "+":
            n_gran = guess + 1
        else:
            break
    print(f"{taxmin_pc} taxmin bilan TOPDIM")
    return taxmin_pc

def play(x=10):
    replay = True
    while replay:
        taxminlar_user = son_top(x)
        taxminlar_pc = son_top_pc(x)

        if taxminlar_user < taxminlar_pc:
            print(f"Tabriklayman siz {taxminlar_user} taxmin bilan YUTDINGIZ!!")
        elif taxminlar_pc < taxminlar_user:
            print(f"Men {taxminlar_pc} taxmin bilan yutdim!")
        else:
                print("DURRANG")
        replay = int(input("Yana oynaysizmi?: Ha[1]   Yoq[0]"))

play()