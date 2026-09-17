inverse = int(input("Введите 1 для обычного перевода, и 2 для реверсивного: "))


units = {
    1: (1024, "KB"),
    2: (1024 ** 2, "MB"),
    3: (1024 ** 3, "GB"),
    4: (1024 ** 4, "TB")
}

if inverse == 1:
    try:
        bytes_count = float(input("Напишите количество байт: "))
    except ValueError:
        print("Ошибка")
        exit()

    user_choice = int(input("Выберите единицу для перевода"
                            "\n1.KB"
                            "\n2.MB"
                            "\n3.GB"
                            "\n4.TB"))

    if user_choice in units:
        divider, units_name = units[user_choice]
        res = bytes_count / divider
        print(f"Результат: {res}")
    else:
        print("Ошибка")

elif inverse == 2:
    try:
        question = float(input("Напишите количеств"))
    except ValueError:
        print("Ошибка")
        exit()

    inverse_user_choice = int(input("Какая это единица\n"
                                        "1.KB\n"
                                        "2.MB\n"
                                        "3.GB\n"
                                        "4.TB\n"))

    if inverse_user_choice in units:
        multiplier, inverse_units_name = units[inverse_user_choice]
        inverse_res = question * multiplier
        print(f"Результат: {inverse_res} байт")
    else:
        print("Ошибка")

