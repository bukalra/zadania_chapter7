from faker import Faker
faker = Faker()

class BaseContact:
    def __init__(self, name, last_name, private_number, email):
        self.name = name
        self.last_name = last_name
        self.private_number = private_number
        self.email = email
        self.lable_lenght = len(self.name) + len(self.last_name)
    def contact(self):
        print(f'I am calling to {self.name} {self.last_name} using business number {self.private_number}')

class BusinessContact(BaseContact):
    def __init__(self, company, position, business_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.business_number = business_number
        self.lable_lenght = len(self.name) + len(self.last_name)
    def contact(self):
        print(self.company, self.position, self.business_number)
        print(f'I am calling to {self.name} {self.last_name} using business number {self.business_number}')

def create_contact(type, quantity):
    if type == 1:
        i = 0
        while i < quantity:
            name = faker.first_name()
            last_name = faker.last_name()
            private_number = faker.phone_number()
            business_number = faker.phone_number()
            company = faker.company()
            email = name+'.'+last_name+'@'+faker.free_email_domain()
            position = faker.job()
            card = BaseContact(name, last_name, private_number, email)
            card.contact()
            i += 1
    if type == 2:
        i = 0
        while i < quantity:
            name = faker.first_name()
            last_name = faker.last_name()
            private_number = faker.phone_number()
            business_number = faker.phone_number()
            company = faker.company()
            email = name+'.'+last_name+'@'+faker.free_email_domain()
            print(email)
            position = faker.job()
            print(position)
            card = BusinessContact(company, position, business_number, name, last_name, private_number, email)
            card.contact()
            i += 1

type = int(input('What type of contact you want to create: 1.Private, 2.Business '))
quantity = int(input('How many contacts you want to create: '))
create_contact(type, quantity)
