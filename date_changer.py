import datetime

created_date="Дата создания"
print(created_date)
created_date=(datetime.datetime.now())
print(created_date)
temp_created_date=(datetime.datetime.now().strftime("%d-%m"))
print(temp_created_date)

issue_date="Дедлайн"
print(issue_date)
issue_date = datetime.datetime.strptime(input ('Введите дату в формате "день-месяц-год": '), '%d-%m-%Y')
temp_issue_date = (issue_date.strftime('%d-%m'))
print(temp_issue_date)
