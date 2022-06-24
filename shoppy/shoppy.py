from shoppy.resources import ProductResource, FeedbackResource, QueriesResource, OrderResource


class Shoppy:
    def __init__(self, api_key: str, api_url: str = "https://shoppy.gg/api", user_agent: str = "Shoppy API Client"):
        self.api_key = api_key
        self.api_url = api_url
        self.headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json',
            'User-Agent': user_agent,
        }

        self.products = ProductResource(api_url=self.api_url, headers=self.headers)
        self.feedbacks = FeedbackResource(api_url=self.api_url, headers=self.headers)
        self.queries = QueriesResource(api_url=self.api_url, headers=self.headers)
        self.orders = OrderResource(api_url=self.api_url, headers=self.headers)
