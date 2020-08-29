from .resource_client import ResourceClient
from .mixins import ListMixin, CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin


class ProductResource(ResourceClient, ListMixin, CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin):
    endpoint = "/v1/products/"
