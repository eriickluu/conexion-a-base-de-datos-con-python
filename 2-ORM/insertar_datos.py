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

if __name__ == '__main__':
    if User.table_exists():
        User.drop_table()    
    User.create_table()

    # 1
    user = User()
    user.username = 'Erick'
    user.password = 'password'
    user.email = 'erick@codigofacilito.com'
    user.save()

    # 2
    user = User(username='Adrian', password='password', email='adrian@codigofacilito.com')
    user.save()

    # 3
    user = {
        'username': 'Lucio',
        'password': 'password'
    }
    
    user = User(**user)
    user.save()

    # 4
    user = User.create(username='Erick2', password='password', email='erick2@codigofacilito')

    # 5 
    query = User.insert(username='Adrian2', password='password')
    query.execute()