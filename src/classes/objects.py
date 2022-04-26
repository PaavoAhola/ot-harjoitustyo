class Users:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)


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
        self.squares = []
        for i in range(10):
            self.squares.append([])
        for i in range(10):
            for j in range(10):
                self.squares[i].append(Square(i,j))

    def add_highscore(self, time, user):
        self.highscores.append((time, user))
        if len(self.highscores) == 11:
            self.highscores.sort()
            self.highscores.pop()

class Square:
    def __init__(self, x, y):
        self.letter = None
        self.on = True
        self.position = (x,y)
        self.surface = None

    def switch(self):
        if self.on:
            self.on = False
        else:
            self.on = True

    def insert_letter(self, x):
        self.letter = x
