from payment_processor.payement_processor import paymentprocessor
from payment_processor.ConcreteStrategy import creditcard,bitcoin,PayPalPayment


creditcardmethod = creditcard("156746317863214856") 
bitcoinmethod = bitcoin("231653412318954162165465456456465")
PayPalPaymentmethod = PayPalPayment("ahmed123@gmail.com")

client = paymentprocessor(creditcardmethod)
client.processpayment(100)
client.set_strategy(bitcoinmethod)
client.processpayment(500)
client.set_strategy(PayPalPaymentmethod)
client.processpayment(1000)