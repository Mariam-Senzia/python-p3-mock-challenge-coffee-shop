class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or not 3 <= len(name):
            raise Exception("Invalid input")
        if hasattr(self , "_name"):
            raise Exception("Name cannot be changed")
        self._name = name

    def orders(self):
        #list of all orders
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list(set(order.customer for order in self.orders()))
    
    def num_orders(self):
        count = 0
        for order in self.orders():
            if order.coffee == self:
                count += 1
        return count

    def average_price(self):
        total_price = 0
        for order in self.orders():
            total_price += order.price
            
        if self.num_orders() > 0:
            return total_price / self.num_orders()

class Customer:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or not 1 <= len(name) <= 15:
            raise Exception("Invalid input")
        self._name = name

    def orders(self):
        # all customer orders
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set(order.coffee for order in self.orders()))
    
    def create_order(self, coffee, price):
        order1 = Order(self ,coffee , price)
        self.orders().append(order1)
        return order1
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if not isinstance(price, float) or not 1.0 <= price <= 10.0:
            raise Exception("Invalid input")
        if hasattr(self , "_price"):
            raise Exception("Price cannot be changed")
        self._price = price

    def customer(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffee(self):
        return [order for order in Order.all if order.coffee == self]