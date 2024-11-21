from .extension import db
from datetime import datetime

# CREACION DEL MODELO PARA LA BD EN SQLITE
class UserModel(db.Model):
    __tablename__ = 'user'  # Especificamos el nombre de la tabla
    idUser = db.Column(db.Integer, primary_key=True)  # Renombré 'idUser' como identificador único
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=True)
    phone = db.Column(db.String(15), unique=False, nullable=True)
    role = db.Column(db.String(20), default='Employee', nullable=False)  # campo para el rol

    def __init__(self, username, password, email, address, phone, role):
        self.username = username
        self.password = password
        self.email = email
        self.address = address
        self.phone = phone
        self.role = role

    def __repr__(self):
        return f"User (Username = {self.username}, email = {self.email}, address = {self.address}, phone = {self.phone}, role = {self.role})"

# CLASE PARA MODELO DE PRODUCTOS
class ProductModel(db.Model):
    __tablename__ = 'product'
    idProduct = db.Column(db.Integer, primary_key=True)  # Renombré 'id' a 'idProduct' para identificar producto
    name = db.Column(db.String(80), unique=True, nullable=False)  # Nombre del producto
    price = db.Column(db.Float, nullable=False)  # Precio del producto
    description = db.Column(db.Text, nullable=False)  # Descripción del producto
    stock = db.Column(db.Integer, nullable=False)  # Stock disponible

    def __init__(self, name, price, description, stock):
        self.name = name
        self.price = price
        self.description = description
        self.stock = stock

    def __repr__(self):
        return f"Product (Name = {self.name}, Price = {self.price}, Description = {self.description}, Stock = {self.stock} )"

# CLASE PARA ORDENES (ENTRE DEPARTAMENTOS)
class OrderModel(db.Model):
    __tablename__ = 'order'
    idOrder = db.Column(db.Integer, primary_key=True)  # Renombré 'id' a 'idOrder'
    user_id = db.Column(db.Integer, db.ForeignKey('user.idUser'), nullable=False)  # Relación con la tabla 'user' usando idUser
    order_date = db.Column(db.DateTime, default=datetime.utcnow)  # Fecha de la orden
    total = db.Column(db.Float, nullable=False)  # Total de la orden
    status = db.Column(db.String(20), default='pending')  # Estado de la orden

    # Relación con la clase User
    user = db.relationship('UserModel', backref='orders')

    def __init__(self, user_id, total, status='pending', order_date=None):
        self.user_id = user_id
        self.total = total
        self.status = status
        self.order_date = order_date if order_date else datetime.utcnow()

    def __repr__(self):
        return f"Order (ID = {self.idOrder}, User ID = {self.user_id}, Total = {self.total}, Status = {self.status})"

# CLASE PARA DEPARTAMENTO
class DepartmentModel(db.Model):
    __tablename__ = 'department'
    idDepartment = db.Column(db.Integer, primary_key=True)  # Renombré 'id' a 'idDepartment'
    nameDepartment = db.Column(db.String(80), unique=True, nullable=False)  # Nombre del departamento
    description = db.Column(db.String(120), nullable=False)  # Descripción del departamento
    user_id = db.Column(db.Integer, db.ForeignKey('user.idUser'), nullable=False)  # Relación con la tabla 'user' usando idUser

    #relacion con la clase UserModel
    user = db.relationship('UserModel', backref='departments', lazy=True)

    def __init__(self, nameDepartment, description, user_id = None):
        self.nameDepartment = nameDepartment
        self.description = description
        self.user_id = user_id

    def __repr__(self):
        return f"Department (Name = {self.nameDepartment}, Description = {self.description}, User ID = {self.user_id})"

# CLASE PARA RELACIONAR ORDENES Y PRODUCTOS
class OrderProductModel(db.Model):
    __tablename__ = 'OrderProduct'
    idOrderProduct = db.Column(db.Integer, primary_key=True)  # Renombré 'id' a 'idOrderProduct'
    order_id = db.Column(db.Integer, db.ForeignKey('order.idOrder'), nullable=False)  # Relación con la tabla 'order'
    product_id = db.Column(db.Integer, db.ForeignKey('product.idProduct'), nullable=False)  # Relación con la tabla 'product'
    quantity = db.Column(db.Integer, nullable=False)  # Cantidad del producto en la orden

    # Relaciones con los modelos Order y Product
    order = db.relationship('OrderModel', backref=db.backref('order_products', lazy=True))
    product = db.relationship('ProductModel', backref=db.backref('order_products', lazy=True))

    def __init__(self, order_id, product_id, quantity):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

    def __repr__(self):
        return f"OrderProduct (Order ID = {self.order_id}, Product ID = {self.product_id}, Quantity = {self.quantity})"
