from app import app
from app import logger
from app.mongo_handler import MongoHandler
from app import error_handler


if __name__ == '__main__':
    # Running app in debug mode
    mongo_handler = MongoHandler()
    mongo_handler.load_product_data()
    app.run(host="0.0.0.0", debug=True)