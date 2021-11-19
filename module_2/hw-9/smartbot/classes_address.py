from abc import abstractmethod, ABC


class Assistant(ABC):

    @abstractmethod
    def add_record(self, record, records):
        pass

    @abstractmethod
    def remove_record(self, record, records):
        pass

    @abstractmethod
    def change_record(self):
        pass

    @abstractmethod
    def show_records(self):
        pass


class AddressBook(Assistant):
    def __init__(self, record):
        super().__init__(record)


class NoteBook(Assistant):
    def __init__(self, record):
        super().__init__(record)


class Record:
    pass


class Name:
    pass


class Phone:
    pass


class Address:
    pass


class Email:
    pass


class Birthday:
    pass
