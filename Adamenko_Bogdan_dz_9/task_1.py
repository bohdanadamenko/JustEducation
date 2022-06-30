import time
import itertools

class TrafficLight:
    def __init__(self):
        self.__color = (('Red', 7), ('Yellow', 2), ('Green', 3))

    def running(self):
        for color, sec in itertools.cycle(self.__color):
            print(f'Now its {color} Light for {sec}')
            time.sleep(sec)

sf = TrafficLight().running()