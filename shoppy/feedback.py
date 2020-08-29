from .resource_client import ResourceClient
from .mixins import ListMixin, RetrieveMixin


class FeedBackResource(ResourceClient, ListMixin, RetrieveMixin):
    endpoint = "/v1/feedbacks/"
