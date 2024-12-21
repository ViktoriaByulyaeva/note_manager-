import datetime # импорт даты
username = input ("Как Вас зовут? Введите Ваше имя: ")
print ("Здравствуйте, ", username, "!")
title = input ("Введите название заметки: ")
content = input ("Расскажите о своих планах и целях, " + username + ": ")
status = input( "Введите статус заметки: ")

created_date = (datetime.datetime.now()) #дата создания (сейчас)
print ("Дата создания заметки: ", created_date.strftime("%d-%m")) #Сокращение даты до д-м

issue_date="Дедлайн: "
print(issue_date)
issue_date = datetime.datetime.strptime(input ('Введите дату в формате "день-месяц-год": '), '%d-%m-%Y') #пользователь вводит дату
temp_issue_date = (issue_date.strftime('%d-%m')) #сокращаем дату
print (username, "," , temp_issue_date, "подойдет дедлайн", title) #итог
