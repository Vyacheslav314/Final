import file_operation
import Note
import view
 


def add():
    note = view.create_note()
    array = file_operation.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_operation.write_file(array, 'a')
    print('Заметка добавлена...')
  if valid == True:
           print('Такой заметки нет, возможно, вы ввели неверный id') 


def show(text):
    logic = True
    array = file_operation.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Note.Note.get_id(notes))
    if logic == True:
        print('Нет ни одной заметки...')


def edit_note():
    id = input('Введите id необходимой заметки: ')
    array = file_operation.read_file()
    valid = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            valid = False
            note = view.create_note()
            Note.Note.set_title(notes, note.get_title())
            Note.Note.set_body(notes, note.get_body())
            Note.Note.set_date(notes)
            print('Заметка изменена...')
                
                
def delete_note():
    id = input('Введите id необходимой заметки: ')
    array = file_operation.read_file()
    valid = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            valid = False
            array.remove(notes)
            print('Заметка удалена...')
    if valid == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    file_operation.write_file(array, 'a')
    
