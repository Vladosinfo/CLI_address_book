from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
        # self.phone = phone  # Optional | multiple
        # self.email = email  # Optional


    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

    def validate(self):
        pass


class Record:
    def __init__(self, name):
        self.name = Name(name)  # Mandatory
        self.phones = []

    # def add_name(self):
    #     pass

    def add_phone(self, phone):
        self.phones.append(phone)

    def edit_phone(self):
        pass

    def remove_phone(self):
        pass

    def find_phone(self):
        pass


    def __str__(self):
        return f"Name: {self.name.value}; phones: {'; '.join(p for p in self.phones)}"
    

class AddressBook(UserDict):
    
    def add_record(self, value):
        self.data[value.name] = value.phones


    def find(self):
        pass

    def delete(self):
        pass



def main():
    abook = AddressBook()
    john_record = Record("John")
    john_record.add_phone("0962455835")
    john_record.add_phone("7777777777")

    abook.add_record(john_record)

    for name, record in abook.data.items():
        print(f"Name: {name}, record: {record}")


if __name__ == "__main__":
    main()