import logging
from fuzzywuzzy import fuzz

from .address_book import add_contact, delete_contact, change_contact, find_contact, show_contacts, show_birthdays, \
    dump_note, CONTACTS
from .note import add_note, delete_note, change_note, find_note, show_notes, NOTE


# Config logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG, datefmt='%d.%m.%Y %H:%M:%S')

# Init logger
logger = logging.getLogger()


def handle_info(func):
    def inner(*args):
        result = func(*args)
        logger.info(result)
        return result

    return inner


def exit_app():
    """Функция выхода из бота"""
    # dump_note(ADDRESS_BOOK_FILE, CONTACTS)
    # dump_note(NOTE_FILE, NOTE)
    return


COMMAND = {
    'add_contact': add_contact,
    'delete_contact': delete_contact,
    'change_contact': change_contact,
    'find_contact': find_contact,
    'show_contacts': show_contacts,
    'show_birthdays': show_birthdays,
    'add_note': add_note,
    'delete_note': delete_note,
    'change_note': change_note,
    'find_note': find_note,
    'show_notes': show_notes,
    'exit': exit_app
}


def command_analyzer(input_command):
    """Функция, которая занимается анализом введенных команд"""
    psb_cmd = []
    for key, value in COMMAND.items():
        if fuzz.ratio(key, input_command) == 100:
            return value()
        elif 80 < fuzz.ratio(key, input_command) < 100:
            print(f"Похоже, вы имели ввиду команду: {key}")
            return value()
        elif 40 <= fuzz.ratio(key, input_command) <= 80:
            psb_cmd.append(key)
    if len(psb_cmd) > 0:
        return f'К сожалению, команда не распознана. Вероятно, вы имели ввиду что-то из этого: {", ".join(psb_cmd)}\n \
                 Попробуйте ввести команду еще раз.'
    else:
        return f'К сожалению, команда не распознана. \
                 Попробуйте ввести команду еще раз.'


def main():
    print(f'Список команд: {[i for i in COMMAND.keys()]}')
    while True:
        user_input = input('Input your command: ')
        command = user_input.lower().strip()
        result = command_analyzer(command)
        if not result:
            exit_app()
            print('Bye')
            break
        print(result)


if __name__ == '__main__':
    main()
