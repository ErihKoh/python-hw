# ФУНКЦИИ ДЛЯ ОБРАБОТКИ ТЕЛЕФОНА
import re
from datetime import datetime, timedelta
from .models import Session, Contact
from sqlalchemy.exc import NoResultFound
from sqlalchemy import select

# def load_note(path_file):
#     """Функция чтения данных из DB"""
#


# Пусть к файлу с контактами
CONTACTS = []


def sanitize_phone_number(number_phone):
    # Убирает лишние символы
    new_phone = (
        number_phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone


def check_phone_number(number_phone):
    # Функция проверяет валидность "нормализированного" номера и возвращает его в стандарте +380, или возвращает
    # False если невалиден
    sanitized_phone = sanitize_phone_number(number_phone)
    for symbol in sanitized_phone:  # должен содержать только цифры
        if symbol not in "0123456789":
            return False
    if sanitized_phone[0:3] == "380" and len(sanitized_phone) == 12:
        return "+" + str(sanitized_phone)  # начинаться с 380 и имеет длину 12
    elif sanitized_phone[0:1] == "0" and len(sanitized_phone) == 10:
        return "+38" + str(sanitized_phone)  # начинаться с 0 и имеет длину 10
    else:
        return False


def input_phone():
    # Дает возможность ввести телефон и проверяет его валидность.
    # Если невалиден - ввод еще раз, Если валиден - возвращает валидный телефон
    phone = input("Введите телефон.\n"
                  ">>> ")
    if not check_phone_number(phone):
        print("Вы ввели некорректный телефон.\n"
              "Попробуйте еще раз ;)")
        return input_phone()
    else:
        return phone


def add_other_phones():
    # Возвращает список от одного и более валидных телефонов.
    # После корректного введения 1 телефона спросит, хочешь ли добавить еще.
    # И, если ты уже ввел хотя бы 1 валидный номер, а потом захотел ввести еще, но ввел неправильно или передумал
    # вводить, будет предложено не вводить телефон и двинутся дальше вместо " Ты ввел неправильно, попробуй еще"
    phones_list = list()
    phone = input_phone()
    phones_list.append(phone)
    while True:
        other_phone = input("Если хотите добавит еще один номер - введите его.\n"
                            "Если хотите продолжить - нажмите 'Enter'.\n>>> ")
        if other_phone == "":
            return phone
        else:
            if check_phone_number(other_phone):
                phones_list.append(check_phone_number(other_phone))
                return ', '.join(phones_list)
            else:
                return "Вы ввели невалидный телефон.\nПопробуйте еще раз."


def enter_address():
    # Функция обработки адреса
    # Просто дает возможность вводить или не вводить адрес. Проверки нет.

    address = input("Введите адрес контакта и нажмите 'Enter'.\n"
                    "Что бы пропустить - нажмите 'Enter'.\n"
                    ">>> ")
    if address == "":
        return
    else:
        return address


def email_is_correct(email):
    # ФУНКЦИИ ДЛЯ ОБРАБОТКИ ЭМЕЙЛА
    # 1. Дать возможность пропустить ввод емейла.
    # 2. Проверка введенного емейла ( )
    # Функция принимает введенный эмейл, проверяет его, если валиден - возвращает его, иначе - возвращает False

    check = re.match(r"[a-zA-Z._]{1}[a-zA-Z._0-9]+@[a-zA-Z]+\.[a-z]{2}[a-z]*", email)
    if check:
        return email
    return False
    # Критерии проверки:
    # 1. Все буквы только англ алфавита
    # 2. ПРЕФИКС (то что до @)
    # 2.1 начинаеться с латинской буквы, содержит любое число символов
    # 2.2 и может содержать любое число/букву включая нижнее подчеркивание
    # 3. СУФФИКС (то что после @)
    # 3.1 Состоит из двух частей, разделенных точкой
    # 3.2 После точки должно быть минимум 2 символа


def enter_email():
    # Функция ничего не принимает, возвращает либо валидное значение email, либо None
    # Функция дает возможность ввести email или перейти дальше. В случае ошибки так же предложит пропустить или
    # попробовать заново.

    email = input("Введите Email человека и нажмите 'Enter'.\n"
                  "Чтобы пропустить - нажмите 'Enter'.\n>>> ")
    if email == "":
        return None
    else:
        if email_is_correct(email):
            return email_is_correct(email)
        else:
            print("Вы ввели недействительный email.\n"
                  "Попробуйте еще раз.")
            return enter_email()


# def birthday_is_correct(date):
#     # ФУНКЦИИ ДЛЯ ОБРАБОТКИ ДАТЫ РОЖДЕНИЯ
#     # 1. Дать возможность вводить или не вводить день рождения
#     # 2. Проверка на соответствие заданному формату даты
#
#     if re.match(r"^(?:0[1-9]|1[12])\.(?:[0-2][1-9]|3[01])\.(?:19[2-9]\d|[2-9]\d{3})$", date):
#         return True
#     return False


def enter_birthday():
    birthday = input(
        "Введите день рождения человека в формате 'mm.dd.yyyy' и нажмите 'Enter'.\n"
        "Чтобы пропустить - нажмите 'Enter'.\n"
        ">>> ")
    # pattern = re.match(r"^(?:[0-2][1-9]|3[01])\.(?:0[1-9]|1[12])\.(?:19[2-9]\d|[2-9]\d{3})$", birthday)
    if birthday == "":
        return
    else:
        # if pattern:
        return birthday
        # else:
        #     print("Вы ввели недействительную дату.\n"
        #           "Попробуйте еще раз.")
        #     return enter_birthday()


def insert_to_db(name, phones, email, address, birthday):
    """Функция записи данных в DB"""
    with Session() as session:
        data_for_db = Contact(name, phones, email, address, birthday)
        session.add(data_for_db)
        session.commit()


def add_contact() -> str:
    # Собранная функция добавления контакта
    name = input("Введите имя контакта: ")
    birthday = enter_birthday()
    address = enter_address()
    phones = add_other_phones()
    email = enter_email()
    insert_to_db(name, phones, email, address, birthday)
    return f'В записную книжку добавлена запись.\n' \
           f'Имя: {name}\n' \
           f'Дата рождения: {birthday}\n' \
           f'Адрес проживания: {address}\n' \
           f'Номер телефона: {phones}\n' \
           f'Email: {email}\n'


def delete_contact() -> str:
    # Функция удаления контакта
    name = input("Введите имя контакта для удаления: ")
    session = Session()
    try:
        session.query(Contact).filter(Contact.name == name).one()
        session.query(Contact).filter(Contact.name == name).delete(synchronize_session=False)
        session.commit()
        session.close()
        return f'Контакт с именем: {name}, удален'
    except NoResultFound:
        return f'Контакт с именем: {name}, в списке не найден'


def show_contacts() -> str:
    # Функция вывода всех контактов
    session = Session()
    statement = select(Contact.name, Contact.phone, Contact.email, Contact.address, Contact.birthday)
    result = session.execute(statement).all()
    if result:
        for i in result:
            print(
                f' Имя: {i[0]}\n Дата рождения: {i[4]}\n Адрес проживания: {i[3]}\n Номер телефона: {i[1]}\n Email: {i[2]}\n')
    else:
        return "Список пустой"
    return "==========================="


def current_week():
    current_date = datetime.now().date()
    day_of_week = current_date.weekday()

    to_beginning_of_week = timedelta(days=day_of_week)
    beginning_of_week = current_date - to_beginning_of_week

    to_end_of_week = timedelta(days=6 - day_of_week)
    end_of_week = current_date + to_end_of_week
    return beginning_of_week.strftime("%d-%m"), end_of_week.strftime("%d-%m")


def show_birthdays() -> str:
    # Функция выводы ближайших дней рождения контактов
    start, end = current_week()
    with Session() as session:
        statement = select(Contact.name, Contact.birthday)
        result = session.execute(statement).all()
        for i in result:
            if i:
                if start < i[1].strftime("%d-%m") < end:
                    print(f'{i[0]}: {i[1]}')
            return f"Запрос успешно выполнен"


def find_contact():
    """Функция поиска контакта по имени"""
    result = ''
    name_for_search = input("Введите имя.\n>>> ")
    session = Session()
    try:
        session.query(Contact).filter(Contact.name == name_for_search).one()
        session.commit()
        session.close()
        return f'Контакт с именем: {name_for_search}, изменен'
    except NoResultFound:
        return f'Контакт с именем: {name_for_search}, в списке не найден'


def wanna_change_smth_else():
    """Вложенная функция запроса на измениня каких-либо других полей"""
    answer = input("Изменения внесены. Если Хотите изменить что-то еще - введите любой символ и "
                   "нажмите 'Enter', чтобы выйти - просто нажмите 'Enter'.\n>>> ")
    if not answer:
        return 'ok'
    else:
        return change_contact()


# 3. Пользователю выводиться все поля контакта, и спрашиваеться, которое он хочет изменить.
# 4. Вызываеться функция изменения данного параметра
# 5. Спрашиваеться, нужно ли изменить что то еще
# 6. Если нужно изменить что то еще - начинаеться пунки 3.


def wanna_add_or_change_phone():
    """Вложенная функция изменения телефона контакта"""
    with Session() as session:
        statement = select(Contact.name, Contact.phones)
        result = session.execute(statement).one()


def change_contact():
    """Функция изменения контакта"""
    # contact = search_contact()
    # Принимает на вход контакт, найденный функцией search_contact_cycle,
    # печатает поля контакта, и спрашивает, который нужно изменить.

    count = 0  # Эта часть кода отображает содержание контакта с нумерацией полей словаря
    name_for_search = input("Введите имя.\n>>> ").strip()
    for contact in CONTACTS:
        # Проверка на предмет наличия контакта в списке контактов
        #  Просьба ввести номер параметра, который нужно изменить, с последующим изменением
        i_wanna_change = input("\nВведите цифру поля, которое хотите отредактировать и нажмите 'Enter'.\n"
                               "Чтобы выйти - просто нажмите 'Enter'.\n>>> ")
        if i_wanna_change == "1":
            contact["name"] = input("Введите новое имя контакта.\n>>> ")
        elif i_wanna_change == "2":
            contact["birthday"] = enter_birthday()
        elif i_wanna_change == "3":
            contact["address"] = str(input("Введите новый адресс контакта.\n>>> "))
        elif i_wanna_change == "4":

            contact["phones"] = wanna_add_or_change_phone()
        elif i_wanna_change == "5":
            contact["email"] = enter_email()
        elif i_wanna_change == "":
            return "Вы завершили редактирование контакта. Никаких изменений не произошло."
        return f'Изменения успешно сохранены'
