"""
Задача 5. Совместное проживание
Что нужно сделать
Чтобы понять, стоит ли ему жить с кем-то или лучше остаться в гордом одиночестве, Артём решил провести необычное исследование. Для этого он реализовал модель человека и модель дома.

Человек может (должны быть такие методы):

есть (+ сытость, − еда);
работать (− сытость, + деньги);
играть (− сытость);
ходить в магазин за едой (+ еда, − деньги);
прожить один день (выбирает одно действие согласно описанному ниже приоритету и выполняет его).
У человека есть (должны быть такие атрибуты):

имя,
степень сытости (изначально 50),
дом.
В доме есть:

холодильник с едой (изначально 50 еды),
тумбочка с деньгами (изначально 0 денег).
Если сытость человека становится меньше нуля, человек умирает.

Логика действий человека определяется следующим образом:

Генерируется число кубика от 1 до 6.
Если сытость < 20, то нужно поесть.
Иначе, если еды в доме < 10, то сходить в магазин.
Иначе, если денег в доме < 50, то работать.
Иначе, если кубик равен 1, то работать.
Иначе, если кубик равен 2, то поесть.
Иначе играть.
По такой логике эксперимента человеку надо прожить 365 дней.

Реализуйте такую программу и создайте двух людей, живущих в одном доме. Проверьте работу программы несколько раз.
"""


class House:
    def __init__(self):
        self.fridge = 50
        self.money = 0


class Human:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.satiety = 50

    def eat(self):
        if self.house.fridge:
            self.satiety += 10
            self.house.fridge -= 10


    def earn_money(self):
        self.satiety -= 10
        self.house.money += 100

    def play(self):
        self.satiety -= 10

    def shopping(self):
        if self.house.money:
            self.house.money -= 100
            self.house.fridge += 10

    def live_one_day(self):
        dice = __import__('random').randint(1, 6)

        if self.satiety < 20:
            self.eat()
        elif self.house.fridge < 10:
            self.shopping()
        elif self.house.money < 50:
            self.earn_money()
        elif dice == 1:
            self.earn_money()
        elif dice == 2:
            self.eat()
        else:
            self.play()


if __name__ == '__main__':
    house = House()
    human1 = Human('Artem', house)
    human2 = Human('Anna', house)

    for _ in range(365):
        human1.live_one_day()
        human2.live_one_day()

        if human1.satiety <= 0 or human2.satiety <= 0:
            print('Game Over!')
            break




