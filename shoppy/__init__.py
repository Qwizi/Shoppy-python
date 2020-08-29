import requests
from .product import ProductResource
from .order import OrderResource
from .feedback import FeedBackResource
from .query import QueryResource


class Shoppy:
    def __init__(self, api_key):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': self.api_key,
            'Content-Type': 'application/json',
            'User-Agent': 'Qwizi App'
        })
        self.product = ProductResource(self.session)
        self.order = OrderResource(self.session)
        self.feedback = FeedBackResource(self.session)
        self.query = QueryResource(self.session)
