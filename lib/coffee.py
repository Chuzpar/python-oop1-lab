#!/usr/bin/env python3

class Coffee:
    def __init__(self, type, price):
        self.type = type
        self.price = price
    @property
    def size(self):
        return self.size
    @size.setter
    def size(self, new_size):
        if type(new_size) == str and new_size in ["Small", "Medium", "Large"]:
            self.size = new_size
        else:
            print("size MUst be Small, Medium, or Large")
    
    def tip(self, amount):
        if type(amount) == int and amount > 0:
            print(f"This coffee is great! Here's a tip of ${amount}.")
        else:
            print("Tip amount must be a positive integer")
    pass