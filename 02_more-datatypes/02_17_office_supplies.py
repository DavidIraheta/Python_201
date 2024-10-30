# Using f-strings, print out the name, last name, and favorite
# office supply item of each person in the given dictionary,
# formatted like so:
#
# LASTNAME, Name           Office supply item
# LONGERLASTNAME, Name     Office supply item

office = [
    {"full_name": "Michael Scott", "item": "world's best boss mug"},
    {"full_name": "Dwight Schrute", "item": "pepper spray"},
    {"full_name": "Jim Halpert", "item": "phone"},
    {"full_name": "Pam Beesly", "item": "post-its"},
    {"full_name": "Ryan Howard", "item": "business cards"},
    {"full_name": "Stanley Hudson", "item": "crossword-puzzle"},
    {"full_name": "Kevin Malone", "item": "m&ms"},
    {"full_name": "Meredith Palmer", "item": "flask"},
    {"full_name": "Angela Martin", "item": "cat food"},
    {"full_name": "Oscar Martinez", "item": "calculator"},
    {"full_name": "Phyllis Lapin", "item": "cut flowers"},
    {"full_name": "Kelly Kapoor", "item": "People magazine"},
    {"full_name": "Toby Flenderson", "item": "files"},
    {"full_name": "Creed Bratton", "item": "mung beans"},
    {"full_name": "Darryl Philbin", "item": "forklift"},
# ]

for x in range(len(office - 1)):
for i in range(len(office - x i1)):
    name = office[x]["full_name"].split()
    last_name = name[1].upper()
    first_name = name[0]
    item = office[x]["item"]
    print(f"{last_name}, {first_name:<10} {item}")


# office_favorites = []
# office_favorites.sort(len"full_name".split()[1])
# max_last_name_length = max(len(person["full_name"].split()[1]) for person in office)
# for person in office:
#     name = person["full_name"].split()
#     last_name = name[1].upper()
#     first_name = name[0]
#     item = person["item"]
#     office_favorites.append(f"{last_name}, {first_name:<10} {item}")
#     print(f"{last_name:<{max_last_name_length}}, {first_name:<10} {item}")



# for item in office_favorites:
#     print(item)
