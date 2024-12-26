import datetime
def create_note() :
    notes = []
    print("Привет. Я - планировщик задач. ")  # приветствие

    username = input("Введите имя пользователя: ").strip()
    print(f"Рад познакомиться, {username}!" )

    title = input("Введите название заметки: ").strip()

    content = input("Расскажите о своих планах и целях, " + username + ": ").strip()

    print("Введите статус заметки:")  # Запрашиваем статус заметки
    print("1) новая")
    print("2) в процессе")
    print("3) выполнено")
    while True:
        status_input = input("Ваш выбор (новая, в процессе, выполнено): ").strip().lower()
        if status_input in ['новая', 'в процессе', 'выполнено']:
            status = status_input
            break
        else:
            print(
                "Некорректный ввод. Пожалуйста, выберите статус из предложенных вариантов: новая, в процессе, выполнено.")
    print(status)

    create_date = (datetime.datetime.now().strftime("%d-%m-%Y"))
    print(create_date)
    while True:
        try:  # формат даты
            issue_date = datetime.datetime.strptime(input('Дедлайн: (введите дату в формате "день-месяц-год"): '), '%d-%m-%Y')  # дедлайн от пользователя
            temp_issue_date = (issue_date.strftime('%d-%m-%Y'))
            print(temp_issue_date)
            break
        except ValueError:
            print('Некорректная дата')

    note = {'Имя пользователя': username,
             'Название заметки': title,
             'Содержание': content,
             'Статус': status,
             'Дата создания': create_date,
             'Дедлайн': temp_issue_date} , # словарь

    notes.append(note)

    s = "" #проверка на пустоту в пунктах
    if len(s) == 0:
        print("Строка пустая")

    print("\nЗаметка создана:")
    print(note)

    return note
create_note ()
