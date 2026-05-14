import json
from pathlib import Path
from dataclasses import dataclass,asdict

@dataclass
class Contact:
    name:str
    phone:str
    email:str =''

class ContactBook:
    def __init__(self):
        self.contacts=[]

    def add_contact(self,name,phone,email=''):
        contact=Contact(name,phone,email)
        self.contacts.append(contact)
        return True

    def del_contact(self,name):
        for i,contact in enumerate(self.contacts):
            if contact.name.lower()==name.lower():
                del self.contacts[i]
                return True
        return False

    def search_contact(self,name):
        for contact in self.contacts:
            if contact.name.lower()==name:
                return contact
        return None

    def list_all_contacts(self):
        for contact in self.contacts:
            print(f'    Contact of {contact.name}\nName :{contact.name}\nPhone No: {contact.phone}\nEmail ID : {contact.email}')
            print()

    def save_to_file(self,filename:str='contactbook.json'):
        data=[asdict(contact) for contact in self.contacts]
        try:
            with open(filename,'w') as f:
                json.dump(data,f,indent=2)
        except IOError:
            return"Error occured"

    def load_from_file(self,filename:str='contactbook.json'):
        filepath=Path(filename)
        try:
            with open(filepath,'r')as f:
                data=json.load(f)
            self.contacts=[Contact(**item) for item in data ]
        except(json.JSONDecodeError,IOError):
            return []

if __name__=='__main__':
    cb=ContactBook()
    cb.load_from_file()


    while True:
        print('    CONTACT BOOK')
        print('1.Add contact\n2.Remove contact\n3.search contact\n4.List of the all the contacts\n5.To exit')
        command=int(input("Enter the options : "))

        if command==1:
            name=input('Enter Name : ')
            phone=input('Enter mobile no : ')
            email=input('Enter email : ')
            cb.add_contact(name,phone,email)
            cb.save_to_file()
        elif command==2:
            name=input('Enter name to del : ')
            cb.del_contact(name)
            cb.save_to_file()
        elif command==3:
            name=input('Enter name to search : ')
            print(cb.search_contact(name))
        elif command==4:
                cb.list_all_contacts()
        elif command==5:
            print('Thank you for visiting!')
            cb.save_to_file()
            break







