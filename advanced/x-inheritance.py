class B:
    def __init__(self):
        print("From B: ", type(self).__name__)


class C(B):
    def __init__(self):
        print("From C: ", type(self).__name__)
        super().__init__()


x = C()
