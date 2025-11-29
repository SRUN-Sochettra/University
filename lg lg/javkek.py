# class Rectangle:
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width
        
#     def __str__(self):
#         return f'Rectangle: {self.height} x {self.width}'

#     def area(self):
#         return self.height * self.width

#     def perimeter(self):
#         return 2 * (self.height + self.width)
    
# rec1 = Rectangle(3, 2)
# rec2 = Rectangle(5, 4)

# print(rec1.area())
# print(rec2.area())
# print(rec1.perimeter())
# print(rec2.perimeter())

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance

#     def withdraw(self, amount):
#         if amount < self.balance:
#             self.balance -= amount
#         elif amount > self.balance:
#             print("Insufficient funds")

#     def display_balance(self):
#         print(f'Owner: {self.owner}, Balance: {self.balance}$')

# p1 = BankAccount("Alice", 1000)
# p1.display_balance()
# p1.deposit(500)
# p1.display_balance()
# p1.withdraw(200)
# p1.display_balance()
# print(p1.withdraw(1500))

# class ParentClass:
#     def feature_1(self):
#         print("Feature 1 from Parent Class")
        
#     def feature_2(self):
#         print("Feature 2 from Parent Class")
        
# class ChildClass(ParentClass):
#     def feature_3(self):
#         print("Feature 3 from Child Class")

# a = ChildClass()
# a.feature_1()
# a.feature_2()
# a.feature_3()

# class SavingAccount(BankAccount):
#     def __init__(self, owner, balance=0, interest_rate=0.02):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate
#     def add_interest(self):
#         interest = self.balance * self.interest_rate
#         self.balance += interest
#         print(f'Interest Added: {interest}, New Balance: {self.balance}$')
        
# acc1 = SavingAccount("Bob", 1000)
# acc1.display_balance()
# acc1.withdraw(200)
# acc1.display_balance()
# acc1.add_interest()
# acc1.add_interest()
# acc1.add_interest()

# class ParentClass:
#     def feature_1(self):
#         print("Feature 1 from Parent Class")

# class ChildClass_1(ParentClass):
#     def feature_2(self):
#         print("Feature 2 from Child Class 1")
        
# class ChildClass_2(ParentClass):
#     def feature_3(self):
#         print("Feature 3 from Child Class 2")
        
# a = ChildClass_1()
# b = ChildClass_2()
# a.feature_1()
# b.feature_1()

# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("Moving!")
#     def fuel_type(self):
#         print("Fuel type: Gasoline")
        
# class Car(Vehicle):
#     pass

# class Boat(Vehicle):
#     def move(self):
#         print("Sailing!")
#     def fuel_type(self):
#         print("Fuel type: Diesel")

# class Plane(Vehicle):
#     def move(self):
#         print("Flying!")
#     def fuel_type(self):
#         print("Fuel type: Jet Fuel")

# car1 = Car("Toyota", "Corolla")
# boat1 = Boat("Yamaha", "242X")
# plane1 = Plane("Boeing", "747")

# for x in (car1, boat1, plane1):
#     print(x.brand)
#     print(x.model)
#     x.fuel_type()
#     x.move()

# class SimpleIterator:
#     def __init__(self,data):
#         self.data = data
#         self.index = 0
#     def get_next(self):
#         if self.index < len(self.data):
#             item = self.data[self.index]
#             self.index += 1
#             return item

# it = SimpleIterator([10,20,30])
# print(it.get_next())
# print(it.get_next())
# print(it.get_next())

import kek

# kek.welcome("Alice")
# print(kek.add(5, 10))
# print(kek.sub(10, 5))
# print(kek.mul(5, 10))
# print(kek.div(10, 5))
# print(kek.vowel_count("Apple"))
# print(kek.consonant_count("Apple"))
# print(kek.reverse_string("Apple"))
# p = kek.person1['name']
# print(p)
# print(kek.vowel_count(p))

# import datetime

# now = datetime.datetime.now()
# print('Current date and time:', now)

# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print('Formatted date:', formatted_date)

# future_date = now + datetime.timedelta(days=30)
# print("Date after 30 days:", future_date.strftime("%Y-%m-%d %H:%M:%S"))

# if now.weekday() >= 5:
#     print("It's the weekend!")
# else:
#     print("It's a weekday.")

# import camelcase
# c= camelcase.CamelCase()
# txt= "hello world"
# print(c.hump(txt))

a = [30,20,60,10,40,50]
a.sort()
print(a)