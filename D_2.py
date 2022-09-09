

class UserInterface:
    def get_user(self):
        print("user")


class UserA(UserInterface):
    def get_user(self):
        print("user a")


# a = UserA()
# a.get_user()


class UserB(UserInterface):
    def get_user(self):
        print("user b")


def all_users(user: UserInterface):
    user.get_user()


