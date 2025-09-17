'''we can create functions within classes. We can create our own methods within the classes too
then we call the method and run it
the first argument within the method inside the class is self'''

class BankAccount:
  def __init__(self,first_name,last_name,account_id,account_type,pin,balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance

  def deposit(self, amount):
    self.balance = self.balance + amount

  def withdraw(self, amount):
    self.balance = self.balance - amount


  def display_balance(self):
    print('Your current balance is', '$',self.balance)

mike = BankAccount('Mike','Smith',12345,'Checking',1234,0)

mike.deposit(96)
mike.withdraw(25)
mike.display_balance()
  
