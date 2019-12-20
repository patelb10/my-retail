"""This module is to configure app to connect with database."""
import os
from pymongo import MongoClient
import json
from bson.json_util import dumps
from app import logger
from app.error_handler import ProductNotFound


class MongoHandler(object):
    def __init__(self):
        self.client = MongoClient(os.environ["MONGODB_PORT_27017_TCP_ADDR"], 27017)
        self.db = self.client['appdb']
        self.collection = self.db['products']

    def load_product_data(self):
        logger.info("Loading Initial data to Mongo database")
        with open('data.json') as f:
            data = json.load(f)
        bulk_data = self.collection.initialize_ordered_bulk_op()
        for item in data:
            bulk_data.find({"id": item["id"]}).upsert().update({"$set": item})
        bulk_data.execute()

    def get_all_products(self):
        output = []
        for s in self.collection.find():
            output.append({'id' : s['id'], 'current_price' : s['current_price']})
        return output

    def find_product_by_id(self, id):
        logger.info("Retriving Product information from id : {}".format(id))
        return self.collection.find_one({"id": id})

    def update_product(self, id, product):
        logger.info("Updating Product information of id : {}".format(id))
        try:
            result = self.collection.update_one({"id": id}, {"$set": product}, upsert=True)
            return result.matched_count > 0
        except pymongo.errors.PyMongoError as e:
            return False