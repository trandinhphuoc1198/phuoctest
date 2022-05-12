from dataclasses import dataclass
from abc import ABC,abstractclassmethod
class paymethod(ABC):
    @abstractclassmethod
    def pay_value(self) -> int:
        pass
@dataclass
class byVisa(paymethod):
    def pay_value(self)-> int:
        return 0.5
@dataclass
class byCash(paymethod):
    def pay_value(self)-> int:
        return 3
@dataclass
class Payment:
    amount:int
    method: paymethod
    def pay_amout(self):
        return self.amount*self.method.pay_value()

a=Payment(20,byVisa())
