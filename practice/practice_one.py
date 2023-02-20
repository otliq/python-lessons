class Man():
    def __init__(self,name):
        self.name = name
        self.fullness = 0
        self.food = 10
        self.money = 0

    def __str__(self):
        return 'Я {}, сытость {}, еды осталось {}, денег осталось {}'.format(self.name,self.fullness,self.food,self.money)

    def eat(self):
        if self.food > 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.food -= 10
        else:
            print('{} нет еды'.format(self.name))

    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.money += 50
        self.fullness -= 10

    def shop(self):
        print('Я сходил в магазин и купил еды!)')
        self.money -= 20
        self.food +=20
man = Man(name="Zoir")
#5min