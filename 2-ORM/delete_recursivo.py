import peewee
from models import(User, Store, Product, Category, CategoriesProduct)

def create_tables():
    if CategoriesProduct.table_exists():
        CategoriesProduct.drop_table()

    if Category.table_exists():
        Category.drop_table()

    if Product.table_exists():
        Product.drop_table()

    if Store.table_exists():
        Store.drop_table()

    if User.table_exists():
        User.drop_table()

    User.create_table()
    Store.create_table()
    Product.create_table()
    Category.create_table()
    CategoriesProduct.create_table()

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
    Product.create(store_id=1, name='mayonesa', description='mayonesa', price=30.9, stock=80)

    Product.create(store_id=2, name='Soda', description='Dieta', price=10.0, stock=50)
    Product.create(store_id=2, name='Fritura', description='Frituras de papa', price=20.5, stock=100)
    Product.create(store_id=2, name='Salsa', description='chile habanero', price=29, stock=80)
    Product.create(store_id=2, name='Mostaza', description='Mostaza', price=30.9, stock=80)

def insert_categories():
    Category.create(name='Liquidos', description='liquidos')
    Category.create(name='Embutidos', description='embutidos')
    Category.create(name='Snacks', description='snacks')
    Category.create(name='Aderezos', description='aderezos')
    Category.create(name='Carnes', description='carnes')

def insert_categories_products():
    CategoriesProduct.create(category_id=1, product_id=2) # liquidos ->Leche
    CategoriesProduct.create(category_id=1, product_id=5) # liquidos ->Soda
    CategoriesProduct.create(category_id=1, product_id=7) # liquidos ->Salsa

    CategoriesProduct.create(category_id=2, product_id=3) # liquidos ->jamon

    CategoriesProduct.create(category_id=3, product_id=6) # snacks ->frituras

    CategoriesProduct.create(category_id=4, product_id=4) # aderezos ->mostaza
    CategoriesProduct.create(category_id=4, product_id=8) # aderezos ->mostaza

    CategoriesProduct.create(category_id=5, product_id=3) # aderezos ->mostaza


def create_schema():
    create_tables()
    insert_users()
    insert_stores()
    insert_products()
    insert_categories()
    insert_categories_products()

if __name__ == '__main__':
    create_schema()

    jamon = Product.get(Product.name == 'Jamon')
    
    jamon.delete_instance(recursive=True)