import os

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")


def convert_to_rub(transaction: dict) -> float:
    """Функция принимает значение в долларах или евро, обращается к API и возвращает конвертацию в рубли"""
    headers = {"apikey": api_key}
    amount = transaction["operationAmount"].get("amount")
    code = transaction["operationAmount"]['currency']['code']
    to = 'RUB'
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={code}&amount={amount}"
    response = requests.get(url, headers=headers, params={'from': code, 'to': 'RUB', 'amount': amount})
    if response.status_code != 200:
        raise ValueError(f"Failed to get currency rate")
    else:
        json_result = response.json()
        rub_amount = json_result["result"]
        return rub_amount


if __name__ == "__main__":
    print(convert_to_rub(45, "USD"))
