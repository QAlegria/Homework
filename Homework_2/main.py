# Задача 2. ООП:
#
# Создайте класс Vehicle с методами start_engine() и stop_engine().
#
# Создайте дочерние классы Car и Motorcycle, переопределите методы.
#

class Vehicle:
    def __init__(self, name):
        self.name = name

    def start_engine(self):
        raise NotImplementedError('Должен быть определен в дочернем классе')

    def stop_engine(self):
        raise NotImplementedError('Должен быть определен в дочернем классе')

class Car(Vehicle):
    def start_engine(self):
        return 'Car started'

    def stop_engine(self):
        return 'Car stopped'

class Motorcycle(Vehicle):
    def start_engine(self):
        return 'Motorcycle started'

    def stop_engine(self):
        return 'Motorcycle stopped'

Audi = Car('Audi')
print(Audi.name, Audi.start_engine(), Audi.stop_engine())

Yamaha = Motorcycle('Yamaha 200')
print(Yamaha.name, Yamaha.start_engine(), Yamaha.stop_engine())