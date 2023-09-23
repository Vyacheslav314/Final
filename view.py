import Note


def create_note():
    title = input('Введите Название заметки: ')
    body = input('Введите Описание заметки: ')
    return Note.Note(title=title, body=body)

def the_end():
    print("Работа программы завершена!!")