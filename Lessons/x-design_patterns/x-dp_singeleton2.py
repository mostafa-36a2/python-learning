class my_class:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y


my_class_object: my_class = None


def init_object(x, y):
    global my_class_object
    if my_class_object:
        return my_class_object
    else:
        my_class_object = my_class(x, y)
        return my_class_object


def get_object():
    return my_class_object


init_object(1, 2)
print(my_class_object.x, my_class_object.y)
