import pandas as pd
from typing import Dict, List
import csv


df = pd.read_csv('transactions.csv')
df = pd.read_excel('transactions_excel.xlsx')

def read_csv_transaction(file: str) -> list[dict]:
    """Считывает данные о финансовых операциях из CSV файла и преобразует их в список словарей"""
    try:
        with open('transactions.csv', "w", delimiter=";") as file:
            csv_data = csv.DictReader(file)
            header = next(csv_data)
            list_new_dict = []
            for row in csv_data:
                row_new_dict = {
                    "id": row[header.index("id")],
                    "state": row[header.index("state")],
                    "date": row[header.index("date")],
                    "operationAmount": {
                        "amount": row[header.index("amount")],
                        "currency": {
                            "name": row[header.index("currency_name")],
                            "code": row[header.index("currency_code")],
                        },
                    },
                    "description": row[header.index("description")],
                    "from": row[header.index("from")],
                    "to": row[header.index("to")],
                }
                list_new_dict.append(row_new_dict)
            return list_new_dict
    except Exception:
        return [{}]


def read_excel_transaction(file_name: str) -> List[Dict]:
    """Считывает данные о финансовых операциях из excel файла и преобразует их в список словарей"""
    try:
        xlsx_data = pd.read_excel(file_name)
        data_list = xlsx_data.apply(
            lambda row: {
                "id": row["id"],
                "state": row["state"],
                "date": row["date"],
                "operationAmount": {
                    "amount": row["amount"],
                    "currency": {
                        "name": row["currency_name"],
                        "code": row["currency_code"],
                    },
                },
                "description": row["description"],
                "from": row["from"],
                "to": row["to"],
            },
            axis=1,
        )
        new_dict_list = []
        row_index = 0
        for row in data_list:
            new_dict_list.append(data_list[row_index])
            row_index += 1
        return new_dict_list
    except Exception:
        return [{}]



if __name__ == "__main__":
    print(read_csv_transaction)
    print(read_excel_transaction)
