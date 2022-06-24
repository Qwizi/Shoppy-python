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
            id='ws9yfM7', 
            attachment_id=None, 
            title='Product', 
            description='Product description', 
            image=None, 
            unlisted=False, 
            type='service', 
            price=10, 
            currency='EUR', 
            email=ProductEmailOut(enabled=False), 
            stock_warning=0, 
            quantity=ProductQuantity(min=1, max=1),
            confirmations=6, 
            gateways=['PayPal'], 
            webhook_urls=[], 
            dynamic_url='', 
            position=None, 
            created_at=datetime.datetime(2020, 8, 31, 12, 5, 56, tzinfo=datetime.timezone.utc), 
            updated_at=datetime.datetime(2022, 6, 22, 18, 4, 24, tzinfo=datetime.timezone.utc), 
            seller=None, 
            stock=9223372036854775807, 
            accounts=[], 
            product_link='https://shoppy.gg/product/ws9yfM5'
        )
    ]
    """
```
