from collections import UserDict

class Field:
    def __init__(self, name, phone, email):
        self.name = name    # Mandatory
        self.phone = phone  # Optional | multiple
        self.email = email  # Optional

class Name:
    pass

class Phone:
    pass

class Record:
    pass

class AddressBook(UserDict):
    pass
