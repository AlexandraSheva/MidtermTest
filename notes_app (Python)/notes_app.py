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

def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить всю записную книжку\n"
          "2. Найти нужную запись\n"
          "3. Редактировать запись\n"
          "4. Добавить запись\n"
          "5. Удалить запись\n"
          "6. Сохранить запись\n"
          "7. Закончить работу")
    choice = int(input())
    return choice

def read_csv(filename: str) -> list:
    data = []
    fields = ["Идентификатор", "Заголовок", "Заметка", "Дата создания/ изменения"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def print_result(data: list):
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

def get_search_date():
    date = input("Введите дату создания/ изменения: ")
    return date

def add_note(data: list):
    new_note = input ("Введите заметку: ")
    max_id = max ( note [id] for note in data) if data else 0
    new_note[id] = max_id + 1
    data.append(new_note)

