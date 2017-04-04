from http import to_requests

class GiftRocket(object):

    def __init__(self, access_token, domain="https://www.giftrocket.com"):
        if not access_token:
            raise Exception("Access token required for GiftRocket API")

        self.requests = to_requests('{}/api/v1/'.format(domain), {
            "access_token": access_token
        })

    # Organizations
    def create_organization(self, data):
        return self.requests("organizations", "POST", data)

    def get_organizations(self):
        return self.requests("organizations", "GET")

    # Organization Members
    def create_organization_member(self, organization_id, data):
        return self.requests(
            "organizations/{}/members".format(organization_id),
            "POST",
            data
        )

    def get_organization_members(self, organization_id):
        return self.requests(
            "organizations/{}/members".format(organization_id),
            "GET"
        )

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
    def get_styles(self, data=None):
        return self.requests("styles", "GET", data or {})

    # Funding Sources
    def get_funding_sources(self, data=None):
        return self.requests("funding_sources", "GET", data or {})
