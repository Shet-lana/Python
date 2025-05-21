# Задание 1
# Создайте класс Device, который содержит информацию об устройстве.
# Спомощью механизма наследования, реализуйте класс
# CoffeeMachine (содержит информацию о кофемашине),
# класс Blender (содержит информацию о блендере), класс
# MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые для работы методы.

class Device:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def turn_on(self):
        print(f"{self.name} включен.")

    def turn_off(self):
        print(f"{self.name} выключен.")


class CoffeeMachine(Device):
    def __init__(self, name, power, water_capacity):
        super().__init__(name, power)
        self.water_capacity = water_capacity # (емкость для воды)

    def brew_coffee(self):
        print(f"{self.name} варит кофе.")


class Blender(Device):
    def __init__(self, name, power, blending_speed):
        super().__init__(name, power)
        self.blending_speed = blending_speed # (скорость смешивания)

    def blend(self):
        print(f"{self.name} смешивает ингредиенты.")


class MeatGrinder(Device):
    def __init__(self, name, power, grinding_speed):
        super().__init__(name, power)
        self.grinding_speed = grinding_speed # (скорость измельчения)

    def grind_meat(self):
        print(f"{self.name} измельчает мясо.")


# Пример использования
coffee_machine = CoffeeMachine("Кофемашина", 1000, 1.5)
blender = Blender("Блендер", 500, 10)
meat_grinder = MeatGrinder("Мясорубка", 800, 8)

coffee_machine.turn_on()
coffee_machine.brew_coffee()
coffee_machine.turn_off()

blender.turn_on()
blender.blend()
blender.turn_off()

meat_grinder.turn_on()
meat_grinder.grind_meat()
meat_grinder.turn_off()
