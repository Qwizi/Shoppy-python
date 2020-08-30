import simplejson as json


class ListMixin:
    def list(self, page=None):
        if page is not None:
            return self.session.get(f"{self.api_url}{self.endpoint}/?page={page}")
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
