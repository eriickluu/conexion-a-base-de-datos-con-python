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

def create_tables():
    if Store.table_exists():
        Store.drop_table()

    if User.table_exists():
        User.drop_table()

    User.create_table()
    Store.create_table()

if __name__ == '__main__':
    # create_tables()

    # user = User.create(username='prueba', password='prueba', email='prueba@prueba.com')
    # store1 = Store.create(name='tienda 1', address='Ninguna', user=user)
    # store2 = Store.create(name='tienda 2', address='Ninguna', user=user)

    # user = User.get(User.id==1)
    # print(user)

    # for store in user.stores:
    #     print(store)

    store1 = Store.get(Store.id == 1)
    print(store1.user)