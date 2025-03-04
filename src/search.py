import re
from typing import Dict, List

from src.file_reader import read_csv_transaction


def search_by_string(dictionaries: List[Dict], user_string: str) -> List[Dict]:
    """Принимеает список словарей и строку поиска, возвращает список словарей, у которых в описании есть эта строка"""
    new_dict_list = []
    for dictionary in dictionaries:
        text = dictionary["description"]
        need_search_string = re.findall(user_string, text, flags=re.IGNORECASE)
        if need_search_string:
            new_dict_list.append(dictionary)
    return new_dict_list


if __name__ == "__main__":
    dictionaries_1 = read_csv_transaction("../src/transactions.csv")
    result = search_by_string(dictionaries_1, "перевод")
    print(result)
