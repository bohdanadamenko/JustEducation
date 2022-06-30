class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    def __str__(self):
        return f'about {self.name}'

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{self._income["wage"] + self._income["bonus"]}$'


petro = Position('Petro', 'Deltoro', 'Smoker',{"wage": 1000, "bonus": 116})

print(petro.get_full_name())
print(petro.get_total_income())

