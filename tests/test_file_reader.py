import pandas as pd

from src.file_reader import read_csv_transaction, read_excel_transaction
from unittest.mock import patch


df_excel = pd.read_excel('transactions_excel.xlsx')
df_csv = pd.read_csv('transactions.csv')


@patch("pandas.read_excel")
def test_read_excel_transaction(mock_dict):
    mock_dict.return_value = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {
                "amount": "16210",
                "currency": {"name": "Sol", "code": "PEN"},
            },
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "operationAmount": {
                "amount": "29740",
                "currency": {"name": "Peso", "code": "COP"},
            },
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
        },
    ]
    assert read_excel_transaction("transactions_excel.xlsx") == [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {
                "amount": "16210",
                "currency": {"name": "Sol", "code": "PEN"},
            },
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "operationAmount": {
                "amount": "29740",
                "currency": {"name": "Peso", "code": "COP"},
            },
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
        },
    ]
    mock_dict.assert_called_once_with("../src/transactions_excel.xlsx")


def test_read_excel_transaction_1():
    assert read_excel_transaction("../src/transactions_excel.xlsx") == [{}]


def test_read_csv_transaction():
    assert read_csv_transaction("../src/transactions.csv") == [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {
                "amount": "16210",
                "currency": {"name": "Sol", "code": "PEN"},
            },
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "operationAmount": {
                "amount": "29740",
                "currency": {"name": "Peso", "code": "COP"},
            },
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
        },
        {
            "id": "593027",
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "operationAmount": {
                "amount": "30368",
                "currency": {"name": "Shilling", "code": "TZS"},
            },
            "description": "Перевод с карты на карту",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
        },
        {
            "id": "366176",
            "state": "EXECUTED",
            "date": "2020-08-02T09:35:18Z",
            "operationAmount": {
                "amount": "29482",
                "currency": {"name": "Rupiah", "code": "IDR"},
            },
            "description": "Перевод с карты на карту",
            "from": "Discover 0325955596714937",
            "to": "Visa 3820488829287420",
        },
        {
            "id": "5380041",
            "state": "CANCELED",
            "date": "2021-02-01T11:54:58Z",
            "operationAmount": {
                "amount": "23789",
                "currency": {"name": "Peso", "code": "UYU"},
            },
            "description": "Открытие вклада",
            "from": "",
            "to": "Счет 23294994494356835683",
        },
    ]


def test_read_csv_transaction_1():
    assert read_csv_transaction("../src/transactions.csv") == [
        {
            "id": "1962667",
            "state": "EXECUTED",
            "date": "2023-10-22T09:43:32Z",
            "operationAmount": {
                "amount": "18588",
                "currency": {"name": "Peso", "code": "COP"},
            },
            "description": "Перевод организации",
            "from": "Mastercard 7286844946221431",
            "to": "Счет 76145988629288763144",
        },
        {
            "id": "5294458",
            "state": "EXECUTED",
            "date": "2022-06-20T18:08:20Z",
            "operationAmount": {
                "amount": "16836",
                "currency": {"name": "Yuan Renminbi", "code": "CNY"},
            },
            "description": "Перевод с карты на карту",
            "from": "Visa 2759011965877198",
            "to": "Счет 38287443300766991082",
        },
        {
            "id": "5429839",
            "state": "EXECUTED",
            "date": "2023-06-23T19:46:34Z",
            "operationAmount": {
                "amount": "25261",
                "currency": {"name": "Hryvnia", "code": "UAH"},
            },
            "description": "Открытие вклада",
            "from": "",
            "to": "Счет 76768135089446747029",
        },
        {
            "id": "3226899",
            "state": "EXECUTED",
            "date": "2023-04-17T09:21:15Z",
            "operationAmount": {
                "amount": "21680",
                "currency": {"name": "Koruna", "code": "CZK"},
            },
            "description": "Открытие вклада",
            "from": "",
            "to": "Счет 88329674734590848775",
        },
        {
            "id": "3176764",
            "state": "CANCELED",
            "date": "2022-08-24T14:32:38Z",
            "operationAmount": {
                "amount": "16652",
                "currency": {"name": "Euro", "code": "EUR"},
            },
            "description": "Перевод с карты на карту",
            "from": "Mastercard 8387037425051294",
            "to": "American Express 5556525473658852",
        },
    ]


def test_csv_data_dict_2():
    assert read_csv_transaction("../src/transactions.csv") == [{}]
