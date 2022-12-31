from Singleton_decorator import singleton


@singleton
class YourClass:

    def print_hi(self):
    return 'Hi'

obj1 = YourClass()
print(obj1)
print(obj1.print_hi())
obj2 = YourClass()
print(obj2)
print(obj2.print_hi())