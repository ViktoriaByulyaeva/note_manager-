import datetime
notes = [] #список

print ("Привет. Я - планировщик задач. ") #приветствие
username = input ("Как Вас зовут? Введите Ваше имя: ")

print ("Рад познакомиться, ", username, "!")

while True: #бесконечный цикл
    title = input("Введите название заметки: ")
    content = input("Расскажите о своих планах и целях, " + username + ": ")
    print("Статус заметки:"
          "(Ответ возможен только из представленных вариантов)")  # инструкция
    print('1) Готово')  # варианты ответов:
    print("2) В процессе")
    print("3) Отложено")
    while True:
        status = input("Ваш ответ: ")  # ввести ответ33
        if status.lower() in ['1', 'готово']:
            print("Статус заметки обновлен на: Готово")
            break
        elif status.lower() in ['2', 'в процессе']:
            print('Статус заметки обновлен на: В процессе')
            break
        elif status.lower() in ['3', 'отложено']:
            print("Статус заметки обновлен на: Отложено")
            break
        else:  # если пользователь ввел иные значения в ответ
            print("Некорректный ответ. Повторите попытку и выберете из предложенных вариантов")
    create_date = 'Дата создания'
    create_date = datetime.datetime.now()  # дата сейчас (момент создания)
    print('Дата создания: ', datetime.datetime.now().strftime('%d-%m-%Y'))
    while True:
        try:  # формат даты
            issue_date = datetime.datetime.strptime(input('Дедлайн: (введите дату в формате "день-месяц-год"): '),
                                                    '%d-%m-%Y')  # дедлайн от пользователя
            break
        except ValueError:
            print('Некорректная дата')

    # условия:
    if create_date.day == issue_date.day and create_date.month == issue_date.month and create_date.year == issue_date.year:
        print("Срок выполнения сегодня")

    elif create_date > issue_date:
        print('Срок выполнения задачи прошел')

    else:
        period = issue_date - create_date
    print('Осталось {} дней'.format(period.days))

    note1 = {'Имя пользователя' : username, 'Название заметки' : title, 'Содержание' : content, 'Статус' : status, 'Дата создания' : create_date, 'Дедлайн' : issue_date} #словарь
    notes.append(note1) #добавить словарь в список

    note2 = input('Нужна еще одна заметка? Впишите ответ: да/нет. Ответ: ')
    if note2 == 'нет' :
        print('Возвращайтесь снова. Будем вместе достигать целей! ')
        break
    elif note2 == 'да' :
        print("Вместе мы добьемся вершин!")
    else:
        print('Некорректный ответ')
print(notes) #увидеть весь список словарей
