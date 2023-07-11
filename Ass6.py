def ds(roll_no, Name):
    my_list = [roll_no, Name]
    my_tuple = (roll_no, Name)
    my_set = {roll_no, Name}
    my_dict = {'roll_no': roll_no, 'Name': Name}
    print("Initial data structures:")
    print("List:", my_list)
    print("Tuple:", my_tuple)
    print("Set:", my_set)
    print("Dictionary:", my_dict)
    new_roll_no = input("Enter a new roll number: ")
    new_Name = input("Enter a new Name: ")
    my_list[0] = new_roll_no
    my_list[1] = new_Name
    my_tuple = (new_roll_no, new_Name)
    my_set.remove(roll_no)
    my_set.add(new_roll_no)
    my_set.remove(Name)
    my_set.add(new_Name)
    my_dict['roll_no'] = new_roll_no
    my_dict['Name'] = new_Name
    print("Data structure updated:")
    print("List:", my_list)
    print("Tuple:", my_tuple)
    print("Set:", my_set)
    print("Dictionary:", my_dict)
    del my_list
    del my_tuple
    del my_set
    del my_dict
ds("10", "Nirmit")