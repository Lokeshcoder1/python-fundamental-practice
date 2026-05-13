class Contact:
    def __init__(self,name,phone,email=''):
        self.name=name
        self.phone=phone
        self.email=email

    def __str__(self):
        return (f"name :{self.name}\n"
                f"contact :{self.phone}\n"
                f"email :{self.email}")

    def to_dict(self):
        return {'name':self.name,
                'phone':self.phone,
                'email':self.email}

    @classmethod
    def from_dict(cls,data):
        contact=cls(data['name'],data['phone'],data['email'])
        return contact

class ContactBook:
    def __init__(self,contacts=None):
        self.contacts=contacts if contacts is not None else []

    def all_contacts(self):
        contacts=[str(con) for con in self.contacts]
        return contacts

    def add_contact(self,name,phone,email=''):
        contact=Contact(name,phone,email)
        self.contacts.append(contact)



    def list_all_contacts(self):
        for c in self.all_contacts():
            print(c)


cb=ContactBook()
cb.add_contact('lokesh',9989370804,'lokeshmanishankarg@gmail.com')
cb.add_contact('loki',9989371804,'lokeshmanishankar@gmail.com')
cb.del_contact('lokesh')
print(cb.list_all_contacts())




