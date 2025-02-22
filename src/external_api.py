import json
import os
from typing import Any

import requests
from dotenv import load_dotenv
from requests import RequestException

load_dotenv()

api_key = os.getenv("API_KEY")


def convert_to_rub(transaction: dict) -> Any:
    """Функция принимает значение в долларах или евро, обращается к API и возвращает конвертацию в рубли"""
    currency = transaction['currency']
    amount = transaction['amount']
    try:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={amount}"
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers)
        json_result = response.json()
        rub_amount = json.loads(json_result)["result"]
        return rub_amount
    except RequestException:
        return 0


 #if __name__ == "__main__":
 #   print(convert_to_rub(45, "USD"))
