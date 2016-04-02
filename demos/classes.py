class AddressBookEntry:
  def setup(self, name, phone_number):
    self.name = name
    self.phone_number = phone_number

  def area_code(self):
    return self.phone_number.split('-')[0]

# me = AddressBookEntry()
AddressBookEntry.setup(AddressBookEntry(), 'matt', '503-123-4567')
AddressBookEntry.area_code(AddressBookEntry())






# me = AddressBookEntry()
# me.setup('matt', '503-123-4567')
# me.area_code()
