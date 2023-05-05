import scr.utils as utils

PATH_TO_PAYMENTS = "../sources/operations.json"
COUNT_TRANSFERS = 5
OBLIGATION_PARAMETERS_PAY = {"id", "date", "state", "operationAmount", "description", "to"}


def main():
    payments = utils.get_latest_payments(PATH_TO_PAYMENTS, COUNT_TRANSFERS, OBLIGATION_PARAMETERS_PAY)

    for pay_info in payments:
        payment = utils.create_payment(pay_info)
        utils.show_payment(payment)


if __name__ == "__main__":
    main()
