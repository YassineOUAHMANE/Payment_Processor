from .PaymentStrategy import PaymentStrategy
class bitcoin(PaymentStrategy):
    def __init__(self,walletnumber:str):
        self.walletnumber = walletnumber
    
    def pay(self,amount:float):
        print(f"paid  ${amount:.2f} using  wallet account : {self.walletnumber}.")

class creditcard(PaymentStrategy):
    def __init__(self,creditcardnumber:str):
        self.cardnumber = creditcardnumber
    
    def pay(self,amount:float):
        print(f"paid ${amount:.2f} using creditcard account : {self.cardnumber}.")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float):
        print(f"Paid ${amount:.2f} using PayPal account : {self.email}.")

