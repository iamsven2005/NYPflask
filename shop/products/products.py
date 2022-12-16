class Product:
    def __init__(self, name, price, discount, stock, desc, brand, category,expenses):
        self.name = name
        self.price = price
        self.discount = discount
        self.stock = stock
        self.desc = desc
        self.brand = brand
        self.category = category
        self.image = ""
        self.expenses = 0
    
    def set_name(self,name):
        self.name = name
    def set_price(self, price):
        self.price = price
    def set_discount(self,discount):
        self.discount = discount
    def set_stock(self, stock):
        self.stock = stock
    def set_desc(self, desc):
        self.desc = desc
    def set_brand(self,brand):
        self.brand = brand
    def set_category(self, category):
        self.category = category
    def set_image(self, image):
        self.image = image
    def set_expenses(self, expenses):
        self.expenses = expenses

    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def get_discount(self):
        return self.discount
    def get_stock(self):
        return self.stock
    def get_desc(self):
        return self.desc 
    def get_brand(self):
        return self.brand
    def get_category(self):
        return self.category
    def get_image(self):
        return self.image
    def get_expenses(self):
        return self.expenses
    