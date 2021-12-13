import requests_mock
import requests
# import sys
# sys.path.append('./src')
from src.currency import CurrencyExchange

@requests_mock.Mocker(kw="mock")
def test_get_currency(**kwargs):
    m = kwargs["mock"]
    url='http://api.exchangeratesapi.io/v1/latest?access_key=e7a7dcd869ef0db71dfcb083a5ad625e&base=EUR&symbols=USD'
    test_json = {   
        "success": True,
        "timestamp": 1639341544,
        "base": "EUR",
        "date": "2021-12-12",
        "rates": {
            "USD": 1.131676
        }
    }
    m.get(url, json=test_json)
    out = requests.get(url).json()
    currencyExchange = CurrencyExchange()
    out = currencyExchange.get_currency(to_currency = "USD")
    assert out == test_json["rates"]["USD"]
