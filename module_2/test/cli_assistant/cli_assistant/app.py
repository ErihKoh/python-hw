import re
import pickle

from .adress_book import Record, AddressBook, Name, Phone

DEFAULT_ADDRESS_BOOK_PATH = ".address_book.bin"


def dump_address_book(path, address_book):
    with open(path, "wb") as f:
        pickle.dump(address_book, f)


def load_address_book(path):
    try:
        with open(path, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


flag = True
address_book = load_address_book(DEFAULT_ADDRESS_BOOK_PATH)


def error_handler(func):
    def wrap(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(e, func.__doc__)

    return wrap


def greeting_handler(*args, **kwargs):
    return 'How can I help you?'


def close_handler(*args, **kwargs):
    dump_address_book(DEFAULT_ADDRESS_BOOK_PATH, address_book)
    global flag
    flag = False

    return 'Good bye!'


@error_handler
def add_contact_handler(name, number, *args, **kwargs):
    """
       name: string
       number: integer
    """
    if name == '' or number == '':
        raise NameError('ValueError: entered wrong values. Name and numbers are required')
    else:
        record = Record(Name(name), [Phone(number)])
        print(record)
        address_book.add_record(record)
        return 'Contact was added'


@error_handler
def edit_contact_handler(name: str, old_number: int, new_number: int):
    """
        name: string
        old_number: integer
        new_number: integer
    """
    if name == '' or old_number == '' or new_number == '':
        raise NameError('ValueError: entered wrong values. Name and numbers are required. Or enter "exit" for complete')
    else:
        old_record = Record(Name(name), [Phone(old_number)])
        new_record = Record(Name(name), [Phone(new_number)])
        address_book.edit_record(old_record, new_record)
        return 'Contact was changed'


def delete_handler(name: str, number: int):
    """
       name: string
       name: integer

    """
    if name == '':
        raise NameError('ValueError: entered wrong values. Name is required. Or enter "exit" for complete')
    else:
        record = Record(Name(name), [Phone(number)])
        address_book.delete_record(record)
        return 'Contact was deleted'


def show_all_contacts(*args, **kwargs):
    for page in address_book.iterator(2):

        if page:
            print(page)
            return ''
        else:
            return 'address_book is empty'


changed_action = {
    'hello': greeting_handler,
    'add': add_contact_handler,
    'change': edit_contact_handler,
    'delete': delete_handler,
    'show all': show_all_contacts,
    'close': close_handler,
    'exit': close_handler,
    'good bye': close_handler
}


@error_handler
def parser(com):
    """
    Command:
           'add'  for adding a contact (param: name: str and number: int)
           'delete' for remove contact (param: name: str and number: int)
           'change' for changing number of contact (param: name: str and number(new number): int )
           'show all' for printing all contacts
           'hello' for greeting
           'exit', 'good bye', 'close' for exit from script
    """
    result = re.match(r'hello|add|show all|change|exit|good bye|close|delete', com)
    if not result:
        raise NameError('ValueError: command was wrong, try again! Or enter "exit" for complete')
    else:
        entered_command = result.group()
        print(entered_command)
        entered_list = com.split(" ")
        print(entered_list)
        # end_index = result.end()
        # str_without_command = com[end_index + 1::]
        # list_without_command = com[end_index + 1::].strip().split(' ') if str_without_command else []
        # name = list_without_command[0] if len(list_without_command) >= 1 else ''
        # number = list_without_command[1] if len(list_without_command) >= 2 else ''
        # new_number = int(list_without_command[2]) if len(list_without_command) == 3 else ''

    # return changed_action[entered_command](name, number, new_number)


def main():
    while flag:
        command = input('Enter command: ').lower()
        print(parser(command))


if __name__ == '__main__':
    main()
