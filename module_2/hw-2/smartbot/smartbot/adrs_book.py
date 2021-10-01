import json
from abc import abstractmethod, ABC
from collections import UserDict
import re
from datetime import datetime

# class AbstractAssistant(ABC):
#
#     @abstractmethod
#     def add_record(self, record, records):
#         pass
#
#     @abstractmethod
#     def remove_record(self, record, records):
#         pass
#
#     @abstractmethod
#     def change_record(self):
#         pass
#
#     @abstractmethod
#     def show_records(self):
#         pass

records = []


class Assistant():

    def add_record(self, record):
        records.append(record)
        print(records)

    def edit_record(self, record, new_record, records):
        pass

    def show_record(self, record):
        pass

    def show_all(self, records):
        pass

    def delete_record(self, record):
        pass


class AddressBook(Assistant):
    def __init__(self, record):
        super().__init__(record)


# class NoteBook(Assistant):
#     def __init__(self, record):
#         super().__init__(record)


# class Record:
#
#     def __init__(self, name):
#         self._name = name
#
#     record = {}
#
#     @property
#     def value(self):
#         return self._name
#
#     @value.setter
#     def value(self, names):
#         self._name = names
#
#     def __str__(self):
#         return f"{self.__class__.__name__}: {self._name}"



class Name:
    def __init__(self, name):
        self._name = name

    @property
    def value(self):
        return self._name

    @value.setter
    def value(self, name):
        self._name = name

    def __str__(self):
        return f"{self.__class__.__name__}: {self._name}"


#
#
# class Phone:
#     pass
#
#
# class Address:
#     pass
#
#
# class Email:
#     pass
#
#
# class Birthday:
#     pass


if __name__ == "__main__":
    # ab = Assistant()
    # ab.add_record('address')
    # ab.add_record('phones')

    file = 'D:\Admin\GitHub\Python\python-hw\module_2\hw-2\smartbot\jfile.json'

    rec = Record(Name('Yurii'))
    rec.create_record()

    name = Name('Yurii').value

    print(name)

    # with open(file, 'w') as fh:
    #     json.dump(rec, fh)
