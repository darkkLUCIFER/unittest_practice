class Supervisor:

    def __init__(self, username, password, phone_number=None):
        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.__is_logged_in = False

    @classmethod
    def sample(cls):
        return cls('ali', '123', '09351234567')

    @classmethod
    def login(cls, username, password):
        supervisor = cls(username, password)
        supervisor.__is_logged_in = True
        return supervisor

    def protected(self):
        if self.__is_logged_in:
            return [1, 2, 3]
        raise ValueError()
