from http import to_requests

class GiftRocket(object):
    base_url = 'https://www.giftrocket.com/api/v1/'

    def __init__(self, access_token):
        if not access_token:
            raise Exception("Access token required for GiftRocket API")

        self.requests = to_requests(self.base_url, {
            "access_token": access_token
        })

    # Orders
    def create_order(self, data):
        return self.requests("orders", "POST", data)

    def get_orders(self, data):
        return self.requests("orders", "GET", data)

    def get_order(self, order_id):
        return self.requests("orders/{}".format(order_id), "GET")

    # Gifts
    def get_gifts(self, data):
        return self.requests("gifts", "GET")

    def get_gift(self, gift_id):
        return self.requests("gifts/{}".format(gift_id), "GET")

    # Styles
    def get_styles(self):
        return self.requests("gifts", "GET")

    # Funding Sources
    def get_funding_sources(self):
        return self.requests("funding_sources", "GET")
