import datetime
create_date = datetime.datetime.now() #дата сейчас (момент создания)
print ('Дата создания: ', datetime.datetime.now().strftime('%d-%m-%Y'))

while True:
    try: #формат даты
        issue_date = datetime.datetime.strptime(input('Дедлайн: (введите дату в формате "день-месяц-год"): '), '%d-%m-%Y')  # дедлайн от пользователя
        break
    except ValueError:
        print('Некорректная дата')

#условия:
if create_date.day == issue_date.day and create_date.month == issue_date.month and create_date.year == issue_date.year:
    print("Срок выполнения сегодня")

elif create_date > issue_date :
    print('Срок выполнения задачи прошел')

else:
    period = issue_date - create_date
print ('Осталось {} дней'.format(period.days))

