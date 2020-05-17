from pymongo import MongoClient

client = MongoClient() #localhost 27017

db = client['minicurso_python']

if __name__ == '__main__':
    user1 = {'username': 'codigofacilito1', 'password': 'password123', 'age' : 23}
    user2 = {'username': 'codigofacilito2', 'password': 'password123', 'age' : 24}
    user3 = {'username': 'codigofacilito3', 'password': 'password123', 'age' : 25}
    user4 = {'username': 'codigofacilito4', 'password': 'password123', 'age' : 26}

    # db.users.insert(user1)
    # db.users.insert_many(user1, user2, user3)

    result = db.users.insert_one(user4)
    print(result.inserted_id)
