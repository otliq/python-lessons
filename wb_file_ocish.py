import pickle
with open('yozib_boruvchi_fayl',"rb") as file:
    fayl = pickle.load(file)

print(fayl)