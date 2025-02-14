# Strategy Pattern - Payment Processor 💳🔄

## 📌 Introduction
The **Strategy Pattern** is a **behavioral design pattern** that allows defining a family of algorithms, encapsulating each one, and making them interchangeable dynamically. This model promotes extensibility and modularity by avoiding multiple conditional structures (`if-else` or `switch-case`).

In this project, we apply the **Strategy Pattern** to a **payment processor**, allowing different payment methods to be accepted flexibly.

---

## 📁 Project Structure
```
📦 payment_processor_project
├── 📜 main.py  # Entry point of the application
├── 📂 payment_processor  # Package containing the Strategy Pattern implementation
│   ├── 📜 concretestrategy.py  # Implements different payment strategies
│   ├── 📜 payment_processor.py  # Manages the execution of the selected strategy
│   ├── 📜 PaymentStrategy.py  # Strategy interface
```

---

## 🏗️ Component Explanation

1. **`PaymentStrategy.py`** (Strategy Interface)  
   - Defines a common interface for all payment strategies.

2. **`concretestrategy.py`** (Concrete Strategies)  
   - Implements different payment methods, such as **Credit Card, PayPal, and Cryptocurrency**.

3. **`payment_processor.py`** (Context)  
   - Contains a reference to a payment strategy and executes the processing based on the selected strategy.

4. **`main.py`** (Entry Point)  
   - Allows the user to select a payment method and execute it.

---

## 🛠️ Running the Project
### 1️⃣ Prerequisites
Ensure you have **Python 3.x** installed.

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Example Usage (`main.py`)
```python
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
```

---

## 🎯 Advantages of the Strategy Pattern
✅ **Reduces conditional complexity**  
✅ **Easy extensibility**: Adding a new payment method is simple.  
✅ **Code reusability**: Strategies can be reused independently.  

---

## 📜 License
This project is open-source and available under the **MIT License**.

<p align="center"><b>Happy Coding! 🎄✨</b></p>
