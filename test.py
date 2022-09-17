class Player:
    def __init__(self, name):
        self._name = name

    def set_name(self, new_name):
        self._name = new_name

    def get_name(self):
        return self._name


user_1 = Player("Jhon")
print(user_1.get_name())
user_1.set_name("I")
print(user_1.get_name())