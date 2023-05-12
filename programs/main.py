import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import scr.utils as utils
from constants.constants import PATH
from constants.constants import COUNT_TRANSFERS


def main() -> None:
    # Получаем полный путь к файлу с операциями, откуда бы не был запущен скрипт
    *dirs, name_file = PATH.split("/")
    path_to_file = utils.get_path_to_file(name_file, *dirs)

    # Получаем итератор на основе списка словарей из JSON-файла
    # с информацией о платежах пользователя, словари отсортированы
    # по дате в обратном порядке
    payments = utils.get_payments(path_to_file)

    counter = 0

    # Создаём объекты класса Payment и выводим на экран информацию либо
    # по заданному количеству успешных и корректных платежей,
    # либо пока в списке не закончатся платежи
    while counter < COUNT_TRANSFERS:
        latest_payment = next(payments, None)
        if latest_payment:
            payment = utils.create_payment(latest_payment)
            if all((payment.id_pay,
                    payment.state_pay,
                    payment.date_pay,
                    payment.operation_amount_pay,
                    payment.description_pay,
                    payment.to_pay)):
                utils.show_payment(payment)
                counter += 1
        else:
            break


if __name__ == "__main__":
    main()
