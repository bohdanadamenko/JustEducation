class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title} drowing somthing')


class Pen(Stationery):
    def draw(self):
        print(f'Pen {self.title} drowing somthing')


class Pencil:
    def draw(self):
        print(f'Pencil {self.title} drowing somthing')


class Handle(Stationery):
    def draw(self):
        print(f'Handle {self.title} drowing somthing')

pen = Pen('Chetkiy')
pen.draw()