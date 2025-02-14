from abc import ABC,abstractmethod
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self,amout:float):
        pass