class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nChildren: {self.children}")

    def calm_child(self, child):
        child.is_calm = True

    def feed_child(self, child):
        child.is_hungry = False

class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_calm = False
        self.is_hungry = True


parent = Parent('Alex', 35)
child1 = Child('Milena', 10)
child2 = Child('Emilia', 12)
child3 = Child('Nare', 11)
children = [child1, child2, child3]

for child in children:
    if parent.age - child.age >= 16:
        parent.children.append(child)
# print(parent.children)

for child in parent.children:
    if child.is_hungry:
        parent.feed_child(child)
        print(child.is_hungry)

for child in parent.children:
    if not child.is_calm:
        parent.calm_child(child)
        print(child.is_calm)


