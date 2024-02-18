def get_list_of_numbers():
    file_path = (
        "/home/mostafa/Documents/Python/Lessons/Projects/x-clustering/numbers.txt"
    )
    res = []
    with open(file_path, "r") as input_file:
        return [int(line.strip()) for line in input_file.readlines()]


def scale_list(numbers, max_bar=100):
    """
    >>> scale_list([10, 20, 30, 40, 50])
    [0.0, 25.0, 50.0, 75.0, 100.0]
    >>> scale_list([10, 50])
    [0.0, 100.0]
    """
    # find the minimum and maximum values in the list
    min_num = min(numbers)
    max_num = max(numbers)

    # scale each number to be between 0 and max_bar
    scaled_nums = []
    for num in numbers:
        scaled_num = int(((num - min_num) / (max_num - min_num)) * max_bar)
        scaled_nums.append(scaled_num)

    return scaled_nums


def shift_list_to_zero(numbers):

    # find the minimum and maximum values in the list
    min_num = min(numbers)
    max_num = max(numbers)

    # scale each number to be between 0 and max_bar
    shifted_nums = []
    for num in numbers:
        # scaled_num = int(((num - min_num) / (max_num - min_num)))
        shifted_num = int(num - min_num)
        shifted_nums.append(shifted_num)

    return shifted_nums
