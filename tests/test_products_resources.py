from typing import List

import pytest
from faker import Faker

from shoppy.resources import ProductResource
from shoppy.schemas import ProductOut, ProductType, ProductEmailOut, ProductQuantity
from tests.conftest import headers, API_URL


@pytest.mark.asyncio
async def test_products_list_empty(mocker):
    resource = ProductResource(api_url=API_URL, headers=headers)

    async def mock_list(self):
        return []

    mocker.patch(
        "shoppy.resources.ProductResource.list",
        mock_list
    )
    products = await resource.list()
    assert resource.schema == ProductOut
    assert resource.endpoint == "/v1/products/"
    assert products == []


@pytest.mark.asyncio
async def test_products_list(mocker, random_string):
    resource = ProductResource(api_url=API_URL, headers=headers)

    async def mock_list(self):
        faker = Faker()
        products = []
        # Create 50 products
        for _ in range(50):
            random_id = random_string
            new_product = ProductOut(
                id=random_id,
                title=faker.word(),
                description=faker.text(),
                price=faker.random_int(min=0, max=100),
                type=ProductType.SERVICE.value,
                created_at=faker.date_time(),
                updated_at=faker.date_time(),
                stock=faker.random_int(min=0, max=100),
                currency="PLN",
                gateways=["PayPal"],
                unlisted=False,
                email=ProductEmailOut(enabled=False),
                quantity=ProductQuantity(min=1, max=5),
                confirmations=0,
                attachment_id=None,
                custom_fields=None,
                webhook_urls=None,
                dynamic_url=None,
                position=None,
                seller=None,
                product_link=f"https://shoppy.gg/products/{random_id}"
            )
            # Add product to list
            products.append(new_product)
        # return products
        return products

    mocker.patch("shoppy.resources.ProductResource.list",
                 mock_list)
    products: List[ProductOut] = await resource.list()
    assert len(products) == 50

    assert resource.schema == ProductOut
    assert resource.endpoint == "/v1/products/"
    assert products[0].id is not None
    assert products[0].price is not None
    assert products[0].product_link is not None
    assert products[0].type is not None
    assert products[0].title is not None
    assert products[0].description is not None
    assert products[0].stock is not None
    assert products[0].currency is not None


@pytest.mark.asyncio
async def test_products_list_pagination(mocker, random_string):
    resource = ProductResource(api_url=API_URL, headers=headers)

    # Mock list method
    async def mock_list(self, page=int):
        faker = Faker()
        products = []
        # Create 50 products
        for _ in range(51):
            random_id = random_string
            new_product = ProductOut(
                id=random_id,
                title=faker.word(),
                description=faker.text(),
                price=faker.random_int(min=0, max=100),
                type=ProductType.SERVICE.value,
                created_at=faker.date_time(),
                updated_at=faker.date_time(),
                stock=faker.random_int(min=0, max=100),
                currency="PLN",
                gateways=["PayPal"],
                unlisted=False,
                email=ProductEmailOut(enabled=False),
                quantity=ProductQuantity(min=1, max=5),
                confirmations=0,
                attachment_id=None,
                custom_fields=None,
                webhook_urls=None,
                dynamic_url=None,
                position=None,
                seller=None,
                product_link=f"https://shoppy.gg/products/{random_id}"
            )
            # Add product to list
            products.append(new_product)
        # return products paginated list
        paginated_list = [products[i:i + 25] for i in range(0, len(products), 25)]
        if not page:
            page = 1
        return paginated_list[page - 1]

    mocker.patch("shoppy.resources.ProductResource.list", mock_list)

    products = await resource.list(page=1)
    products_second_page = await resource.list(page=2)
    products_thirth_page = await resource.list(page=3)
    assert resource.endpoint == "/v1/products/"
    assert len(products) == 25
    assert len(products_second_page) == 25
    assert len(products_thirth_page) == 1
    assert products[0].id is not None
    assert products[0].title is not None
    assert products[0].description is not None
    assert products[0].price is not None
    assert products[0].type is not None
