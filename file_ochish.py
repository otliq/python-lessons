import pickle

with open("pi_million_digits.txt","r") as file:
    pi = file.read()
    pi = pi.rstrip().replace('\n','')

def pi_ichida(raqam):
    """pi soni ichiga raqamni kirishini tekshiradi"""
    print(raqam in pi)

# print(pi_ichida(str(151515)))


with open('wb_pi','wb') as file:
    pickle.dump(pi,file)