def func():
    assert False


def test_func():
    try:
        variable = func()
    except Exception as e:
        variable = None
    finally:
        return variable


vld_creator = test_func()
print(vld_creator)
