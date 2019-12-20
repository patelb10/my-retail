from app.mongo_handler  import MongoHandler
from urllib.parse import urljoin
import requests
from collections import OrderedDict
from copy import deepcopy
import json
from app.error_handler import ProductNotFound, ExternalAPINotFound,  InvalidRequestError, ProductNotUpdated
import jsonschema

class ProductService(object):
    def __init__(self):
        self.external_url = "https://redsky.target.com/v2/pdp/tcin/"
        self.exclude_string = "taxonomy,price,promotion,bulk_ship,rating_and_review_reviews,rating_and_review_statistics,question_answer_statistics"
        self.mongo_handler = MongoHandler()

    def get_product(self, id):
            product = self.mongo_handler.find_product_by_id(id)
            if not product:
                raise ProductNotFound("test")
            # take out object_id from document
            product.pop('_id')
            external_data = {}
            try:
                url = urljoin(self.external_url, str(id)) + "?excludes={}".format(self.exclude_string)
                result = requests.get(url)
                external_data = result.json()
            except Exception:
                ExternalAPINotFound()
            try:
                item_title = external_data["product"]["item"]["product_description"]["title"]
            except KeyError:
                item_title = None
            if item_title:
                product["name"] = item_title
            #arrange document in order
            data_order = ('id', 'name', 'current_price')
            ordered_product_data = OrderedDict(
                (k, product[k]) for k in data_order)
            return ordered_product_data

    def save_product(self, id, product):
        #validate parameters
        try:
            schema = {
                "type": "object",
                "properties" : {
                    "id" : {
                    "type": "number"
                    },
                    "current_price": {
                    "type": "object",
                    "properties" : {
                        "currency_code" : {"type" : "string"},
                        "value" : {"type" : "number"},
                         },
                    "required": [
                    "currency_code",
                    "value"
                    ]
                    }
                },
            }
            jsonschema.validate(product, schema)
        except jsonschema.ValidationError:
            raise  InvalidRequestError()
        product_valid = self.mongo_handler.find_product_by_id(id)
        if not product_valid:
            raise ProductNotFound()
        update_product = self.mongo_handler.update_product(id, product)
        if not update_product:
            raise ProductNotUpdated()
        return product
