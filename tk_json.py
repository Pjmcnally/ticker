import json


def main():
    links_json = """
[
    {
        "SiteName": "zacks",
        "UrlTemplate": "https://www.zacks.com/stock/quote/{0}",
        "Enabled": true,
        "Order": 1
    },
    {
        "SiteName": "finviz",
        "UrlTemplate": "https://finviz.com/quote.ashx?t={0}",
        "Enabled": true,
        "Order": 2
    },
    {
        "SiteName": "openinsider",
        "UrlTemplate": "http://openinsider.com/search?q={0}",
        "Enabled": true,
        "Order": 3
    },
    {
        "SiteName": "earningswhispers",
        "UrlTemplate": "https://earningswhispers.com/stocks/{0}",
        "Enabled": true,
        "Order": 4
    },
    {
        "SiteName": "shortsqueeze",
        "UrlTemplate": "http://shortsqueeze.com/?symbol={0}",
        "Enabled": false,
        "Order": 5
    }
]"""

    # p_out = json.dumps(links_obj, indent=4)
    p_in = json.loads(links_json)
    for item in sorted(p_in, key=lambda k: k['Order']):
        print(type(item["Order"]))


main()
