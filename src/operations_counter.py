from collections import Counter
from typing import Dict, List

from src.file_reader import read_csv_transaction


def get_counter_operations_by_description(
    dictionaries: List[Dict], operations: List
) -> Dict:
    """Принимает список операций и список категорий операций и возвращает словарь,
    где ключи - категории, а значения - количество операций в этой категории"""
    operations_list = []
    for dictionary in dictionaries:
        if dictionary["description"] in operations:
            operations_list.append(dictionary["description"])
        counted = Counter(operations_list)
        return counted


if __name__ == "__main__":
    dictionaries_1 = read_csv_transaction("../src/transactions.csv")
    list_1 = ["Открытие вклада", "Перевод с карты на карту"]
    result = get_counter_operations_by_description(dictionaries_1, list_1)
    print(result)
