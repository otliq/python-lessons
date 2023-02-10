

def get_full_name(name,lastname,surname=""):
    if surname=="":
        return f"{name} {lastname}".title()
    else:
        return f"{lastname} {name} {surname}".title()

def get_biggest(num1,num2,num3):
    return max(num1,num2,num3)


def get_list(list1):
    n = " ".join(list1)
    return f"{n.title()}"

def get_even(sonlar):
    juft_sonlar = []
    for i in sonlar:
        if i % 2 == 0:
            juft_sonlar.append(i)
        else:
            pass
    return juft_sonlar

def check_fibo(num):
    if num <= 0:
        return False
    sequence = [0, 1]
    while len(sequence) <= num:
        next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
        sequence.append(next_value)
    return num in sequence