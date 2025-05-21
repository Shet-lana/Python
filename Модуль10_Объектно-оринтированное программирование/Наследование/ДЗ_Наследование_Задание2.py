# Задание 2
# Создайте класс Ship, который содержит информацию о корабле.
# С помощью механизма наследования, реализуйте класс Frigate
# (содержит информацию о фрегате), класс Destroyer (содержит информацию об эсминце),
# класс Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые для работы методы.

class Ship:
    def __init__(self, name, displacement):
        self.name = name
        self.displacement = displacement

    def sail(self):
        print(f"{self.name} плывет.")

    def anchor(self):
        print(f"{self.name} стоит на якоре.")


class Frigate(Ship):
    def __init__(self, name, displacement, armament):
        super().__init__(name, displacement)
        self.armament = armament

    def fire(self):
        print(f"{self.name} ведет огонь из {self.armament}.")


class Destroyer(Ship):
    def __init__(self, name, displacement, speed):
        super().__init__(name, displacement)
        self.speed = speed

    def patrol(self):
        print(f"{self.name} патрулирует на скорости {self.speed} узлов.")


class Cruiser(Ship):
    def __init__(self, name, displacement, range):
        super().__init__(name, displacement)
        self.range = range

    def long_range_mission(self):
        print(f"{self.name} выполняет дальнюю миссию на расстояние {self.range} миль.")


# Пример использования
frigate = Frigate("Фрегат", 5000, "пушки")
destroyer = Destroyer("Эсминец", 8000, 30)
cruiser = Cruiser("Крейсер", 12000, 5000)

frigate.sail()
frigate.fire()
frigate.anchor()

destroyer.sail()
destroyer.patrol()
destroyer.anchor()

cruiser.sail()
cruiser.long_range_mission()
cruiser.anchor()
