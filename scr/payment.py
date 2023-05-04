class Payment:

    def __init__(self):

        self.__id = None
        self.__state = None
        self.__date = None
        self.__operation_amount = None
        self.__description = None
        self.__from = None
        self.__to = None

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
        date_for_format = str(date).split("T")[0].split("-")[::-1]

        if len(date_for_format) == 3:
            if all([
                len(date_for_format[0]) == 2,
                date_for_format[0].isdigit() and int(date_for_format[0]) in range(1, 32),
                len(date_for_format[1]) == 2,
                date_for_format[1].isdigit() and int(date_for_format[1]) in range(1, 13),
                len(date_for_format[2]) == 4,
                date_for_format[2].isdigit()
            ]):

                self.__date = ".".join(date_for_format)
            else:
                self.__date = "Invalid date format!"

        else:
            self.__date = "Invalid date format!"

    def get_date(self):
        return self.__date

    def set_operation_amount(self, operation_amount):

        self.__operation_amount = operation_amount

    def get_operation_amount(self):
        return self.__operation_amount

    def set_description(self, description):
        self.__description = description

    def get_description(self):
        return self.__description

    def set_pay_from(self, pay_from):
        self.__from = pay_from

    def get_pay_from(self):
        return self.__from

    def set_pay_to(self, pay_to):
        self.__to = pay_to

    def get_pay_to(self):
        return self.__to


class OperationAmount:

    def __init__(self, dict_):
        self.__amount = None
        self.__currency_name = None

    def set_amount(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def set_currency_name(self, name):
        self.__currency_name = name

    def get_currency_name(self):
        return self.__currency_name





