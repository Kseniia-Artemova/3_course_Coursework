# 3_course_Coursework
Coursework of 3 course. Code for the "Account Transactions" widget

The information about payments reads from JSON-file "operations.json"
in folder "sources". On this information's base creates objects of class Payment.
The informations about 5 the latest successful payments displayed on the screen.
Please, enjoy!

For setup and operation:
1. poetry install
2. don't change the location of files and folders
3. activate virtual environment with command: poetry shell
4. run file from project's root with command: python programs/main.py

# Пример вывода для одной операции:
14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.
