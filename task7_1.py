cards = [{'name': 'Joe', 'last_name': 'Doe', 'company':'Apple' , 'position':'manager' , 'email':'joe.doe@apple.com' },
{'name': 'Jake', 'last_name': 'Simson', 'company':'Google' , 'position':'developer' , 'email':'jake.simson@google.com' },
{'name': 'Bow', 'last_name': 'Black', 'company':'Cisco' , 'position':'sales' , 'email':'bow.black@cisco.com' },
{'name': 'Sammy', 'last_name': 'Frank', 'company':'Intel' , 'position':'director' , 'email':'sammy.frank@intel.com' },
{'name': 'July', 'last_name': 'Obama', 'company':'Miscosoft' , 'position':'CEO' , 'email':'july.obbama@ms.com' }
]

class BusinessCards:
    def __init__(self, name = 'Mark', last_name = 'Dowson', company = 'Orange', position = 'presales', email = 'mark.dowson@orange.com'):
        self.name = name
        self.last_name = last_name
        self.company = company
        self.position = position
        self.email = email

first_card = BusinessCards()

for each in cards:
    card = (BusinessCards(name = each['name'], last_name = each['last_name'], company = each['company'], position = each['position'], email = each['email']))
    print(card.name, card.last_name, card.email)