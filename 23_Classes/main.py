# OOP object-oriented programming

class Warrior:
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname
        self.health: int = 100

    def attack(self, enemy):
        enemy.health -= 20

    def is_alive(self):
        return self.health

def game_main_loop(warrior1, warrior2):
    while warrior1.is_alive() and warrior2.is_alive():
        attacker, enemy = __import__('random').sample([warrior1, warrior2], k=2)
        attacker.attack(enemy)
        print(f"{enemy.nickname} has been attacked {attacker.nickname}")
        print(f"{warrior1.health} | {warrior2.health}")
        __import__('time').sleep(3)

    print(f"Winner: {warrior1.nickname if warrior1.is_alive() else warrior2.nickname}")


def main():
    warrior1 = Warrior(nickname='Subzero')
    warrior2 = Warrior(nickname='Scorpion')
    game_main_loop(warrior1, warrior2)


if __name__ == '__main__':
    main()