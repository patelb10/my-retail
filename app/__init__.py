"""This is init module."""

from flask import Flask
#from app import product_routes
import logging

#from app import errors

# Place where app is defined


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('app')

app = Flask(__name__)

from app import product_routes