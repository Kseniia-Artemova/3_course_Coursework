import scr.utils as utils

PATH_TO_PAYMENTS = "../sources/operations.json"
NUMBER_SUCCESSFUL_TRANSFERS = 5


def main():
    payments = utils.open_payments(PATH_TO_PAYMENTS, revert=True)
    counter = 0
    index = 0

    while counter != NUMBER_SUCCESSFUL_TRANSFERS:
        if payments[index]["state"] == "EXECUTED":
            payment = utils.create_payment(payments[index])
            utils.show_payment(payment)
            counter += 1

        index += 1
