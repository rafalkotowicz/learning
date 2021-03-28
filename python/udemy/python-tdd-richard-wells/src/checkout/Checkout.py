class Checkout:
    class Discount:
        def __init__(self, no_of_items, discount_price):
            self.no_of_items = no_of_items
            self.discount_price = discount_price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def add_item_with_price(self, item, price):
        self.prices[item] = price

    def add_item_to_cart(self, item):
        if item not in self.prices:
            raise Exception("Unknown item: " + item)

        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def add_discount(self, item, no_of_items, discount_price):
        discount = self.Discount(no_of_items, discount_price)
        self.discounts[item] = discount

    def calculate_total(self):
        total = 0
        for item, count in self.items.items():
            total += self.calculate_item_price(item, count)
        return total

    def calculate_item_price(self, item, count):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if count >= discount.no_of_items:
                total += self.calculate_discounted_item_total(count, discount, item)
            else:
                total += self.prices[item] * count
        else:
            total += self.prices[item] * count
        return total

    def calculate_discounted_item_total(self, count, discount, item):
        total = 0
        no_of_discounts = count / discount.no_of_items
        total += no_of_discounts * discount.discount_price
        remaining = count % discount.no_of_items
        total += remaining * self.prices[item]
        return total
