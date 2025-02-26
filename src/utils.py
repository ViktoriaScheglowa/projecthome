import json
from typing import Any

from src.external_api import convert_to_rub

import requests
import logging


logging.basicConfig(
    filename='utils.log',
    filemode='w',
    format='%(asctime)s %(name)s %(Levelname)s:%(message)s')


logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('utils.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions_dictionary(path: str) -> Any:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as operations:
            try:
                transactions_data = json.load(operations)
                return transactions_data
            except json.JSONDecodeError:
                transactions_data = []
                return transactions_data
    except FileNotFoundError:
        transactions_data = []
        return transactions_data


def return_transaction_amount_in_rub(transactions: list, transaction_id: int) -> Any:
    """Функция принимает транзакцию и возвращает сумму транзакции в рублях, если не в рублях, конвертирует в рубли"""
    for transaction in transactions:
        if transaction.get("id") == transaction_id:
            if transaction["operationAmount"]["currency"]["code"] == "RUB":
                rub_amount = transaction["operationAmount"]["amount"]
                return rub_amount
            else:
                not_rub_amount = transaction["operationAmount"]["amount"]
                currency = transaction["operationAmount"]["currency"]["code"]
                rub_amount = round(convert_to_rub(not_rub_amount, currency), 2)
                if rub_amount != 0:
                    return rub_amount
                else:
                    return "Конвертация не может быть выполнена"
    else:
        return "Транзакция не найдена"


if __name__ == "__main__":
    transactions = get_transactions_dictionary("../data/operations.json")
    print(return_transaction_amount_in_rub(transactions, 41428829))