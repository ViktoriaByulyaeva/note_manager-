print("Статус заметки:"
      "(Ответ возможен только из представленных вариантов)") #инструкция
print('1) Готово') #варианты ответов:
print("2) В процессе")
print("3) Отложено")

while True:
    answer = input("Ваш ответ: ") #ввести ответ33
    if answer.lower() in ['1', 'готово'] :
        print("Статус заметки обновлен на: Готово")
        break
    elif answer.lower() in ['2', 'в процессе'] :
        print('Статус заметки обновлен на: В процессе')
        break
    elif answer.lower() in ['3', 'отложено']:
        print("Статус заметки обновлен на: Отложено")
        break
    else: #если пользователь ввел иные значения в ответ
        print("Некорректный ответ. Повторите попытку и выберете из предложенных вариантов")


status_now = {'Текущий статус' : answer}
print(status_now)