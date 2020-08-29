from .resource_client import ResourceClient
from .mixins import ListMixin, RetrieveMixin


class OrderResource(ResourceClient, ListMixin, RetrieveMixin):
    endpoint = "/v1/orders/"
