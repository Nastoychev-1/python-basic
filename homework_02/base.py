from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 2000
    started = False
    fuel = 60
    uel_consumption = 12

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError('Недостаточно топлива для запуска')

    # def move(self, distance: float):
    #     needed_fuel = self.fuel_consumption * distance
    #
    #     if needed_fuel < self.fuel:
    #         print('Поехали!')
    #         self.fuel -= needed_fuel
    #     else:
    #         raise NotEnoughFuel('Не хватает топлива')

    def move(self,distance):
        if self.fuel_consumption * distance <= self.fuel:
            self.fuel -= self.fuel_consumption * distance
        else:
            raise NotEnoughFuel('Не хватает топлива')

