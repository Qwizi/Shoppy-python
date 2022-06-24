# Shoppy python api client

# Usage

```python
from shoppy import Shoppy

API_KEY = 'your-api-key'


async def main():
    # Create a new shoppy client
    shoppy = Shoppy(api_key=API_KEY)
    # Get the list of all products
    products = await shoppy.products.list()
    # print products
    print(products)
    """
    Example response
    [
        ProductOut(
            id="ws9yfM3",
            title="Product 1",
            description="This is a product",
            image=None,
            unlisted=False,
            type="service",
            price=50,
            currency="EUR",
            email=ProductEmailOut(enabled=False),
            stock_warning=0,
            quantity=ProductQuantity(
                min=1,
                max=10
            ),
            confirmations=0,
            gateways=["PayPal"],
            webhook_url=["https://example.com/webhook"],
            dynamic_url=None,
            position=1,
            created_at="2020-01-01T00:00:00.000Z",
            updated_at="2020-01-01T00:00:00.000Z",
            seller=None,
            stock=10,
            accounts=[],
            product_link="https://shoppy.gg/product/ws9yfM3",
        )
    ]
    """
```
