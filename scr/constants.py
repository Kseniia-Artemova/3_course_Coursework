PATH = "sources/operations.json"  # путь к файлу с операциями от корневой папки проекта
COUNT_TRANSFERS = 5
OBLIGATION_PARAMETERS_PAY = {"id", "date", "state", "operationAmount", "description", "to"}
FORMAT_DATE = "%Y-%m-%dT%H:%M:%S.%f"    # принятый формат даты
AMOUNT_DIGITS = {"card": 16, "account": 20}