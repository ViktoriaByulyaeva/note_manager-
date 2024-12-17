note = {
    'username' : input ('Введите имя пользователя '),
    'title' : input ('Введите название заметки '),
    'content' : input ('Введите содержание заметки '),
    'status' : input ('Введите статус заметки '),
    'created_date' : input('Дата создания: '),
    'issue_date' : input('Дедлайн: '),
    'titles' : []
}

title1 = input('Заголовок №1 ')
title2 = input('Заголовок №2 ')
title3 = input('Заголовок №3 ')
titles = [title1, title2, title3]
note ['titles'].append(titles)

print(note)
