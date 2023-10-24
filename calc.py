# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 20:35:49 2023

@author: PC
"""
class Calculator():
    
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def add(self):
        print(self.x + self.y)
    
    def substract(self):
        print(self.x - self.y)
        
    def multiply(self):
        print(self.x * self.y)
        
    def divide(self):
        print(self.x / self.y)
    
    def even_or_odd(self):
        if (self.x)%2 == 0:
            print("This number is even")
        else:
            print("This number is odd")
        
    def factorial(self):
        fac=1
        for num in range(2 , (self.x) + 1):
            fac *= num
        return fac
    
    def fibo(self):
        if (self.x) == 1:
            return 0
        elif (self.x) == 2:
            return 1
        else:
            return fibo((self.x) - 1)+fibo((self.x) - 2)
        
        

while True:
    print("welcome to the calculator system")

    print("1-add")
    print("2-substract")
    print("3-multiply")
    print("4-divide")
    print("5-check if number is even or odd")
    print("6-factorial")
    print("7-fibonacci")
    print("8-EXIT")
    choice=input("Enter your choice:- \n")
    if choice == "1":
        x=int(input("Enter the first number :\n"))
        y=int(input("Enter the second number :\n"))
        ob=Calculator(x, y)
        ob.add()
    elif choice == "2":
        x=int(input("Enter the first number :\n"))
        y=int(input("Enter the second number :\n"))
        ob=Calculator(x, y)
        ob.substract()
    elif choice == "3":
        x=int(input("Enter the first number :\n"))
        y=int(input("Enter the second number :\n"))
        ob=Calculator(x, y)
        ob.multiply()
    elif choice == "4":
        x=int(input("Enter the first number :\n"))
        y=int(input("Enter the second number :\n"))
        ob=Calculator(x, y)
        ob.divide()
    elif choice == "5":
        x=int(input("Enter the number :\n"))
        y=0
        ob=Calculator(x,y)
        ob.even_or_odd()
    elif choice == "6":
        x=int(input("Enter the number :\n"))
        y=0
        ob=Calculator(x,y)
        res=ob.factorial()
        print(res)
    elif choice == "7":
        x=int(input("Enter the number :\n"))
        y=0
        ob=Calculator(x,y)
        res=ob.fibo()
        print(res)
    elif choice == "8":
        break
