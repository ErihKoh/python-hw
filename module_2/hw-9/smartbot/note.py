import re
from .address_book import load_note
from pathlib import Path

NOTE = []


def check_note_name(note_list, new_name_note):
    """Функция проверка существования заголовка в списке"""
    for note in note_list:
        if note['name'] == new_name_note:
            print("Заметка с таким именем уже существует.")
            return True
        else:
            return False


def input_name_note():
    name_note = input('Введите имя заметки: ')
    # Проверяем, есть ли заметка с таким заголовком в базе
    is_exist_name = check_note_name(NOTE, name_note)
    if is_exist_name:
        return input_name_note()
    return name_note


def input_tags():
    new_note_tags = input('Введите один или несколько тегов заметки: ')
    # Сплитим все заметки в список
    tags = re.split(r'[ ,]+', new_note_tags)
    tag_list = ['#' + i for i in tags]
    return tag_list


def input_text_note():
    new_note_text = input('Введите текст заметки: ')
    return new_note_text


def add_note():
    """Функция создания заметки"""

    name_note = input_name_note()
    tags_note = input_tags()
    text_note = input_text_note()

    created_note = {'name': name_note, 'tag': tags_note, 'text': text_note}
    NOTE.append(created_note)
    print(created_note)
    return 'Ваша заметка успешно сохранена.\n'


def delete_note():
    """Функция удаления заметок по заголовку"""
    note_title = input("Введите заголовок заметки для удаления.\n>>> ")
    for note in NOTE:
        if note_title == note['name']:
            index = NOTE.index(note)
            NOTE.pop(index)
            return f"Заметка с заголовком: '{note_title}' успешно удалена."
        else:
            return f"Заметка c заголовком: '{note_title}', отсутствует."


def change_note():
    """Функция редактирования заметки"""
    note_name = input("Введите заголовок заметки для редактирования.\n>>>  ")
    for note in NOTE:
        if note_name == note['name']:
            while True:
                value_to_change = input("Введите имя поля, которое хотите отредактировать:"
                                        " 'name', 'text' либо 'tag'.\n"
                                        "Чтобы выйти - просто нажмите 'Enter'.\n>>> ").strip()
                if value_to_change.lower() == "":
                    break
                elif value_to_change.lower() == 'text':
                    note_text = str(input("Enter text.\n>>> "))
                    note['text'] = note_text
                elif value_to_change.lower() == 'name':
                    note_name = str(input("Enter name.\n>>> "))
                    note['name'] = note_name
                elif value_to_change.lower() == 'tag':
                    note_tag = str(input("Enter tag.\n>>> "))
                    tag_list = note['tag']
                    if note_tag in tag_list:
                        tag_list.remove(note_tag)
                    else:
                        tag_list.append(note_tag)
                else:
                    return "Вы ввели неверную команду, пожалуйста, попробуйте еще раз."
            return f"Заметка успешно изменена."
        else:
            return f"Заметка с заголовком: '{note_name}', отсутствует."


def show_notes() -> str:
    """Функция вывода всех заметок"""
    result = ''
    if NOTE:
        for note in NOTE:
            for k, v in note.items():
                if not isinstance(v, list):
                    result += f'{k.title()}: {v}\n'
                else:
                    if len(v) != 1:
                        result += f'{k.title()}: {", ".join(v)}\n'
                    else:
                        result += f'{k.title()}: {v[0]}\n'
            result += '\n'
        return result
    else:
        return 'Нет записей в заметках.'


def find_note():
    """Функция поиска заметок по заголовку и тегу"""
    search_value = input('Пожалуйста, введите имя или тег заметки для поиска.\n>>> ')

    if search_value.find('#') == 0:
        for note in NOTE:
            if search_value in note['tag']:

                tags = ', '.join(note['tag'])
                return f"Заметка: {note['name']}\nТеги: {tags}\nТекст: {note['text']}\n"

            else:
                return f'Заметка по тегу {search_value} не найдена.'
    else:
        for note in NOTE:
            if search_value == note['name']:
                tags = ', '.join(note['tag'])
                return f"Заметка: {note['name']}\nТеги: {tags}\nТекст: {note['text']}\n"

            else:
                return f'Заметка c именем: {search_value}, не найдена.'
