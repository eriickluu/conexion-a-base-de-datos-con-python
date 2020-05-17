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

if __name__ == '__main__':
    # user = User.get(User.id == 1)
    # print(user)

    # users = User.select(User.username, User.password).where((User.id > 3) and (User.password == 'password')).get()
    # print(users.username)

    # user = User.select().where( User.email >> None ).get()
    # print(user)

    # users = ['Erick', 'Erick2']
    # users = User.select().where( User.username << users )
    # for user in users:
    #     print(user)

    # users = User.select().where( User.username.contains('Erick'))
    # for user in users:
    #     print(user)

    # users = User.select().where( User.username.startswith('A'))
    # for user in users:
    #     print(user)

    users = User.select().where( User.username.endswith('2'))
    for user in users:
        print(user)

    #  user = user[0]

    #  for user in users:
    #      print(user)

