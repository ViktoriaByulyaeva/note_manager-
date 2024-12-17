titles_=[] #список заголовков

while True: #начинается цикл для введения заголовков без ограничения
    title = input('Введите название ')
    print("Чтобы закончить, нажмите 'enter' ")
    titles_.append(title)
    if title == "": #условие для завершения
        break

titles_ = [i for i in titles_ if i] #убираем пустые строки в списке

setarr = set (titles_) #проверка уникальности элементов
if len(titles_) == len(setarr):
    print('Все элементы уникальны')
else:
    print("Есть одинаковые заголовки")

print(titles_)
