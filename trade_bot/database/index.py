from pymongo import MongoClient


class DB(self):
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
