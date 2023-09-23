#Напишите проект, содержащий функционал работы с заметками. 
#Программа должна уметь создавать заметку, сохранять её, 
#читать список заметок, редактировать заметку, удалять заметку.

def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить все заметки\n"
          "2. Найти заметку по идентификатору\n"
          "3. Найти заметку по дате\n"
          "4. Добавить заметку\n"
          "5. Удалить заметку\n"
          "6. Закончить работу\n")
    choice = int(input())
    return choice

def work_with_notebook():
    choice = show_menu()
    note_book = read_csv('notebook.csv')

    while (choice != 6):
        if choice == 1: # 1. Отобразить все заметки
            print_result(note_book) 
        elif choice == 2: # 2. Найти заметку по идентификатору
            id = get_search_id()
            print_result(find_by_id(note_book, id)) 
        elif choice == 3: # 3. Найти заметку по дате     Этот пункт не смогла реализовать: выдает ошибку – не понимаю, почему
            date = get_search_date() 
            print_result(find_by_date(note_book, date))
        elif choice == 4: # 4. Добавить заметку
            note_data = get_new_note() 
            add_note(note_book, note_data)
            write_csv('notebook.csv', note_book)
        elif choice == 5: # 5. Удалить заметку
            id = get_search_id() 
            print_result(find_by_id(note_book, id)) 
            delete_note(note_book, find_by_id(note_book, id))
            write_csv('notebook.csv', note_book)
        choice = show_menu()

def read_csv(filename: str) -> list:
    data = []
    fields = ["Идентификатор", "Заголовок", "Заметка", "Дата создания"]
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
    fields = ["Идентификатор", "Заголовок", "Заметка", "Дата создания"]
    for v in fields:
        s += v.center(20)
    print(f'{s}')

    for i in range(len(data)):
            s = ' '
            for v in data[i].values():
                s += v.center(20)
            print(f'{s}')

def get_search_id():
    for_id = input("Введите идентификатор: ")
    return for_id
        
def find_by_id(data: list, for_id):
    search_by_id = []
    for line in data:
        index = line['Идентификатор'].lower()
        if index.find(for_id.lower()) == 0:
            search_by_id.append(dict(line))
    return search_by_id

def get_search_date():
    date = input("Введите дату: ")
    return date

def find_by_date(data: list, date):
    search_by_date = []
    for line in data:
        index = line['Дата']
        if  index.find(date) == 0:
            search_by_date.append(dict(line))
    return search_by_date

def get_new_note():
    line = {}
    fields = ["Идентификатор", "Заголовок", "Заметка", "Дата создания"]
    for v in fields:
        data = input(f'Введите {v}: ')
        line[v] = data
    return line

def add_note(data: list, note_data: dict):
    data.append(dict(note_data))
    return data

def delete_note(data: list, note):
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

def get_file_name():
    name = input("Введите имя файла: ")
    return name


work_with_notebook()