#def show_menu() -> int:
#    print("\nВыберите необходимое действие:\n"
#          "1. Отобразить всю записную книжку\n"
#          "2. Найти нужную запись\n"
#          "3. Редактировать запись\n"
#          "4. Добавить запись\n"
#          "5. Удалить запись\n"
#          "6. Закончить работу")
#    choice = int(input())
#    return choice

def read_notebook (filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print (line)

def write_notebook (filename):
    with open(filename, 'w', encoding='utf-8') as file:
        
    



read_notebook('notebook.csv')