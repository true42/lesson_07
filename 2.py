class Clothes:

    def __init__(self, name, size, height):
        self.size = size
        self.height = height
        self.name = name

    @property
    def consumption(self):
        pass


class Coat(Clothes):

    def __init__(self, size, name='coat', height =None):
        super().__init__(name, size, height)
        self.size = size
        self.name = name

    def consumption(self):
        return f'Your {self.name} requires {round(self.size / 6.5 + 0.5, 2)} meters of cloth'


class Costume(Clothes):

    def __init__(self, height, name='costume', size =None):
        super().__init__(name, size, height)
        self.size = size
        self.name = name

    def consumption(self):
        return f'Your {self.name} requires {round(self.height * 2 + 0.3, 2)} meters of cloth'


x = Coat(12)
print(x.consumption())
y = Costume(1.86)
print(y.consumption())
