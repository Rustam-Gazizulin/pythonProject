# class House:
#
#     def __init__(self, number, color, owner):
#         self.number = number
#         self.color = color
#         self.owner = owner
#
#     def get_owner(self):
#         return self.owner
#
#
# house1 = House(10, "red", "Jhon")
# house2 = House(11, "green", "Ivan")
# house3 = House(12, "black", "Olga")
#
# print(house1.color)
# owner_name = house2.get_owner()
# print(owner_name)
#
#
# class User:
#     def __init__(self, name, password):
#         self.name = name
#         self.password = password
#
#     def change_password(self, old_password, new_password):
#         self._is_password_correct(old_password)
#         self._is_password_valid(new_password)
#         self._was_password_used(new_password)
#
#     def _is_password_correct(self, old_password):
#         pass
#
#     def _is_password_valid(self, new_password):
#         pass
#
#     def _was_password_used(self, new_password):
#         pass
#
#
# user = User("Jhon", "12345")
#
# user.change_password()


class SomeClass:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def print(self):
        print(self._concat())

    def _concat(self):
        return f"{self.var1} {self.var2}"


object_1 = SomeClass(var1="Hello", var2="World")

object_1.print()
