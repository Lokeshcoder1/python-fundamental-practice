import json

class Contact:
    def __init__(self,name,phone,email=''):
        self.name=name
        self.phone=phone
        self.email=email

    def __str__(self):
        return f"name :{self.name}\ncontact :{self.phone}\nemail :{self.email}"

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

    def add_contact(self,name,phone,email=''):
        contact=Contact(name,phone,email)
        self.contacts.append(contact)
        return f"Contact Added successfully in the contact book!"

    def del_contact(self,name):
        for i,contact in enumerate(self.contacts):
            if contact.name.lower()==name.lower():
                del self.contacts[i]
                return True
            return None

    def search_contact(self,name):
        for contact in self.contacts:
            if contact.name.lower()==name:
                print(contact)
                return True
            return None

    def list_all_contacts(self):
        for contact in self.contacts:
            print(contact)
            print()

class FileStorage:
    def __init__(self,filename='contactbook.json'):
        self.filename=filename

    def save_to_file(self,cb):
        data=[con.to_dict() for con in cb.contacts]
        with open(self.filename,'w') as f:
            json.dump(data,f,indent=2)

    def load_from_file(self):
        try:
            with open(self.filename,'r') as f :
                data=json.load(f)
            return  [Contact.from_dict(item) for item in data]
        except FileNotFoundError:
            return []



if __name__=='__main__':
    storage=FileStorage()
    loaded_contacts=storage.load_from_file()
    cb=ContactBook(loaded_contacts)

    while True:
        print('    CONTACT BOOK')
        print('1.Add contact\n2.Remove contact\n3.search contact\n4.List of the all the contacts')
        command=int(input("Enter the options : "))

        if command==1:
            name=input('Enter Name : ')
            phone=input('Enter mobile no : ')
            email=input('Enter email : ')
            cb.add_contact(name,phone,email)
            storage.save_to_file(cb)
        elif command==2:
            name=input('Enter name to del : ')
            cb.del_contact(name)
            storage.save_to_file(cb)
        elif command==3:
            name=input('Enter name to search : ')
            print(cb.search_contact(name))
        elif command==4:
                cb.list_all_contacts()
        elif command==5:
            print('Thank you for visiting!')
            storage.save_to_file(cb)
            break







