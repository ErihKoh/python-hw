from abc import ABC, abstractmethod
import pickle
import json


class SerializationInterface(ABC):

    def __init__(self, file_name, some_data):
        self.file_name = file_name
        self.some_data = some_data

    @abstractmethod
    def write_file(self, data):
        pass

    @abstractmethod
    def read_file(self, data):
        pass


class SerializationBin(SerializationInterface):
    def __init__(self, file_name, some_data):
        super().__init__(file_name, some_data)

    def write_file(self, **kwargs):
        with open(self.file_name, "wb") as fh:
            pickle.dump(self.some_data, fh)

    def read_file(self, **kwargs):
        with open(self.file_name, "rb") as fh:
            unpacked = pickle.load(fh)
            print(unpacked)
        return unpacked


class SerializationJson(SerializationInterface):
    def __init__(self, file_name, some_data):
        super().__init__(file_name, some_data)

    def write_file(self, **kwargs):
        with open(self.file_name, "w") as fh:
            json.dump(self.some_data, fh)

    def read_file(self, **kwargs):
        with open(self.file_name, "r") as fh:
            unpacked = json.load(fh)
            print(unpacked)
        return unpacked


file_bin_name = "data.bin"
file_json_name = "data.json"
data_for_save = "Hello world!"

# test_obj_bin = SerializationBin(file_bin_name, data_for_save)
# test_obj_json = SerializationJson(file_json_name, data_for_save)
# test_obj_bin.write_file()
# test_obj_json.write_file()

if __name__ == "__main__":
    pass
