class House:
    def __init__(self, fridge, money):
        self.fridge = fridge
        self.money = money

class Human:
    def __init__(self, name, house):
        self.name = name
        self.satiety = 50
        self.house = house

    def eat(self):
        if self.house.fridge:
            self.satiety += 10
            self.house.fridge -= 5
            print(f"{self.name} ate!")
        else:
            print("Not enough food!")
        #     if self.house.money:
        #         self.work()

    def work(self):
        #if self.house.money < 100:
            self.satiety -= 10
            self.house.money += 10
            print(f"{self.name} worked 100 $!")


    def shopping(self):
        if self.house.fridge < 10:
            self.house.money -= 100
            self.house.fridge += 50
            print(f"{self.name} went to shopping")
        else:
            print("Insufficient fund!")
            
    def play(self):
        self.satiety -= 10
        print(f"{self.name} played!")

    def isAlive(self):
        return self.satiety
    
    def live(self):
        dice = __import__('random').randint(1, 6)

        if self.satiety < 20:
            self.eat()
        elif self.house.fridge < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play()

house = House(50, 0)
human1 = Human("Milena", house)
human2 = Human("Emilik", house)

for day in range(1, 366):
    print(f"DAY{day}:")
    human1.live()
    human2.live()

    if not human1.isAlive() :
        print(f"{human1.name} died")
        break
    if not human2.isAlive():
        print(f"{human2.name} died")
        break
    print("-" * 30)
