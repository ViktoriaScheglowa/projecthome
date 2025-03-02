# Проект "Homework 10_1"

## Описание:

Программа создана для фильтрации и сортировки банковских счетов по дате оплаты
## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/ViktoriaScheglowa/projecthome.git
```

2. Установите зависимости:
```
pip install -r requirements.txt
```

3. Создайте базу данных и выполните миграции:
```
python manage.py migrate
```

4. Запустите локальный сервер:
```
python manage.py runserver
```
## Используемые функции:

1. Функция скрывающая номер карты и счета.
2. Функция сортировки по дате.
3. Функция фильтрации в операциях по счетам.
4. Функция выдающая транзакции, где валюта операции соответствует заданной.
5. Функция возвращающая описание каждой операции по очереди.
6. Функция генерирующая номера карт в заданном диапазоне.
7. Функция принимает значение в долларах или евро, обращается к API и возвращает конвертацию в рубли.
8. Функция принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
9. Функция принимает транзакцию и возвращает сумму транзакции в рублях, если не в рублях, конвертирует в рубли. 
10. Функция считывает данные о финансовых операциях из CSV файла и преобразует их в список словарей.
11. Функция считывает данные о финансовых операциях из excel файла и преобразует их в список словарей.

## Тестирование:

Для запуска тестирования необходимо в терминале ввести "pytest"

## Документация:

Дополнительную информацию о структуре проекта и API можно найти в [документации](docs/README.md).

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).
