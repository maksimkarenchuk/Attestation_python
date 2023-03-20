from controller import Controller
from modelJSON import ModelJSON
from view import View
from note import Note

import os
import datetime
from colorama import init, Back, Fore, Style

init(autoreset=True)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def run():
    c = Controller(ModelJSON("notes.json"), View())

    while True:
        command = input(Fore.CYAN +
                        '[1] Добавить заметку\n'
                        '[2] Показать заметку\n'
                        '[3] Показать все заметки\n'
                        '[4] Редактировать заметку\n'
                        '[5] Удалить заметку\n'
                        '[6] Удалить все заметки\n'
                        '[7] Выход\n' + Fore.MAGENTA +
                        'Выберите действие: ' + Style.RESET_ALL)

        if command == '1':
            print(Fore.CYAN + '\tСоздание заметки.' + Style.RESET_ALL)
            c.create_note(get_note_data())

        elif command == '2':
            print(Fore.CYAN + '\tПоказать заметку.' + Style.RESET_ALL)
            if c.notes_exist():
                c.show_note(int(get_number()))

        elif command == '3':
            if c.notes_exist():
                print(Fore.CYAN + '\tПоказать все заметки.' + Style.RESET_ALL)
                c.show_notes()

        elif command == '4':
            if c.notes_exist():
                print(Fore.CYAN + '\tРедактировать заметку.' + Style.RESET_ALL)
                updated_id = int(get_number())
                if c.note_id_exist(updated_id):
                    c.update_note(updated_id, get_note_data())

        elif command == '5':
            if c.notes_exist():
                print(Back.RED + Fore.BLACK + '\tВы удаляете заметку!' + Style.RESET_ALL)
                delete_id = int(get_number())
                if c.note_id_exist(delete_id):
                    c.delete_note(delete_id)

        elif command == '6':
            if c.notes_exist():
                print(Back.RED + Fore.BLACK + 'Удалить все заметки!' + Style.RESET_ALL)
                if input(Back.RED + Fore.BLACK + 'Уверены!!! (Y/N): ' +
                         Style.RESET_ALL).capitalize() == 'Y':
                    if c.notes_exist():
                        c.delete_all_notes()

        elif command == '7':
            break

        else:
            print(Fore.MAGENTA + '\tНеверный ввод!' + Style.RESET_ALL)


def get_note_data():
    note_id = 0
    date = datetime.datetime.now()
    title = input(Fore.MAGENTA + '\t\tДайте имя заметке: ' + Style.RESET_ALL)
    text = input(Fore.MAGENTA + '\t\tЗаполните заметку: ' + Style.RESET_ALL)
    return Note(note_id, date, title, text)


def get_number():
    while True:
        get_choice = input(Fore.MAGENTA + '\t\tВведите id заметки: ' + Style.RESET_ALL)
        if get_choice.isdigit() and int(get_choice) > 0:
            return get_choice
        else:
            print(Fore.RED + '\t\t\tВведено неверное id заметки!' + Style.RESET_ALL)
