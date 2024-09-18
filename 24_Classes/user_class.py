class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_banned = False
        self.friends = []

    def print_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nBan status: {self.is_banned}")

    def add_friend(self, friend):
        if isinstance(friend, User):
            self.friends.append(friend)

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nBan status: {self.is_banned}"

user1 = User(name='Milena', age=20)
user1.print_info()

user2 = User('Emilia', 16)
user2.print_info()
user2.add_friend(user1)
print(user2.friends)
print(user2)