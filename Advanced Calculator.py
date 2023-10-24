# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 20:59:16 2023

@author: PC
"""
class Calculator:
    
    def __init__(self):
        print("welcome to amit calculator\n")
        
    def add(self,*args):
            return sum(args)
        
    def subtract(self,*args):
        result = args[0]
        for num in args[1:]:
            result-=num
        return result
    
    def multiply(self,*args):
        result = 1
        for num in args:
            result*=num
        return result
    
    def divide(self,*args):
        result = args[0]
        for num in args[1:]:
            if num == 0:
                return"cannot divide by zero"
            result /= num
            #result = result / num
        return result
    
    def even_odd(self,num):
        if num%2 == 0:
            return "even"
        else:
            return "odd"
        
    def factorial(self,num):
        if num == 0:
            return 1
        else:
            return num*self.facotial(num-1)
        
    def fibonacci(self,num):
        if num <0:
            return "math error"
        elif num <=1:
            return num
        else:
            return self.fibonacci(num-1) + self.fibonacci(num-2)
        
calc = Calculator()
while True:
    print("please select an operation: ")
    print("1.addition ")
    print("2. subtraction ")
    print("3. multiplication ")
    print("4. division ")
    print("5. even/odd ")
    print("6.factorial ")
    print("7. fibonacci ")

    choice = input("enter your choice (1-7): ")
    if choice in ('1','2','3','4'):
        numbers = [float(num) for num in input("enter number separated by comma:\n").split(",")]
        if choice == "1":
               print("result: ",calc.add(*numbers))
        elif choice == "2":
                print("result: ",calc.subtract(*numbers))
        elif choice == "3":
                print("result: ",calc.multiply(*numbers))
        elif choice == "4":
                print("result: ",calc.divide(*numbers))

        elif choice in ('5','6','7'):
             num = int(input("enter your number: "))
        if choice == "5":
                    print("result: ",calc.even_odd(num))
        elif choice == "6":
                    print("result: ",calc.factorial(num))
        elif choice == "7":
                    print("result: ",calc.fibonacci(num))
        else:
                    print("invalid input")
                    exit = input("do you want to perform another operation? (y/n) ")
                    if exit.lower() != "y":
                        break