# Паттерны проектирования — это многократно используемые решения чаcто
# встречающихся проблем разработки программного обеспечения. Они помогают
# организовать код таким образом, чтобы сделать его более гибким, расширяемым и
# удобным для сопровождения.
# Три основных типа паттернов с примерами реализации на Python:

#_________________________ Структурные Паттерны _______________________________________

#### 1. **Adapter** («Адаптер»)
# Задача: Позволяет объектам с разными интерфейсами взаимодействовать друг с другом.
# Реализация: Создаем класс - обертку, который адаптирует один интерфейс к другому.

# Пример использования:

class Dog:
    def bark(self):
        return 'Woof!'


class Cat:
    def meow(self):
        return 'Meow!'


# Адаптер класса Cat к интерфейсу Dog
class CatToDogAdapter(Dog):
    def __init__(self, cat):
        self.cat = cat

    def bark(self):
        # Адаптируем метод meow() кота к интерфейсу собаки
        return f'Cat says {self.cat.meow()}'


cat = Cat()
adapter = CatToDogAdapter(cat)
print(adapter.bark())  # Output: Cat says Meow!

#### 2. **Decorator** («Декоратор**)
# Задача: Динамически добавляет поведение объекту без изменения его исходного кода.
# Реализация: Используем классы - декораторы, обертывающие оригинальный объект и
# предоставляющие дополнительные возможности.

# Пример использования:

from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass


class SimpleCoffee(Coffee):
    def cost(self):
        return 10


class MilkDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 5


simple_coffee = SimpleCoffee()
milk_decorated_coffee = MilkDecorator(simple_coffee)
print(milk_decorated_coffee.cost())  # Output: 15

#### 3. **Composite** («Композит»)
# Задача: Представляет иерархию объектов как единое целое.
# Реализация: Определяем базовый компонент, из которого составляются композитные
# объекты произвольной вложенности.
# Пример использования:

from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def render(self):
        pass


class Leaf(Component):
    def render(self):
        print("Leaf")


class Composite(Component):
    def __init__(self):
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def render(self):
        for child in self.children:
            child.render()


leaf1 = Leaf()
leaf2 = Leaf()
composite = Composite()
composite.add_child(leaf1)
composite.add_child(leaf2)
composite.render()  # Output: Leaf\nLeaf


#____________________________ Поведенческие Паттерны____________________________________

#### 1. **Observer** («Наблюдатель»)
# Задача: Уведомляет зависимые объекты о произошедших изменениях состояния основного
# объекта. Реализация: Объект - наблюдаемый хранит список наблюдателей и уведомляет
# их при изменении своего состояния.

# Пример использования:

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def detach(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            pass

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


class ConcreteObserverA(Observer):
    def update(self, message):
        print(f'A received message: {message}')


subject = Subject()
observer_a = ConcreteObserverA()
subject.attach(observer_a)
subject.notify('Hello')  # Output: A received message: Hello


#### 2. **Strategy** («Стратегия**)
# Задача: Определяет семейство алгоритмов, инкапсулирует каждый алгоритм и делает их
# взаимозаменяемыми.
# Реализация: Реализуется интерфейс стратегии, разные конкретные стратегии реализуют
# этот интерфейс.

# Пример использования:

from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass


class ConcreteStrategyA(Strategy):
    def execute(self):
        return 'Executing strategy A'


class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def do_some_business_logic(self):
        result = self._strategy.execute()
        print(result)


context = Context(ConcreteStrategyA())
context.do_some_business_logic()  # Output: Executing strategy A


#### 3. **Command** («Команда**)
# Задача: Инкапсулирует запрос в виде объекта, позволяя передавать команды
# другим объектам.
# Реализация: Команды становятся объектами, которые имеют общее API и могут
# выполняться различными исполнителями.

# Пример использования:


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


class Light:
    def turn_on(self):
        print('Light is on')

    def turn_off(self):
        print('Light is off')


light = Light()
on_command = LightOnCommand(light)
off_command = LightOffCommand(light)

on_command.execute()  # Output: Light is on
off_command.execute()  # Output: Light is off


#_______________________________ Креативные Паттерны___________________________________

#### 1. **Singleton** («Одиночка**)
# Задача: Обеспечивает наличие единственного экземпляра класса и глобальную точку
# доступа к нему.
# Реализация: Используется специальный конструктор, ограничивающий создание
# экземпляров класса одним объектом.

# Пример использования:


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    def log(self, message):
        print(f'Log: {message}')


logger1 = Logger()
logger2 = Logger()
print(logger1 is logger2)  # Output: True

#### 2. **Factory Method** («Фабричный Метод**)
# Задача: Предоставляет интерфейс для создания объектов, делегируя решение конкретных
# классов производителям объектов.
# Реализация: Базовый класс определяет фабричный метод, а подклассы решают, какой
# именно экземпляр создавать.

# Пример использования:

from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def operation(self):
        pass


class ConcreteProductA(Product):
    def operation(self):
        return 'Result of product A'


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result


class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()


creator = ConcreteCreatorA()
result = creator.some_operation()
print(result)  # Output: Creator: The same creator's code has just worked with Result of product A


#### 3. **Abstract Factory** («Абстрактная Фабрика**)
# Задача: Позволяет создавать семейства связанных или зависящих друг от друга объектов
# без указания их конкретных классов.
# Реализация: Абстрактная фабрика создает группы продуктов, принадлежащих одной семье.

# Пример использования:

from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self):
        pass


class AbstractProductB(ABC):
    @abstractmethod
    def another_useful_function_b(self):
        pass


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self):
        return 'The result of the product A1.'


class ConcreteProductB1(AbstractProductB):
    def another_useful_function_b(self):
        return 'The result of the product B1.'


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()


factory = ConcreteFactory1()
product_a = factory.create_product_a()
product_b = factory.create_product_b()
print(product_a.useful_function_a(), product_b.another_useful_function_b())
# Output: The result of the product A1. The result of the product B1.


# Эти паттерны позволяют строить гибкую архитектуру приложений, уменьшают зависимости
# между модулями и облегчают расширение функционала системы.