from src.currency_file import CurrencyExchange
import time

if __name__ == "__main__":
    CurrencyExchange.get_config()
    obj1= CurrencyExchange(base_currency="EUR",interval=4)
    print(" USD rate is :{}".format(obj1.get_currency(to_currency = "USD")))
    time.sleep(10)
    print("USD rate is :{}".format(obj1.get_currency(to_currency = "USD")))
    obj2= CurrencyExchange(interval=4)
    print("JPY rate is :{}".format(obj1.get_currency(to_currency = "JPY")))
    time.sleep(10)
    jpyValue = obj1.get_currency(to_currency = "JPY")
    print(f"JPY rate is :{jpyValue}")