class Crossword:
    def __init__(self, name, creator):
        self.name = name
        self.creator = creator
        self.highscores = []
        self.squares = []
        for i in range(10):
            self.squares.append([])
        for i in range(10):
            for j in range(10):
                self.squares[i].append(Square(i,j))

    def add_highscore(self, time, user):
        self.highscores.append((time, user))
        self.highscores.sort()
        if len(self.highscores) == 11:
            self.highscores.pop()

    def show_highscores(self):
        print(f"{self.name} by {self.creator}")
        tries = False
        for score in self.highscores:
            print(f"{score[1]}: {score[0]}")
            tries = True
        if not tries:
            print("Ei tuloksia")


class Square:
    def __init__(self, x, y):
        self.letter = " "
        self.on = True
        self.position = (x,y)
        self.surface = None
        self.hint_right = ""
        self.hint_down = ""

    def switch(self):
        if self.on:
            self.on = False
        else:
            self.on = True

    def insert_letter(self, x):
        self.letter = x
