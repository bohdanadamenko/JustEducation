class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def how_match(self):
        q = 1
        for_one_m = 25
        how_match_kg = self.length * self.width * q * for_one_m
        print(f'Нужно {how_match_kg}кг асфальта для покрытия дороги длинной {self.length}м. '
              f'и шириной {self.width}м.')
        return how_match_kg

how = Road(10, 3).how_match()
print(how)