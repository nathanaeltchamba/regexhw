import re

file = open('./names.txt', encoding='utf-8')

data = file.read()

file.close()

person_filter = re.findall('''

                        ([\w]+,\s[\w]+)                         # name
                        (\t\s[\w\d+.-]+@[\w\d]+.com)            # email
                        (\t\s\(?\d{3}\)?\s?-?\d{3}-\d{4})       # phone
                        (\t\s[\w]+\s[\w]+\s[\w]+\s[\w]+,)       # title 
                        (\s@[\w\d.+]+)                          # twitter


''', data, re.X)


people = []
                                            # I don't know why person_dict is not defined
for person in person_filter:
    person_dict = {
        'name': person[0],
        'email': person[1],
        'phone': person[2],
        'title': person[3],
        'twitter': person[4]
    }

# people.append(person_dict)

# print(people[0]['phone'])

# compiled search

contact_search = re.compile('''
                        (?P<Name>[\w]+,\s[\w]+)                         # name
                        (?P<Email>\t\s[\w\d+.-]+@[\w\d]+.com)            # email
                        (?P<Phone>\t\s\(?\d{3}\)?\s?-?\d{3}-\d{4})       # phone
                        (?P<Title>\t\s[\w]+\s[\w]+\s[\w]+\s[\w]+,)       # title 
                        (?P<Twitter>\s@[\w\d.+]+)                          # twitter
 ''', re.X)

for i in contact_search.finditer(data):
    print(f"Name: {i.group('name')}\nEmail: {i.group('email')}\nPhone: {i.group('phone')}\nTitle: {i.group('title')}\nTwitter: {i.group('twitter')}")

        

