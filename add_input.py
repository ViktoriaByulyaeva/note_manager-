username = input ("Как Вас зовут? ")
print ("Здравствуйте, ", username, "!")
title = input ("введите название заметки ")
content = input ("Расскажите о своих планах и целях, " + username + " ")
import datetime
created_date=(datetime.datetime.now())
print("Дата создания заметки: ", created_date.strftime("%d-%m"))
issue_date = input ("Дата, когда нужно закончить ")
print(username, "," , issue_date, "подойдет дедлайн", title)