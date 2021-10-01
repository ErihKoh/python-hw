import json
from pathlib import Path

from adrs_book import AddressBook, Name, Phone, Record, Birthday, Address, Email


def add_contact() -> Record:
    # Собранная функция добавления контакта
    # Не принимает аргументов, возвращает словарь с проверенными значениями имени, телефона (телефонов),
    # и по желанию - почта и день рождения
    name = input("Введите имя контакта: ")
    birthday = input("Введите день рождения контакта: ")
    address = input("Введите адрес контакта: ")
    phones = input("Введите номер контакта: ")
    email = input("Введите почту контакта: ")

    return Record(Name(name), Phone(phones), Birthday(birthday), Address(address), Email(email))


if __name__ == "__main__":
    FILES = Path() / 'files'
    FILES.mkdir(exist_ok=True)
    file = './files/address_book.json'
    # result = add_contact()
    res = add_contact()
    s = res.create()
    print(s)

    with open(file, 'w') as fh:
        json.dump(s, fh)
