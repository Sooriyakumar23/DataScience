class Calculator:
    def __init__(self):
        pass
    def add(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return (self.num1 + self.num2)
    def subtract(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return (self.num1 - self.num2)
    def multiply(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return (self.num1 * self.num2)
    def divide(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return (self.num1 / self.num2)
    def print_numbers(self):
        print(f"First Number = {self.num1}, Second Number = {self.num2}")

def is_even_number(num):
    if (num %2 == 0):
        print (f"Yes, {num} is Even")
    else:
        print (f"No, {num} is Old")

def squre_number(num):
    return (num * num)