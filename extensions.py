import requests
import json
from config import keys


class APIException(Exception):
    pass

# Исключения при вводе неправильных данных
class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты "{base}".\nСписок всех доступных валют: /values')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'"{quote}" такой валюты нет в списке.\nСписок всех доступных валют: /values')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'"{base}" такой валюты нет в списке.\nСписок всех доступных валют: /values')

        try:
            amount = float(amount.replace(",", "."))
        except KeyError:
            raise APIException(f'Не удалось обработать колличество "{amount}"')

        # API валютного обменника
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base