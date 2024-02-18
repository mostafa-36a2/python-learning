class MyClass(object):
    @classmethod
    def _new_instance(cls, blah):
        print(blah)

MyClass._new_instance("blah")
