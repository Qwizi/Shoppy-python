import requests
import simplejson as json


class ResourceClient:
    endpoint = None
    api_url = "https://shoppy.gg/api"

    def __init__(self, session):
        self.session = session



class List:
    def list(self):
        return self.session.get(f"{self.api_url}{self.endpoint}")


class Create:
    def create(self, data):
        return self.session.put(f"{self.api_url}{self.endpoint}", data=json.dumps(data))


class Retrieve:
    def retrieve(self, obj_id):
        return self.session.get(f"{self.api_url}{self.endpoint}{obj_id}/")


class Update:
    def update(self, obj_id, updated_data):
        return self.session.post(f"{self.api_url}{self.endpoint}{obj_id}/", data=json.dumps(updated_data))


class Delete:
    def delete(self, obj_id):
        return self.session.delete(f"{self.api_url}{self.endpoint}{obj_id}/")


class Product(ResourceClient, List, Create, Retrieve, Update, Delete):
    endpoint = "/v1/products/"


class Order(ResourceClient, List, Retrieve):
    endpoint = "/v1/orders/"


class FeedBack(ResourceClient, List, Retrieve):
    endpoint = "/v1/feedbacks/"


class Query(ResourceClient, List, Retrieve, Update):
    endpoint = "/v1/queries/"

    def reply(self, query_id, message):
        return self.session.post(f"{self.endpoint}{query_id}/", data=json.dumps({'message': message}))


class Shoppy:
    def __init__(self, api_key):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': self.api_key,
            'Content-Type': 'application/json',
            'User-Agent': 'Qwizi App'
        })
        self.product = Product(self.session)
        self.order = Order(self.session)
        self.feedback = FeedBack(self.session)
        self.query = Query(self.session)
