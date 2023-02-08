from uuid import uuid4

class Avto:
    """Avtomobil klassi"""
    __num_avto = 0
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobil hususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self,km):
        """Mashinaning km ga yana km qo'shish"""
        if km >=0:
            self.__km += km
        else:
            print("Kilometerni qaytarib bolmaydi")
    @classmethod
    def get_num_avto(cls):
        return Avto.__num_avto
avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)

print(Avto.get_num_avto())