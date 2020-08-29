import requests
import simplejson as json


class ListMixin:
    def list(self):
        return self.session.get(f"{self.api_url}{self.endpoint}")


class CreateMixin:
    def create(self, data):
        return self.session.put(f"{self.api_url}{self.endpoint}", data=json.dumps(data))


class RetrieveMixin:
    def retrieve(self, obj_id):
        return self.session.get(f"{self.api_url}{self.endpoint}{obj_id}/")


class UpdateMixin:
    def update(self, obj_id, updated_data):
        return self.session.post(f"{self.api_url}{self.endpoint}{obj_id}/", data=json.dumps(updated_data))


class DeleteMixin:
    def delete(self, obj_id):
        return self.session.delete(f"{self.api_url}{self.endpoint}{obj_id}/")


class ResourceClient:
    endpoint = None
    api_url = "https://shoppy.gg/api"

    def __init__(self, session):
        self.session = session


class ProductResource(ResourceClient, ListMixin, CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin):
    endpoint = "/v1/products/"


class OrderResource(ResourceClient, ListMixin, RetrieveMixin):
    endpoint = "/v1/orders/"


class FeedBackResource(ResourceClient, ListMixin, RetrieveMixin):
    endpoint = "/v1/feedbacks/"


class QueryResource(ResourceClient, ListMixin, RetrieveMixin):
    endpoint = "/v1/queries/"
    STATUS = ('close', 'reopen')

    def reply(self, query_id, message):
        return self.session.post(f"{self.endpoint}{query_id}/", data=json.dumps({'message': message}))

    def update(self, obj_id, updated_data, action):
        return self.session.post(f"{self.api_url}{self.endpoint}{obj_id}/{action}", data=json.dumps(updated_data))


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
