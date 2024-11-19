from .extension import db

""" CREACION DEL MODELO PARA LA BD EN SQLITE """
class User(db.Model): #Nombre de clase
    id = db.Column(db.Integer, primary_key=True) #columna de la clase
    username = db.Column(db.String(80), unique=True, nullable=False) #columna de la clase
    password = db.Column(db.String(120), unique=False, nullable=False) #columna de la clase
    email = db.Column(db.String(120), unique=True, nullable=False) #columna de la clase
    is_admin = db.Column(db.Boolean, default=False) #columna de la clase
    address = db.Column(db.String(120), unique=False, nullable=True) #columna de la clase
    phone = db.Column(db.String(15), unique=False, nullable=True) #columna de la clase

    def __init__(self, username, password, email, address, phone): #Funcion que valida los datos CONSTRUCTOR
        self.username = username
        self.password = password
        self.email = email
        self.address = address
        self.phone = phone

    def __repr__(self):
        return f"User (Username = {self.username}, email = {self.email}, addres = {self.address}, phone = {self.phone})" #Funcion que muestra los datos del usuario
    

""" CREAION DE LA CLASE DE PRODUCTOS PARA LA BASE DE DATOS EN SQLITE """
class Product(db.Model): #Nombre de clase
    id = db.Column(db.Integer, primary_key=True) #columna de la clase
    name = db.Column(db.String(80), unique=True, nullable=False) #columna de la clase
    price = db.Column(db.Integer, nullable=False) #columna de la clase
    quantity = db.Column(db.Integer, nullable=False) #columna de la clase
    description = db.Column(db.String(120), unique=False, nullable=False) #columna de la clase

    def __init__(self, name, price, quantity, description): #Funcion que valida los datos
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description
    
    def __repr__(self):
        return f"Product (Name = {self.name}, Price = {self.price}, Quantity = {self.quantity}, Description = {self.description})"

""" CREACION DE LA CLASE DE ORDENES PARA BD EN SQLITE """
class Order(db.Model): #Nombre de clase
    id = db.Column(db.Integer, primary_key=True) #columna de la clase
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False) #columna de la clase
    quantity = db.Column(db.Integer, nullable=False) #columna de la clase
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #columna de la clase

    def __init__(self, product_id, quantity, user_id): #Funcion que valida los datos
        self.product_id = product_id
        self.quantity = quantity
        self.user_id = user_id

    def __repr__(self):
        return f"Order (Product ID = {self.product_id}, Quantity = {self.quantity}, User ID = {self.user_id})"
    
""" CREACION DE LA RELACION ENTRE PRODCUTOS Y ORDEN PARA BD EN SQLITE """
class OrderProduct(db.Model): #Nombre de clase
    id = db.Column(db.Integer, primary_key=True) #columna de la clase
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False) #columna de la clase
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False) #columna de la clase
    quantity = db.Column(db.Integer, nullable=False) #columna de la clase

    def __init__(self, order_id, product_id, quantity): #Funcion que valida los datos
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
    def __repr__(self):
        return f"OrderProduct (Order ID = {self.order_id}, Product ID = {self.product_id}, Quantity = {self.quantity})"

