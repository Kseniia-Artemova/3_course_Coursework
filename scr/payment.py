class Payment:

    def __init__(self):
        self.__id = None
        self.__state = None
        self.__date = None
        self.__operation_amount = None
        self.__description = None
        self.__from = None
        self.__to = None

    def __str__(self):
        return f"Payment {self.__id}, more detailed information is closed."

    def __repr__(self):
        return f"Payment(" \
                       f"id={self.__id}," \
                       f"state=\"{self.__state}\"," \
                       f"date=\"{self.__date}\"," \
                       f"operation_amount={self.__operation_amount}," \
                       f"description=\"{self.__description}\"," \
                       f"from=\"{self.__from}\"," \
                       f"to=\"{self.__to}\")"

    def set_id(self, id_operation):
        if type(id_operation) is int:
            self.__id = id_operation

    def get_id(self):
        return self.__id

    def set_state(self, state_operation):
        if state_operation.lower() == "executed":
            self.__state = state_operation.upper()

    def get_state(self):
        return self.__state

    def set_date(self, date):
        for_date = str(date).split("T")[0].split("-")[::-1]
        if self.__check_date(for_date):
            self.__date = ".".join(for_date)
        else:
            self.__date = "Invalid date format!"

    @staticmethod
    def __check_date(date):
        days_in_months = {
            "01": 31, "02": 29, "03": 31, "04": 30, "05": 31, "06": 30,
            "07": 31, "08": 31, "09": 30, "10": 31, "11": 30, "12": 31
        }

        if len(date) != 3:
            return False
        elif not date[0].isdigit() or len(date[0]) != 2:
            return False
        elif date[1] not in days_in_months:
            return False
        elif int(date[0]) not in range(1, days_in_months.get(date[1]) + 1):
            return False
        elif len(date[2]) != 4 or not date[2].isdigit():
            return False

        return True

    def get_date(self):
        return self.__date

    def set_operation_amount(self, operation_amount):
        pass
        amount = operation_amount.get('amount')
        currency = operation_amount.get('currency')
        currency_name = currency.get('name') if currency else None

        operation_amount_new = OperationAmount(amount, currency_name)

        self.__operation_amount = operation_amount_new

    def get_operation_amount(self):
        return self.__operation_amount

    def set_description(self, description):
        if description and type(description) is str:
            self.__description = description

    def get_description(self):
        return self.__description

    def set_pay_from(self, pay_from):
        if pay_from and self.__check_pay_card(pay_from):
            self.__from = pay_from
        else:
            self.__from = "Incorrect account or card number!"

    @staticmethod
    def __check_pay_card(card):
        AMOUNT_DIGITS = [16, 20]
        card_details = str(card).split()
        card_number = card_details[-1]
        account = card_details[0]
        if not card_number.isdigit():
            return False
        elif len(card_number) not in AMOUNT_DIGITS:
            return False
        elif account.lower() == "счет" and len(card_number) != AMOUNT_DIGITS[-1]:
            return False

        return True

    def get_pay_from(self):
        return self.__from

    def set_pay_to(self, pay_to):
        if pay_to and self.__check_pay_card(pay_to):
            self.__to = pay_to
        else:
            self.__to = "Incorrect account or card number!"

    def get_pay_to(self):
        return self.__to


class OperationAmount:

    def __init__(self, amount, currency):
        self.__amount = None
        self.set_amount(amount)
        self.__currency_name = None
        self.set_currency_name(currency)

    def __str__(self):
        return f"Pay {self.__amount} {self.__currency_name}"

    def __repr__(self):
        return f"OperationAmount(" \
               f"amount=\"{self.__amount}, " \
               f"currency_name=\"{self.__currency_name}\")"

    def set_amount(self, amount):
        if amount and self.__check_amount(amount):
            self.__amount = amount
        else:
            self.__amount = "Incorrect amount!"

    @staticmethod
    def __check_amount(amount):
        for_amount = str(amount).split(".")
        if len(for_amount) != 2:
            return False
        elif len(for_amount[1]) != 2:
            return False
        elif not for_amount[0].isdigit() or not for_amount[1].isdigit():
            return False
        elif int(for_amount[0]) < 0 or int(for_amount[1]) < 0:
            return False

        return True

    def get_amount(self):
        return self.__amount

    def set_currency_name(self, name):
        if name and type(name) is str:
            self.__currency_name = name

    def get_currency_name(self):
        return self.__currency_name





