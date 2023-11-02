class Coffee:
    all = []
    
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, "name"):
            self._name = name
        # if not isinstance(name, str):
        #     raise TypeError("Name needs to be of type str")
        # elif not 1 <= len(name) <= 15 :
        #     raise ValueError("Name must have 1 to 15 characters")
        # else:
        #     self._name = name
        
    def orders(self):
        return [orders for orders in Order.all if orders.coffee == self ]
    
    def customers(self):
        return list({orders.customer for orders in self.orders()})
    
    def num_orders(self):
        return len([orders for orders in Order.all if orders.coffee == self])

    def average_price(self):
        total_price = sum([order.price for order in Order.all if order.coffee == self])
        total_orders = len([orders for orders in Order. all if orders.coffee == self])
        if total_orders > 0:
            return total_price / total_orders
        else:
            return 0
        
class Customer:
    all = []
    
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 < len(name) < 15:
            self._name = name
        # if not isinstance(name, str):
        #     raise TypeError("Name needs to be of type str")
        # elif not 1 <= len(name) <= 15 :
        #     raise ValueError("Name must have 1 to 15 characters")
        # else:
        #     self._name = name
        
    def orders(self):
        return [orders for orders in Order.all if orders.customer == self]
    
    def coffees(self):
        return list({orders.coffee for orders in self.orders()})
    
    def create_order(self, coffee, price):
        return Order(customer=self, coffee=coffee, price=price)
    
class Order:
    all = []
    
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, float) and 1 < price < 10 and not hasattr(self, "price"):
            self._price = price
            
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
            
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee