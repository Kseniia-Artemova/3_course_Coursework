import json
import scr.payment as pay_

def open_payments(path, revert=False):
    with open(path, "rt", encoding="utf-8") as json_file:
        payments = json.load(json_file)

    return payments[::-1] if revert else payments


def create_payment(pay_information: dict):
    payment = pay_.Payment()
    payment.set_id(pay_information.get("id"))
    payment.set_state(pay_information.get("state"))
    payment.set_date(pay_information.get("date"))
    payment.set_operation_amount(pay_information.get("operationAmount"))
    payment.set_description(pay_information.get("description"))
    payment.set_pay_from(pay_information.get("from"))
    payment.set_pay_to(pay_information.get("to"))

    return payment


def show_payment(pay):
    pass
