class Thermostat:
    def __init__(self):
        self.temperature = 20

    def set_temperature(self, new_temp):
        if isinstance(new_temp, int) or isinstance(new_temp, float):
            self.temperature = new_temp
        else:
            raise ValueError('Температура должна быть числом')

    def get_temperature(self):
        return self.temperature


class Door:
    def __init__(self):
        self.is_opened = False

    def open_door(self):
        self.is_opened = True

    def close_door(self):
        self.is_opened = False

    def is_door_opened(self):
        return self.is_opened


class LightBulb:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def is_light_on(self):
        return self.is_on


class SmartHouse:
    def __init__(self):
        # Создаем объекты устройств внутри класса
        self.thermostat = Thermostat()
        self.door = Door()
        self.light_bulb = LightBulb()

    def control_thermostat(self, temperature=None):
        # Изменяет температуру термостата
        if temperature is not None:
            self.thermostat.set_temperature(temperature)
        print(f'Температура установлена на {self.thermostat.get_temperature()} градусов.')

    def control_door(self, action='open'):
        # Открывает/закрывает дверь
        if action.lower() == 'open':
            self.door.open_door()
            print('Дверь открыта.')
        elif action.lower() == 'close':
            self.door.close_door()
            print('Дверь закрыта.')
        else:
            print('Действие не распознано.')

    def control_light(self, state=True):
        # Включает/выключает свет
        if state:
            self.light_bulb.turn_on()
            print('Свет включен.')
        else:
            self.light_bulb.turn_off()
            print('Свет выключен.')


house = SmartHouse()
house.control_thermostat(25)
house.control_door('open')
house.control_light(True)