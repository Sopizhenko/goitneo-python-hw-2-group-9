from collections import UserDict

class Field:
	def __init__(self, value):
		self.value = value


	def __str__(self):
		return str(self.value)


class Name(Field):
	def __init__(self, name):
		super().__init__(name)


class Phone(Field):
	def __init__(self, phone):
		if len(phone) != 10 or not phone.isdigit():
			raise ValueError("Phone number must be 10 digits long.")
		super().__init__(phone)


class Record:
	def __init__(self, name):
		self.name = Name(name)
		self.phones = []


	def __str__(self):
		return f"Contact name: {self.name}, phones: {', '.join(map(str, self.phones))}"


	def add_phone(self, phone):
		self.phones.append(Phone(phone))


	def remove_phone(self, phone):
		for p in self.phones:
			if p.value == phone:
				self.phones.remove(p)
				break


	def edit_phone(self, phone, new_phone):
		for p in self.phones:
			if p.value == phone:
				p.value = new_phone
				break


	def find_phone(self, phone):
		for p in self.phones:
			if p.value == phone:
				return p


class AddressBook(UserDict):
	def add_record(self, record):
		self.data[record.name.value] = record
		print(f"Record with name: {record.name} added to address book.")


	def find(self, name):
		record = self.data.get(name)
		if record:
			return record
		else:
			print(f"No such record with name: {name} in address book.")


	def delete(self, name):
		record_to_delete = self.data.get(name)
		if record_to_delete:
			del self.data[name]
			print(f"Record with name: {name} deleted.")
		else:
			print(f"No such record with name: {name} in address book.")