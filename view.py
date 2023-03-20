from colorama import Fore, Style


class View(object):

    @staticmethod
    def show_number_point_list(notes):
        for note in notes:
            print(Fore.MAGENTA + '>>>...' + Style.RESET_ALL)
            print(note)

    @staticmethod
    def show_note(note):
        print(Fore.MAGENTA + '>>>...' + Style.RESET_ALL)
        print(note)

    @staticmethod
    def show_empty_list_message():
        print(Fore.MAGENTA + '\t\t>>>Cписок заметок пустой!' + Style.RESET_ALL)

    @staticmethod
    def display_note_id_not_exist(note_id):
        print(Fore.MAGENTA + f'>>>\t\tЗаметка ' + Fore.LIGHTYELLOW_EX +
              f'{note_id}' + Fore.MAGENTA + 'не найдена!' +
              Style.RESET_ALL)

    @staticmethod
    def display_note_id_exist(note_id):
        print(Fore.MAGENTA + '>>>Заметка ' + Fore.LIGHTYELLOW_EX +
              f'{note_id}' + Fore.MAGENTA + 'уже есть!' +
              Style.RESET_ALL)

    @staticmethod
    def display_note_stored():
        print(Fore.MAGENTA + f'>>>Заметка успешно добавлена!' + Style.RESET_ALL)

    @staticmethod
    def display_note_updated(note_id):
        print(Fore.MAGENTA + '>>>Заметка ' + Fore.LIGHTYELLOW_EX + f'{note_id} ' +
              Fore.MAGENTA + 'обновлена!' + Style.RESET_ALL)

    @staticmethod
    def display_note_deletion(note_id):
        print(Fore.MAGENTA + '>>>Заметка ' + Fore.LIGHTYELLOW_EX + f'{note_id} ' +
              Fore.MAGENTA + 'удалена!' + Style.RESET_ALL)

    @staticmethod
    def display_all_notes_deletion():
        print(Fore.MAGENTA + '>>>Все заметки удалены!' + Style.RESET_ALL)

    def display_note_id_not_exist(search_id):
        return search_id
