# class Person:
#     def __init__(self,name):
#         self.name=name
#     def test(self):
#         print(f"Hello, my name is {self.name}")
# obj1=Person(input())
# obj1.test()

# class Rectangle:
#     def __init__(self,length,width):
#         self.a=length
#         self.b=width
#     def area(self):
#         return self.a*self.b
# obj1=Rectangle(int(input()),int(input()))
# print(obj1.area())

# class Circle:
#     pi=3.14
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return self.pi*self.radius**2
# obj1=Circle(int(input()))
# print(obj1.area())

# class Car:
#     total_cars=0
#     def __init__(self):
#         Car.total_cars+=1
#     @classmethod
#     def total_car_count(cls):
#         return cls.total_cars
# obj1=Car()
# obj2=Car()
# obj3=Car()
# print(Car.total_car_count())