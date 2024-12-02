# SF_Almacen_y_Gestion
Este proyecto permite gestionar usuarios, productos, órdenes y departamentos dentro de una aplicación con base de datos SQLite. Cada entidad tiene sus correspondientes relaciones y atributos que facilitan la administración y el registro de las operaciones comerciales.

# DESCRIPCIÓN:  
  El sistema es una plataforma que permite gestionar usuarios y sus órdenes. Los usuarios pueden tener productos y estar asignados a departamentos. Las órdenes pueden incluir productos específicos, y cada orden tiene un total y un estado que puede ser "pendiente", "procesado", etc.
La aplicación gestiona usuarios, productos y órdenes con las siguientes características:

  - Usuarios: La tabla user almacena la información del usuario (nombre, correo, dirección, teléfono, etc.), con un campo adicional para el rol del usuario (empleado o administrador).
  - Productos: La tabla product permite gestionar los productos disponibles (nombre, precio, descripción, stock).
  - Órdenes: La tabla order gestiona las órdenes realizadas por los usuarios, con su respectivo total, fecha y estado (pendiente, procesada, etc.).
  - Departamentos: La tabla department define los departamentos dentro de la empresa y su relación con los usuarios.
  - Relación Órdenes y Productos: La tabla OrderProduct relaciona productos con órdenes específicas y la cantidad de cada producto.

  # Instalación

    Clona el repositorio: git clone https://github.com/Rodri0701/SF_Almacen.git


# Crea un entorno virtual (opcional):

    python3 -m venv venv
    source venv/bin/activate  # En Linux/macOS
    venv\Scripts\activate     # En Windows

# Instala las dependencias:

Asegúrate de tener pip actualizado e instala las librerías necesarias:

    pip install -r requirements.txt

El archivo requirements.txt debe incluir las siguientes dependencias:

  - Flask==2.0.3
  - Flask-SQLAlchemy==2.5.1

# Configura la base de datos:

Asegúrate de que extension.py (donde se configura db) esté correctamente configurado. El archivo debe tener lo siguiente:

  - from flask_sqlalchemy import SQLAlchemy
  - db = SQLAlchemy()

Luego, inicializa la base de datos en tu aplicación:

  - from extension import db

# Crea las tablas en la base de datos
db.create_all()

Ejecuta la aplicación:

    flask run

Estructura de la Base de Datos

Las siguientes tablas están presentes en la base de datos:

  user: Almacena usuarios (idUser, username, password, email, address, phone, role).
  product: Almacena productos (idProduct, name, price, description, stock).
  order: Almacena órdenes (idOrder, user_id, order_date, total, status).
  department: Almacena departamentos (idDepartment, nameDepartment, description, user_id).
  OrderProduct: Relaciona productos con órdenes (idOrderProduct, order_id, product_id, quantity).

# Uso

  Crear un usuario: Utiliza el modelo UserModel para crear un usuario en la base de datos.

  Agregar productos: Puedes añadir productos mediante el modelo ProductModel.

  Realizar una orden: Usa el modelo OrderModel para crear órdenes, asociando productos con OrderProductModel.

