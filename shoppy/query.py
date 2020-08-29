from .resource_client import ResourceClient
from .mixins import ListMixin, RetrieveMixin
import simplejson as json


class QueryResource(ResourceClient, ListMixin, RetrieveMixin):
    endpoint = "/v1/queries/"
    STATUS = ('close', 'reopen')

    def reply(self, query_id, message):
        return self.session.post(f"{self.endpoint}{query_id}/", data=json.dumps({'message': message}))

    def update(self, obj_id, updated_data, action):
        return self.session.post(f"{self.api_url}{self.endpoint}{obj_id}/{action}", data=json.dumps(updated_data))
