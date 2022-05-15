class User:
    def __init__(self, name, password):
        self.__name = name
        self.__password = password

    def return_name(self):
        return self.__name
