def change(my_list: list):
    copied_list = my_list.copy()

    # print(my_list, id(my_list))
    # print(copied_list, id(copied_list))

    if len(copied_list) > 0:
        copied_list[0] = -1 * copied_list[0]
    else:
        print("Error, the list is empty")
    return copied_list


x = change([1, 2, 3])
