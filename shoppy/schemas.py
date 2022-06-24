from datetime import datetime
from enum import Enum
from typing import List, Optional, Any, Dict
from uuid import UUID

from orjson import orjson
from pydantic import BaseModel


def orjson_dumps(v, *, default):
    # orjson.dumps returns bytes, to match standard json.dumps we need to decode
    return orjson.dumps(v, default=default).decode()


class BaseWithConfig(BaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


class ProductQuantity(BaseModel):
    min: int
    max: int


class ProductEmailOut(BaseModel):
    enabled: bool


class ProductOut(BaseWithConfig):
    id: str
    attachment_id: Optional[str]
    title: str
    description: Optional[str]
    image: Optional[str]
    unlisted: Optional[bool]
    type: str
    price: int
    currency: str
    email: Optional[ProductEmailOut]
    stock_warning: Optional[int]
    quantity: Optional[ProductQuantity]
    confirmations: Optional[int]
    gateways: List[str]
    webhook_urls: Optional[List[str]]
    dynamic_url: Optional[str]
    position: Optional[int]
    created_at: datetime
    updated_at: datetime
    seller: Optional[str]
    stock: int
    accounts: Optional[List[Dict[str, UUID]]]
    product_link: Optional[str]


class ProductType(Enum):
    SERVICE = "service"
    FILE = "file"
    ACCOUNT = "account"
    DYNAMIC = "dynamic"


class ProductIn(BaseWithConfig):
    title: str
    price: int
    currency: str
    unlisted: Optional[bool]
    description: Optional[str]
    type: ProductType
    stock_warning: Optional[int]
    email: ProductEmailOut
    quantity: ProductQuantity
    confirmations: Optional[int]
    attachment_id: Optional[str]
    custom_fields: Optional[List[str]]
    webhook_urls: Optional[List[str]]
    dynamic_url: Optional[str]
    gateways: Optional[List[str]]
    accounts: Optional[List[str]]


class FeedbackOut(BaseWithConfig):
    id: UUID
    order_id: UUID
    comment: str
    stars: int
    rating: int
    response: Optional[Any]
    created_at: datetime
    updated_at: datetime
    product: Optional[Any]


class QueryReply(BaseModel):
    message: str


class QueryAgent(BaseModel):
    ip: str
    iso_code: str
    country: str
    city: str
    state: str
    state_name: str
    postal_code: str


class QueryGeo(BaseModel):
    geo = QueryAgent


class QueryOut(BaseWithConfig):
    id: str
    status: int
    subject: str
    email: str
    message: str
    created_at: datetime
    updated_at: datetime
    replies: Optional[List[QueryReply]]
    agent: QueryGeo


class OrderOut(BaseWithConfig):
    id: UUID
    pay_id: Optional[UUID]
    product_id: str
    coupon_id: Optional[str]
    price: int
    currency: str
    exchange_rate: Optional[int]
    email: Optional[str]
    delivered: Optional[int]
    confirmations: Optional[int]
    required_confirmations: Optional[int]
    transaction_id: Optional[str]
    crypto_address: Optional[str]
    crypto_amount: Optional[str]
    shipping_address: Optional[str]
    quantity: Optional[int]
    gateway: Optional[str]
    custom_fields: Optional[Dict[str, str]]
    refund_id: Optional[str]
    is_replacement: Optional[bool]
    replacement_id: Optional[str]
    paid_at: Optional[datetime]
    disputed_at: Optional[datetime]
    created_at: datetime
    is_partial: Optional[bool]
    crypto_received: Optional[bool]
    webhooks: Optional[List[str]]
    accounts: Any
    coupon: Optional[List[str]]
    product: Optional[ProductOut]
