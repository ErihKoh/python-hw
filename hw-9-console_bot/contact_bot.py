import re

CONTACT_DICT = {}

flag = True


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
    global flag
    flag = False
    return 'Good bye!'


@error_handler
def add_contact_handler(name: str, number: int):
    """
       name: string
       number: integer
    """
    if name == '' or number == '':
        raise NameError('ValueError: entered wrong values. Name and numbers are required')
    else:
        CONTACT_DICT[name] = number
        return 'Contact was added'


@error_handler
def change_contact_handler(name: str, number: int):
    """
        name: string
        number: integer
    """
    if name == '' or number == '':
        raise NameError('ValueError: entered wrong values. Name and numbers are required. Or enter "exit" for complete')
    else:
        for item in CONTACT_DICT.keys():
            if item == name:
                CONTACT_DICT[item] = number
                return 'Contact was changed '
            else:
                raise NameError('KeyError: name not found')


def show_number_handler(name: str):
    """
       name: string

    """
    if name == '':
        raise NameError('ValueError: entered wrong values. Name is required. Or enter "exit" for complete')
    else:
        return CONTACT_DICT[name]


def show_all_contacts(*args, **kwargs):
    return CONTACT_DICT


changed_action = {
    'hello': greeting_handler,
    'add': add_contact_handler,
    'change': change_contact_handler,
    'phone': show_number_handler,
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
           'phone' for getting a number of contact (param: name: str)
           'change' for changing number of contact (param: name: str and number(new number): int )
           'show all' for printing all contacts
           'hello' for greeting
           'exit', 'good bye', 'close' for exit from script
    """
    result = re.match(r'hello|add|show all|change|exit|good bye|close|phone', com)
    if not result:
        raise NameError('ValueError: command was wrong, try again! Or enter "exit" for complete')
    else:
        entered_command = result.group()
        end_index = result.end()
        str_without_command = com[end_index + 1::]
        list_without_command = com[end_index + 1::].strip().split(' ') if str_without_command else []
        name = list_without_command[0] if len(list_without_command) >= 1 else ''
        number = int(list_without_command[1]) if len(list_without_command) == 2 else ''

    return changed_action[entered_command](name, number)


def main():
    while flag:
        command = input('Enter command: ').lower()
        print(parser(command))


if __name__ == '__main__':
    main()
