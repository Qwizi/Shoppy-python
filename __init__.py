import requests
import simplejson as json


class Base:
    def __init__(self, api_url, headers):
        self.api_url = api_url
        self.headers = headers
        self.endpoint = ''


class List(Base):
    def list(self):
        return requests.get(self.endpoint, headers=self.headers)


class Create(Base):
    def create(self, data):
        return requests.put(self.endpoint, data=json.dumps(data), headers=self.headers)


class Retrieve(Base):
    def retrieve(self, obj_id):
        return requests.get(f"{self.endpoint}{obj_id}/", headers=self.headers)


class Update(Base):
    def update(self, obj_id, updated_data):
        return requests.post(f"{self.endpoint}{obj_id}/", data=json.dumps(updated_data), headers=self.headers)


class Delete(Base):
    def delete(self, obj_id):
        return requests.delete(f"{self.endpoint}{obj_id}/", headers=self.headers)


class Product(Create, List, Retrieve, Update, Delete):
    def __init__(self, api_url, headers):
        super().__init__(api_url, headers)
        self.endpoint = f"{self.api_url}/v1/products/"


class Order(List, Retrieve):
    def __init__(self, api_url, headers):
        super().__init__(api_url, headers)
        self.endpoint = f"{self.api_url}/v1/orders/"


class FeedBack(List, Retrieve):
    def __init__(self, api_url, headers):
        super().__init__(api_url, headers)
        self.endpoint = f"{self.api_url}/v1/feedbacks/"


class Query(List, Retrieve, Update):
    def __init__(self, api_url, headers):
        super().__init__(api_url, headers)
        self.endpoint = f"{self.api_url}/v1/queries/"

    def reply(self, query_id, message):
        return requests.post(f"{self.endpoint}{query_id}/", data=json.dumps({'message': message}), headers=self.headers)


class Shoppy:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://shoppy.gg/api"
        self.headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json',
            'User-Agent': 'Qwizi App'
        }

        self.product = Product(self.api_url, self.headers)
        self.order = Order(self.api_url, self.headers)
        self.feedback = FeedBack(self.api_url, self.headers)
        self.query = Query(self.api_url, self.headers)
