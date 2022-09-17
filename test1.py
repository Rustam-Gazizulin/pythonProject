class Player:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def get_name(self):
        return self.__name


user_1 = Player("Jhon")
name = user_1.name
print(name)