# путь к файлу с операциями от корневой папки проекта
PATH = "sources/operations.json"

# количество платежей для отображения на экране
COUNT_TRANSFERS = 5

# обязательные поля, которые должны быть у платежа
OBLIGATION_PARAMETERS_PAY = {"id", "date", "state", "operationAmount", "description", "to"}

# принятый формат даты
FORMAT_DATE = "%Y-%m-%dT%H:%M:%S.%f"

# корректное количество символов номера для карты и счета
AMOUNT_DIGITS = {"card": 16, "account": 20}
