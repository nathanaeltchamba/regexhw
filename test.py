# import re

# with open("names.txt") as file:
#     data = file.readlines()

# # file = open('./names.txt', encoding='utf-8')

# data = file.readlines()

# file.close()

# pattern = re.findall('([\w]+,[\w]+)', data)

# for item in data:
#         match = pattern.search(item)

#         if match:
#                 print(f'{match.group(3)}')
#         else:
#                 print('Getting there')




# Second version
import re

with open("names.txt")as f:
    data = f.readlines()
    
pattern = re.compile(("([A-Z][\w]+)([ \w ]*)([A-Z][\w]+)"))

# If only last name is needed

print(pattern.search(data[0]))

for person in data:
    match = pattern.search(person)
        
    if match:
        print(f"{match}")
        # print(f"{match.group(1)}{match.group(2)}{match.group(3)}")

    else:
        print(None)
        
# If full name is needed, as shown in the sample output above, use the below print statement:
print(f"{match.group(1)}{match.group(2)}{match.group(3)}")