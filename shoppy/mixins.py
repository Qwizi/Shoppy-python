import asyncio
import json
from enum import Enum
from typing import Coroutine, Callable, Any, Optional, List
from uuid import UUID

import httpx
from httpx import URL
from pydantic import BaseModel

CALLABLE = Callable[..., Coroutine[Any, Any, BaseModel]]
CALLABLE_LIST = Callable[..., Coroutine[Any, Any, List[Optional[BaseModel]]]]


class RequestMethodEnum(Enum):
    GET = "get"
    POST = "post"
    PUT = "put"
    DELETE = "delete"


class BaseMixin:
    api_url: str
    headers: dict[str]
    endpoint: str
    schema: BaseModel

    async def make_request(self, method: RequestMethodEnum, **kwargs):
        async with httpx.AsyncClient(base_url=self.api_url, headers=self.headers) as c:
            if method == RequestMethodEnum.GET:
                page = kwargs.get("page", None)
                obj_id = kwargs.get("obj_id", None)
                url = self.endpoint
                if page:
                    url = f"{self.endpoint}?page={page}"
                if obj_id:
                    url = f"{self.endpoint}{obj_id}"
                resp = await c.get(url)
                data = resp.json()
                return resp, data
            elif method == RequestMethodEnum.POST:
                schema = kwargs.get("schema", None)
                obj_id = kwargs.get("obj_id", None)
                url = self.endpoint
                if obj_id:
                    url = f"{self.endpoint}{obj_id}"
                resp = await c.post(url, json=schema.json())
                data = resp.json()
                return resp, data
            elif method == RequestMethodEnum.DELETE:
                obj_id = kwargs.get("obj_id", None)
                url = f"{self.endpoint}{obj_id}"
                resp = await c.delete(url)
                data = resp.json()
                return resp, data
            elif method == RequestMethodEnum.PUT:
                schema = kwargs.get("schema", None)
                url = self.endpoint
                resp = await c.put(url, json=schema.json())
                data = resp.json()
                return resp, data


class ListMixin(BaseMixin):

    async def __parse_obj(self, url: URL, item):
        path = url.path
        if "products" in path:
            item["product_link"] = f"https://shoppy.gg/product/{item['id']}"
        obj = self.schema.parse_obj(item)
        return obj

    async def list(self, page=None) -> CALLABLE_LIST:
        resp, data = await self.make_request(method=RequestMethodEnum.GET, page=page)
        items = await asyncio.gather(*[self.__parse_obj(resp.url, i) for i in data])
        return items


class CreateMixin(BaseMixin):
    async def create(self, schema: BaseModel) -> CALLABLE:
        async with httpx.AsyncClient(base_url=self.api_url, headers=self.headers) as client:
            url = self.endpoint
            print(url)
            resp = await client.put(url, json=schema.json())
            print(resp.text)
            # model = self.schema.parse_obj(resp.json())
            return resp


class RetrieveMixin(BaseMixin):
    async def retrieve(self, obj_id: str) -> CALLABLE:
        resp, data = await self.make_request(RequestMethodEnum.GET, obj_id=obj_id)
        print(resp.url)
        if resp.status_code != 200:
            raise Exception("Object not found")
        return self.schema.parse_obj(data)


class UpdateMixin(BaseMixin):
    async def update(self, obj_id: UUID, updated_data):
        async with httpx.AsyncClient(base_url=self.api_url, headers=self.headers) as client:
            return client.post(f"{self.endpoint}/{obj_id}", data=json.dumps(updated_data))


class DeleteMixin(BaseMixin):
    async def delete(self, obj_id: UUID):
        async with httpx.AsyncClient(base_url=self.api_url, headers=self.headers) as client:
            return client.delete(f"{self.endpoint}/{obj_id}")
