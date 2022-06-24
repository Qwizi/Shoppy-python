from shoppy.mixins import ListMixin, RetrieveMixin
from shoppy.schemas import ProductOut, FeedbackOut, QueryOut, OrderOut


class ResourceClient:
    endpoint = None

    def __init__(self, api_url: str, headers: dict[str]):
        self.api_url = api_url
        self.headers = headers


class ProductResource(ResourceClient, ListMixin):
    schema = ProductOut
    endpoint = "/v1/products/"


class FeedbackResource(ResourceClient, ListMixin):
    schema = FeedbackOut
    endpoint = "/v1/feedbacks/"


class QueriesResource(ResourceClient, ListMixin, RetrieveMixin):
    schema = QueryOut
    endpoint = "/v1/queries/"


class OrderResource(ResourceClient, ListMixin):
    schema = OrderOut
    endpoint = "/v1/orders/"
