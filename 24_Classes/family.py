class Family:
    def __init__(self, surname, money):
        self.surname = surname
        self.money = money
        self.have_a_house = False

    def buy_house(self, house_price, discount=0):
        house_price -= house_price * discount / 100
        if self.money >= house_price:
            self.money -= house_price
            self.have_a_house = True
            print(f'House purchased! Current money: {self.money}')
        else:
            print('Not enough money!')

    def earn_money(self, amount):
        self.money += amount
        print(f'Earned money: {amount}\tCurrent money: {self.money}')


family = Family(surname='Voskanian', money=10000)
print('Try to buy house!')
family.buy_house(10 ** 6)

while not family.have_a_house:
    family.earn_money(10 ** 4)
    print('Again try!!!')
    family.buy_house(10 ** 6, discount=10)
