class House:
    def __init__(self, fridge, money):
        self.fridge = fridge
        self.money = money

class Human:
    def __init__(self, name, house):
        self.name = name
        self.satiety = 100
        self.house = house

    def eat(self):
        if self.house.fridge > 10:
            self.satiety += 10
            self.house.fridge -= 5
            print(f"{self.name} ate!")
        else:
            print("Not enough food!")

    def work(self):
        if self.house.money < 100:
            self.satiety -= 10
            self.house.money += 100
            print(f"{self.name} worked 100 $!")
    def shopping(self):
        if self.house.fridge:
            self.house.money -= 100
            self.house.fridge += 50
            print(f"{self.name} went to shopping")
        else:
            print("Insuffient fund!")
            
    def play(self):
        self.satiety -= 10
        print(f"{self.name} played!")

    def isAlive(self):
        if self.satiety > 0:
            return True
        return False
    
    def live(self):
        dice = __import__("random").randint(1,6)
        if dice == 3 and self.satiety < 20:
            self.eat()
        elif dice == 3 and self.house.fridge < 10:
            self.shopping()
        elif dice == 4 and self.house.money  < 50:
            self.work()
        else:
            if dice == 1:
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

    if not human1.isAlive() or not human2.isAlive():
        print("Someone died(")
        break
    print("-" * 30)
