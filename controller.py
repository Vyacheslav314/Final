import function as f
import view


def run():
    command = ""
    while True:
        print("\nВведите номер команды:\n\n1 - вывод всех заметок из файла\n2 - добавление заметки"
          "\n3 - редактирование заметки\n4 - удаление заметки\n5 - выборка заметок по дате"
          "\n6 - выход\n\nВведите номер функции: ")
        command = input().strip()
        if command == "1":
            f.show('all')
        if command == "2":
            f.add()
        if command == "3":
            f.show('all')
            f.edit_note()
        if command == "4":
            f.show('all')
            f.delete_note()
        if command == "5":
            f.show('date')
        if command == "6":
            view.the_end()
            break
        print("Нажмите Enter, что бы продолжить ")
        input()