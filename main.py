from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value


class Phone(Field):
    def __init__(self, value=None):
        if value is not None:
            self.value = value
        else:
            self._value = None

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        value = value.strip()
        value = value.replace("+", "").replace("(", "").replace(")", "")

        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be 10 digits")
        else:
            self._value = value


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p

    def edit_phone(self, old_phone, new_phone):
        finded_phone = self.find_phone(old_phone)
        if finded_phone:
            finded_phone.value = new_phone
        else:
            raise ValueError("Phone not found")
        
    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if self.find(name):
            del self.data[name]
        else:
            print("Contact not found")