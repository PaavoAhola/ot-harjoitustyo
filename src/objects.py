class Users:
    def __init__(self):
        self.users = []

    def add_user(self, User):
        self.users.append(User)


class User:
    def __init__(self, name, password):
        self.__name = name
        self.__password = password
        self.own_crosswords = []
        self.saved_crosswords = []

    def return_name(self):
        return self.__name


class Crossword:
    def __init__(self):
        self.highscores = []

    def add_highscore(time, User):
        self.highscores.append((time, User))
        if len(self.highscores) == 11:
            self.highscores.sort()
            self.highscores.pop()
