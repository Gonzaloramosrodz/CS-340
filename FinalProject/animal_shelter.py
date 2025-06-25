from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username='aacuser', password='SNHU1234'):
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31359
        DB = 'AAC'
        COL = 'animals'
        self.client = MongoClient(f'mongodb://{username}:{password}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        if data:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"Insert failed: {e}")
                return False
        else:
            raise Exception("Data parameter is empty")

    def read(self, query):
        try:
            return list(self.collection.find(query))
        except Exception as e:
            print(f"Read failed: {e}")
            return []

    def read_all(self):
        try:
            return list(self.collection.find())
        except Exception as e:
            print(f"Read all failed: {e}")
            return []
