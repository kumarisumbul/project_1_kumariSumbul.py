from Singleton_decorator import singleton

@singleton
class MyDriver:

    @staticmethod
    def get_driver(self):
        driver = webdriver.Chrome()
        return driver

print(MyDriver.get_driver())
