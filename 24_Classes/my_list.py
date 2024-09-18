class MyList:
    def __init__(self):
        self.zambyux = []

    def avelacnel(self, elem):
        self.zambyux += [elem]

    def __str__(self):
        return "<<" + ', '.join(self.zambyux) + '>>'

l = MyList()
l.avelacnel('a')
l.avelacnel('b')
l.avelacnel('c')
l.avelacnel('c')

print(l)