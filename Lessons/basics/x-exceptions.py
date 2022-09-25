import random

class mostafa(BaseException):
    pass

try:
    r =random.random()
    if r < 0.2:
        raise Exception("Hello World!")
    elif r < 0.5:
        raise ValueError("Hello World!")
    elif r < 0.8:
        raise mostafa("Hello World!")
    else:
        raise TypeError("Hello World!")
except mostafa as e:
    print(f"Oops, mostafa happened: {e}")
except TypeError as e:
    print(f"Oops, TypeError happened: {e}")
except ValueError as e:
    print(f"Oops, ValueError happened: {e}")
except Exception as e:
    print(f"Oops, an error happened: {e}")