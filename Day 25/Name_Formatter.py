def format_name(first_name, last_name):
    final_name=""
    final_firstname=""
    final_lastname=""
    for char1 in first_name:
        if char1 == first_name[0]:
            final_firstname+=char1.upper()
        else:
            final_firstname+=char1.lower()

    for char2 in last_name:
        if char2 == last_name[0]:
            final_lastname+=char2.upper()
        else:
            final_lastname+=char2.lower()
    final_name=final_firstname+" "+final_lastname
    return final_name

print(f"Your name in proper format is: {format_name(input("Input your first name below\n"), input("Input your last name below\n"))}")
