from abc import ABCMeta, abstractmethod
from datetime import datetime


class Vehicle(object):
    __metaclass__ = ABCMeta

    def __init__(self, base_fee):
        self.base_fee = base_fee

    @abstractmethod
    def fee(self, passenger_count):
        pass


class Bus(Vehicle):
    def fee(self, passenger_count):
        return self.base_fee * passenger_count


class Uber(Vehicle):
    def fee(self, passenger_count):
        return self.base_fee * passenger_count * self._premium_rate()

    def _premium_rate(self):
        now = datetime.now()
        return 1 if 0 <= now.hour <= 4 else 1.5


class Taxi(Vehicle):
    pass


if __name__ == '__main__':
    b = Bus(10)
    u = Uber(15)
    t = Taxi(20)

    print('Uber', u.fee(1))
    print('Bus', b.fee(1))
    print('Taxi', t.fee(2))
