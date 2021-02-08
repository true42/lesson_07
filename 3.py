class Cell:
    def __init__(self, count_cell):
        if count_cell > 0:
            self.count_cell = count_cell
        else:
            print("Число клеток должно быть больше 0!")

    def __add__(self, other):
        return Cell(self.count_cell + other.count_cell)

    def __sub__(self, other):
        if self.count_cell - other.count_cell > 0:
            return Cell(self.count_cell - other.count_cell)
        else:
            return "Нельзя вычесть больше клеток, чем есть."

    def __mul__(self, other):
        return Cell(self.count_cell * other.count_cell)

    def __truediv__(self, other):
        return Cell(round(self.count_cell / other.count_cell))

    def make_order(self, cells):
        star = ''
        for i in range(self.count_cell//cells):
            star += (cells * '*') + '\n'
        if self.count_cell % cells > 0:
            star += (self.count_cell % cells) * '*' + '\n'
        return star


x = Cell(25)
y = Cell(12)
a = x*y
b = x+y
c = x/y
d = x-y
print(x.make_order(10))
print(y.make_order(6))
print(a.make_order(100))
print(b.make_order(10))
print(c.make_order(1))
print(d.make_order(5))
