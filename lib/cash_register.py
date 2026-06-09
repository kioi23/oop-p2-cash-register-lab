#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.items.extend([item] * quantity)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity,
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total * (100 - self.discount) / 100
        if isinstance(self.total, float) and self.total.is_integer():
            total_value = int(self.total)
        else:
            total_value = round(self.total, 2)

        self.total = total_value
        print(f"After the discount, the total comes to ${total_value}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last_transaction = self.previous_transactions.pop()
        amount = last_transaction["price"] * last_transaction["quantity"]
        self.total -= amount
        if self.total == -0.0:
            self.total = 0.0

        for _ in range(last_transaction["quantity"]):
            for index in range(len(self.items) - 1, -1, -1):
                if self.items[index] == last_transaction["item"]:
                    del self.items[index]
                    break

        if self.total < 0:
            self.total = 0.0
