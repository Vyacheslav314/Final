import function as f
import view


def run():
    command = ''
    while command != '7':
        view.menu()
        command = input().strip()
        if command == '1':
            f.show('all')
        if command == '2':
            f.add()
        if command == '3':
            f.show('all')
            f.id_edit_del_show('del')
        if command == '4':
            f.show('all')
            f.id_edit_del_show('edit')
        if command == '5':
            f.show('date')
        if command == '6':
            f.show('id')
            f.id_edit_del_show('show')
        if command == '7':
            view.goodbuy()
            break
        print("Нажмите Enter, что бы продолжить ")
        input()