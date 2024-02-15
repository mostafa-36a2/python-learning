import sys


def func():
    exit()


try:
    func()
except SystemExit as e:
    print("SystemExit!!")
except:
    print(sys.exc_info()[0])
finally:
    print("LOL")
