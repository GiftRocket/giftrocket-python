giftrocket-python
==============

A python client library for the [GiftRocket API][1].

## Installation

```console
$ pip install giftrocket-python
```

## Getting started

All API requests require an access token.  A sandbox access token is assigned upon signup through the [GiftRocket Dashboard][2]. Once you are ready to move to production, you will be assigned a production access token.

### Authentication

```python
from giftrocket import GiftRocket

# Sandbox environment
client = GiftRocket("[SANDBOX_ACCESS_TOKEN]", "https://testflight.giftrocket.com")

# Production environment
client = GiftRocket("[PRODUCTION_ACCESS_TOKEN]", "https://www.giftrocket.com")
```

### Orders

See [API documentation][3] for all Order options.  Use the FoundingSources resource to look up a valid method for your payment (i.e. credit card, ACH, etc).

```python
# Create a new order, specifying your gift options
# as an array of objects.
response = client.create_order({
  "funding_source_id": "[FUNDING_SOURCE_ID]",
  "gifts": [
    {
      "amount": 40,
      "message": "Such a great way to show appreciation to others!",
      "recipient": {
        "email": "person@yourteam.com",
        "name": "Person Example"
      },
      "style_id": "[STYLE_ID]"
    }
  ]
})

if response.ok:
    order = response.to_json()["order"]


# Return historical orders, optionally passing a starting offset for results.
response = client.get_orders({offset: 10})

# Return a order by order_id
response = client.get_order("[ORDER_ID]")
```

### Funding Sources
Production funding sources must be added through the web dashboard. A sandbox funding source is provided during development.

```python
# Retrieve a list of your funding sources (credit card, ach, etc).
response = client.get_funding_sources()
```

### Styles
A style defines the presentation of your gift.  The styles endpoint returns an array of card designs.

```python
response = client.get_styles()
```

### Gifts
Retrieve a single or many historical gifts sent by your account.

```python
response = client.get_gifts({offset: 10})

response = client.get_gift("[GIFT_ID]")
```

[1]: https://giftrocket.com/docs
[2]: https://giftrocket.com/rewards
[3]: https://giftrocket.com/docs
