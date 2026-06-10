#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size in ["Small", "Medium", "Large"]:
            self._size = size
        else:
            raise ValueError("size must be Small, Medium, or Large")

    def tip(self):
        print("This coffee is great, here's a tip!")
        self.price += 1


if __name__ == "__main__":
    input_size = input("What size of coffee would you like? (small/medium/large): \n ").capitalize()
    input_price = input("Enter the price of your coffee: ")

    coffee = Coffee(input_size, float(input_price))
    print(f"Your coffee order is: \n {coffee.size} - {coffee.price}")
    coffee.tip()
    print(f"New price after tip: {coffee.price}")