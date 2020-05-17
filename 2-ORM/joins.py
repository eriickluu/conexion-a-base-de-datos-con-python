import peewee 
import datetime

HOST = 'localhost'
USER = 'root'
PASSWORD = 'toor'
DATABASE = 'minicurso_python'

database = peewee.MySQLDatabase(DATABASE, host=HOST, port=3306, user=USER, passwd=PASSWORD)

class User(peewee.Model):
    username = peewee.CharField(unique=True, max_length=50, index=True)
    password = peewee.CharField(max_length=50, null=True)
    email = peewee.CharField(max_length=50)
    active = peewee.BooleanField(default=True)
    created_date = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        db_table = 'users'

    def __str__(self):
        return self.username

class Store(peewee.Model):
    user = peewee.ForeignKeyField(User, related_name='stores')
    name = peewee.CharField(max_length=50)
    address = peewee.TextField()
    active = peewee.BooleanField(default=True)
    created_date = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        db_table = 'stores'

    def __str__(self):
        return self.name

class Product(peewee.Model):
    name = peewee.CharField(max_length=100)
    description = peewee.TextField()
    store = peewee.ForeignKeyField(Store, related_name='products')
    price = peewee.DecimalField(max_digits=5, decimal_places=2)
    stock = peewee.IntegerField()
    created_date = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        db_table = 'products'

    def __str__(self):
        return '{name} - ${price}'.format(name=self.name, price=self.price)

def create_tables():
    if Product.table_exists():
        Product.drop_table()

    if Store.table_exists():
        Store.drop_table()

    if User.table_exists():
        User.drop_table()

    User.create_table()
    Store.create_table()
    Product.create_table()

def insert_users():
    User.create(username='prueba', password='prueba', email='prueba@prueba.com')
    User.create(username='prueba2', password='prueba2', email='prueba2@prueba.com')

def insert_stores():
    Store.create(user_id=1, name='tienda facilita uno', address='Oficinas')
    Store.create(user_id=2, name='tienda facilita dos', address='Oficinas')

def insert_products():
    Product.create(store_id=1, name='Pan', description='Pan integral', price=5.5, stock=50)
    Product.create(store_id=1, name='Leche', description='Baja en gradas', price=15.5, stock=100)
    Product.create(store_id=1, name='Jamon', description='de pavo', price=30.9, stock=80)

    Product.create(store_id=2, name='Soda', description='Dieta', price=10.0, stock=50)
    Product.create(store_id=2, name='Fritura', description='Frituras de papa', price=20.5, stock=100)
    Product.create(store_id=2, name='Salsa', description='chile habanero', price=29, stock=80)

def create_shema():
    create_tables()
    insert_users()
    insert_stores()
    insert_products()

if __name__ == '__main__':
    query = (
        Product.select()
        .join(Store)
        .join(User)
        .where(User.id == 1)
        .order_by(Product.price.desc())
    )

    for product in query:
        print(product)
 