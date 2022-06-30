class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def show_speed(self):
        print(f'{self.name} speed now {self.speed}')

    def go(self):
        print(f'car {self.name} going')

    def stop(self):
        print(f'car {self.name} stoping')

    def turn(self, directions):
        print(f'car {self.name} do {directions}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Alert! You speed {self.speed}km/h, its to high')


class SportCar(Car):
    pass


class WorkCar(TownCar):
    pass


class PoliceCar(Car):
    pass


work_car = WorkCar(70, 'Green', 'Mazrda Work', False)
work_car.show_speed()

police = PoliceCar(90, 'Black', 'Opel Patrol', True)
police.turn('right 2 times')
police.stop()