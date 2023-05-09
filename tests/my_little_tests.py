# import scr.payment as pay_
# import scr.utils as u
from datetime import datetime
import os

# pay = pay_.Payment()
# pay.set_date("2090-10-30")
# print(pay.get_date())
# pay.set_operation_amount({'amount': '56516.093', 'currency': {'name': 'USD', 'code': 'USD'}})
# amount = pay.get_operation_amount()
# print(amount.get_amount())
# print(pay)
# print(repr(pay))
# PARAMETERS_PAY = {"id", "date", "state", "operationAmount", "description", "to"}
#
# payments = [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
#              'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
#              'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}, {'id': 114832369, 'state': 'EXECUTED',
#              'date': '2019-12-07T06:99:14.634890', 'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}},
#              'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012', 'to': 'Счет 35158586384610753655'}, {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19T09:22:25.899614', 'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 7810846596785568', 'to': 'Счет 43241152692663622869'}, {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051', 'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 38611439522855669794', 'to': 'Счет 46765464282437878125'}, {'id': 801684332, 'state': 'EXECUTED', 'date': '2019-11-05T12:04:13.781725', 'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381'}]
#
#
# pays = u.get_latest_payments("../sources/operations.json", 5, PARAMETERS_PAY)
# print(pays)
#
# pays_ = u.latest_correct_payments(payments, PARAMETERS_PAY)
# for i in pays_:
#     print(i)


# print(u.hide("1596837868705199"))
# print(u.hide("35737585785074382265"))
#
# date = '2019-11-30 12:22:25.899614'
# the_date = datetime.fromisoformat(date)
# print(the_date)
# amount = iter("6381-")
#
# print(amount)

amount = "45"
print(str(round(float(amount), 3)))