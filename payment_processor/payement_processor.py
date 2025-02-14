from .PaymentStrategy import PaymentStrategy
class paymentprocessor:
    def __init__(self,strategy:PaymentStrategy):
        self.strategy = strategy
    
    def set_strategy(self,strategy:PaymentStrategy):
        self.strategy = strategy
    
    def processpayment(self,amount:float):
        self.strategy.pay(amount)