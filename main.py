class product:
    def __init__(self, name, price, deal_price, rating):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.rating = rating
        self.you_save = price - deal_price

    def display_product_details(self):
        print("Name : {}".format(self.name))
        print("Price : {}".format(self.price))
        print("Deal Price : {}".format(self.deal_price))
        print("Rating : {}".format(self.rating))
        print("You Save : {}".format(self.you_save))

    def get_deal_price(self):
        return self.deal_price


class electronic_item(product):
    def __init__(self, name, price, deal_price, rating, warrenty, color):
        super().__init__(name, price, deal_price, rating)
        self.warrenty = warrenty
        self.color = color

    def display_product_details(self):
        super().display_product_details()
        print("Warrenty : {}".format(self.warrenty))
        print("Color : {}".format(self.color))


class grocery_item(product):
    def __init__(self, name, price, deal_price, rating, expiry_date):
        super().__init__(name, price, deal_price, rating)
        self.expiry_date = expiry_date

    def display_product_details(self):
        super().display_product_details()
        print("Expiry Date : {}".format(self.expiry_date))


class clothing_item(product):
    def __init__(self, name, price, deal_price, rating, color, size, brand):
        super().__init__(name, price, deal_price, rating)
        self.color = color
        self.size = size
        self.brand = brand

    def display_product_details(self):
        super().display_product_details()
        print("Color : {}".format(self.color))
        print("Size : {}".format(self.size))
        print("Brand : {}".format(self.brand))


class clothing_item2(clothing_item):
    def __init__(self, name, price, deal_price, rating, color, size, brand, length):
        super().__init__(name, price, deal_price, rating, color, size, brand)
        self.length = length

    def display_product_details(self):
        super().display_product_details()
        print("Length : {}".format(self.length))


class order:
    delivery_charges = {
        "prime": 100,
        "normal": 0
    }

    def __init__(self, delivery_address, delivery_speed):
        self.items = []
        self.delivery_address = delivery_address
        self.delivery_speed = delivery_speed

    def add_items(self, product, quantity):
        self.items.append((product, quantity))

    def display_order_details(self):
        print("E-Mart Store")
        print("Deliver Address : {}".format(self.delivery_address))
        print("Delivery Speed : {}".format(self.delivery_speed))
        print("Products List")
        print("----------------------------------")
        for product, quantity in self.items:
            product.display_product_details()
            print("Quantity : {}".format(quantity))
            print("")
        print("----------------------------------")
        total_bill = self.get_total_bill()
        print("Total Bill : {}".format(total_bill))
        print("----------------------------------")
        print(" ")

    def get_total_bill(self):
        total_bill = 0
        for product, quantity in self.items:
            total_bill += product.get_deal_price() * quantity
        ordered_total_bill = order.delivery_charges[self.delivery_speed]
        total_bill += ordered_total_bill
        return total_bill

    @classmethod
    def update_delivery_charges(cls, new_charges):
        cls.delivery_charges = new_charges


class cart:
    def greet():
        print("*** Thank You for Visiting ***")


e = electronic_item("Sony Tv", 100000, 75000, 4.3, "2 Years", "Black")
g = grocery_item("Bread", 50, 30, 4.9, "Nov 2024")
c = clothing_item("Casual Shirt", 1500, 1000, 4.4, "Sky Blue", "L", "Raymond")
c2 = clothing_item2("Jeans", 2500, 2000, 4.8, "Black", 34, "Allen Solly", 41.5)
x = order("Hyderabad", "prime")
x.add_items(e, 1)
x.add_items(g, 2)
x.add_items(c, 1)
x.add_items(c2, 1)
x.display_order_details()
cart.greet()