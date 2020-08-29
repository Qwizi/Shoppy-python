class ResourceClient:
    endpoint = None
    api_url = "https://shoppy.gg/api"

    def __init__(self, session):
        self.session = session
