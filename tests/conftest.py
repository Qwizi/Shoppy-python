import datetime
import random
import string

import pytest

from shoppy.schemas import ProductOut, ProductQuantity, ProductType, ProductEmailOut

API_URL = "http://localhost"
headers = {
    'Authorization': "API KEY",
    'Content-Type': 'application/json',
    'User-Agent': "User-Agent",
}


@pytest.fixture
def product():
    return ProductOut(
        id="ws9yfM7",
        title="Test",
        quantity=ProductQuantity(min=1, max=5),
        currency="PLN",
        description="Test",
        type=ProductType.SERVICE.value,
        email=ProductEmailOut(enabled=False),
        price=10,
        unlisted=False,
        gateways=["PayPal"],
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
        stock=999
    )


# pytest fixtures are used to create objects that are used in tests.
# The fixtures are created in the conftest.py file.
@pytest.fixture
def random_string():
    # Random string with length of 6 with letters and numbers
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(6)])
