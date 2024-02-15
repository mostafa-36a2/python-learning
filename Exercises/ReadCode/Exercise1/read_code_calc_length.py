def check_if_list_is_empty(list_var):
    try:
        list_var[0]
    except IndexError:
        # List is empty
        return True
    else:
        # List is not empty
        return False


def calculate_length(list_var: list):

    count = 1

    while not check_if_list_is_empty(list_var):
        list_var.pop()
        count += 1

    return count


def convert_string_to_list(string_variable):
    list_var = []
    for letter in string_variable:
        list_var.append(letter)
    return list_var


user_input = input("Please enter a string: ")

letters_list = convert_string_to_list(user_input)

print(letters_list)

print(f"Number of letters in input: {calculate_length(letters_list)}")

print(f"Number of letters in input: {calculate_length(letters_list)}")
