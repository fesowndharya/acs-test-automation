import requests
import time
import yaml
import logging

class CurrencyExchange():
    config_dict = {}
    
    def __init__(self, base_currency = "EUR" , interval=10):
        # this will be useful only when we have licensed subscription for exchangeratesapi, 
        # where we are allowed to even set our base currency
        self.base_currency_symbol = base_currency
        self.cached_data= {}
        self.interval_in_seconds = interval
        self.ttls={}
        CurrencyExchange.get_config()

    @classmethod
    def get_config(cls):
        with open('config.yaml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        CurrencyExchange.config_dict = data

    def set_interval(self, seconds):
        self.interval_in_seconds = seconds

    def set_base_currency(self, base_currency):
        self.base_currency_symbol = base_currency
    
    def get_currency_rate(self, symbol):
        # since this api not exposed over http, we are jsut logging the exception we encounter and will retur 0
        url = "{base_url}?access_key={access_key}&base={base_sym}&symbols={get_sym}".format(base_url=CurrencyExchange.config_dict["base_url"],access_key=CurrencyExchange.config_dict["access_key"], base_sym=self.base_currency_symbol, get_sym=symbol)
        try:
            logging.debug("Timestamp {}: Requesting from Currency api....".format(time.time()))
            res = requests.get(url)
            if res.status_code == 200:
                res=res.json()
                return res["rates"][symbol]
            else:
                logging.error("ERROR: The status code for the request is :{}".format(res.status_code))
                return None
        except Exception as e:
            logging.error(e)
            
    def get_currency(self, **kwargs):
        key = tuple([(k, v) for k, v in kwargs.items()])
        if key in self.cached_data:
            if (key in self.ttls) and (self.ttls[key] > time.time()):
                logging.debug("Fetching from cache")
                return self.cached_data[key]
            else:
                logging.debug("cache expired")
                self.cached_data[key] = self.get_currency_rate(kwargs["to_currency"])
                logging.debug("New rate is catched")
                self.ttls[key] = time.time() + self.interval_in_seconds
                return self.cached_data[key]
        else:
                self.cached_data[key] = self.get_currency_rate(kwargs["to_currency"])
                self.ttls[key] = time.time() + self.interval_in_seconds
                return self.cached_data[key]

