class LazyVariable:
    def __init__(self, value_function):
        self._value_function = value_function
        self._value = None

    @property
    def value(self):
        if self._value is None:
            self._value = self._value_function()
        return self._value

    def __repr__(self):
        return self.value


# Example usage:
def calculate_value():
    print("Calculating value...")
    return 42


lazy_var = LazyVariable(calculate_value)
# The value is not calculated yet
print("Accessing value for the first time:", lazy_var.value)
# The value is calculated now
print("Accessing value for the second time:", lazy_var.value)
