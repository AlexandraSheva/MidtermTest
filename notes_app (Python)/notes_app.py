#Реализовать консольное приложение заметки, с сохранением, чтением,
#добавлением, редактированием и удалением заметок. Заметка должна
#содержать идентификатор, заголовок, тело заметки и дату/время создания или
#последнего изменения заметки. Сохранение заметок необходимо сделать в
#формате json или csv формат (разделение полей рекомендуется делать через
#точку с запятой). Реализацию пользовательского интерфейса студент может
#делать как ему удобнее, можно делать как параметры запуска программы
#(команда, данные), можно делать как запрос команды с консоли и
#последующим вводом данных, как-то ещё, на усмотрение студента.

import datetime
from datetime import datetime

def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить всю записную книжку\n"
          "2. Найти нужную запись\n"
          "3. Редактировать запись\n"
          "4. Добавить запись\n"
          "5. Удалить запись\n"
          "6. Закончить работу")
    choice = int(input())
    return choice

def work_with_notebook():
    choice = show_menu()
    note_book = read_csv('notebook.csv')

    while (choice != 6):
        if choice == 1: # 1. Отобразить весь справочник
            print_result(note_book) 
        elif choice == 2: # 2. Найти запись по дате
            date = date_search()
            print_result(find_by_date(note_book, date)) 
        #elif choice == 3: # 3. Редактировать заметку
            
        elif choice == 4: # 4. Добавить запись
            user_data = get_new_note() 
            add_note(note_book, user_data)
            write_csv('notebook.csv', note_book)
        elif choice == 5: # 5. Удалить запись
            name = date_search() 
            print_result(find_by_date(note_book, name)) 
            delete_note(note_book, find_by_date(note_book, name))
            write_csv('notebook.csv', note_book)

def read_csv(filename: str) -> list:  #чтение файла
    data = []
    fields = ["Идентификатор", "Заголовок", "Заметка", "Дата создания/ изменения"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def write_csv(filename: str, data: list):   #запись в файл
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def print_result(data: list):  #вывод записей
    s = ' '
    fields = ["Идентификатор", "Заголовок", "Заметка", "Дата создания/ изменения"]
    for v in fields:
        s += v.center(20)
    print(f'{s}')

    for i in range(len(data)):
            s = ' '
            for v in data[i].values():
                s += v.center(20)
            print(f'{s}')

def add_note ():  #ввод заметки
    one_note = []
    title = input ("Введите заголовок: ")
    one_note.append(title)
    note = input ("Введите заметку: ")
    one_note.append(note)
    date_note = datetime.date.today()
    one_note.append(date_note)
    return one_note

def date_search():  #преобразование введенной даты в формат даты
    date_input = input ("Введите дату в формате чч.мм.гг : ")
    dt_input_date = datetime.strptime(date_input, '%d.%m.%y')
    return dt_input_date

def find_by_date(data: list, date):  #поиск по дате
    search_by_date = []
    for line in data:
        index = line['Дата создания/ изменения']
        if index.find(date) == 0:
            search_by_date.append(dict(line))
    return search_by_date

def get_new_note():  # Введение заметки
    line = {}
    fields = ["Идентификатор", "Заголовок", "Заметка", "Дата создания/ изменения"]
    for v in fields:
        data = input(f'Введите {v}: ')
        line[v] = data
    return line

def add_note(data: list, user_data: dict): #добавление словаря в список в файле
    data.append(dict(user_data))
    return data

def delete_note(data: list, note): #удаление заметки
    tmp = []
    for record in note:      
        if record in data:
            print('Запись для удаления:')
            tmp.append(record)
            print_result(tmp)
            confirmation = input('Чтобы удалить, введите ""да"",\n'
                                 'чтобы отменить удаление, введите ""нет"":')
            if confirmation == 'да':
                data.remove(record)
            elif confirmation == 'нет':
                return
            tmp.clear()


        
work_with_notebook()