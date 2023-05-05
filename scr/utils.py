import json
from itertools import islice
import scr.payment as pay_


def get_latest_payments(path, count, parameters):
    with open(path, "rt", encoding="utf-8") as json_file:
        payments = json.load(json_file)

    latest_payments_gen = latest_correct_payments(payments, parameters)
    successful_payments = islice(latest_payments_gen, count)

    return successful_payments


def latest_correct_payments(payments, parameters):
    for pay in payments[::-1]:
        if pay["state"].lower() == "executed":
            if parameters.issubset(set(pay.keys())):
                yield pay


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
    date = pay.get_date()
    description = pay.get_description()
    pay_from = pay.get_pay_from()
    pay_to = pay.get_pay_to()
    operation_amount = pay.get_operation_amount()

    print(f"\033[31m{date.rsplit('.', 1)[0]}\033[0m.{date.rsplit('.', 1)[1]} "
          f"{description}")
    if pay_from:
        print(f"{pay_from[0]} \033[34m{hide(pay_from[1])}\033[0m ", end=" ")
    print(f"-\033[33m> \033[0m{pay_to[0]} \033[34m{hide(pay_to[1])}")
    print(f"\033[31m{operation_amount[0]}\033[0m {operation_amount[1]}")
    print()

def hide(number):
    if len(number) == 16:
        hide_start = 6
        hide_end = 12
        hidden_simbols = hide_end - hide_start
        number_hide = number[:hide_start] + "*" * hidden_simbols + number[hide_end:]
        number_sep = [number_hide[i:i+4]for i in range(0, len(number), 4)]

        return " ".join(number_sep)

    elif len(number) == 20:
        return number.replace(number[:-4], "**")
