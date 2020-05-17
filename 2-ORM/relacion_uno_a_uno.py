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
    user = peewee.ForeignKeyField(User, primary_key=True)
    name = peewee.CharField(max_length=50)
    address = peewee.TextField()
    active = peewee.BooleanField(default=True)
    created_date = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        db_table = 'stores'

    def __str__(self):
        return self.name

if __name__ == '__main__':
    # if Store.table_exists():
    #     Store.drop_table()

    # if User.table_exists():
    #     User.drop_table()

    # User.create_table()
    # Store.create_table()

    # user = User.create(username='prueba', password='prueba', email='prueba@prueba.com')
    # store = Store.create(name='tienda facilita', address='sin direccion', user=user)
    # store = Store.create(name='tienda facilita', address='sin direccion', user_id=1)

    tienda_facil = Store.get(Store.user_id == 1)
    print(tienda_facil)
    print(tienda_facil.user)
    print(tienda_facil.user.password)