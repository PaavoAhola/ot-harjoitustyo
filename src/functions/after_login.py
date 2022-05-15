import os
from datetime import datetime

from entities.crosswords import Crossword
from entities.user import User
from entities.repositories import UserRepository, CrosswordRepository
from functions.menu import login
from functions.using_crosswords import create_crossword, play_crossword

DIRNAME = os.path.dirname(__file__)

USERS = UserRepository(os.path.join(DIRNAME, "data", "users.csv"))
CROSSWORDS = CrosswordRepository(os.path.join(DIRNAME, "data", "crosswords"))

def play_options():
    options = []
    for f in os.listdir(os.path.join(DIRNAME, "data", "crosswords", "published")):
        ff = CROSSWORDS.play(f)
        options.append(ff.name)
    return options
    
def play_environment(pick, user):
    crossword = CROSSWORDS.play(pick + ".txt")
    for i in range(10):
        for j in range(10):
            crossword.squares[i][j].insert_letter(" ")
    correct_crossword = CROSSWORDS.play(pick + ".txt")
    start_time = datetime.now()
    player_effort = play_crossword(crossword)
    correct = True
    for i in range(10):
        for j in range(10):
            if correct_crossword.squares[i][j].letter != player_effort.squares[i][j].letter:
                correct = False
    if correct:
        result = datetime.now()-start_time
        print(f"Hienoa! Aikasi oli {result}.")
        correct_crossword.add_highscore(result, user.return_name())
        CROSSWORDS.publish(correct_crossword)

def projects(user):
    works = []
    for f in os.listdir(os.path.join(DIRNAME, "data", "crosswords", "saved")):
        ff = crosswords.load(f)
        if ff.creator == user.return_name():
            works.append(ff.name)
    return works
    

def stats():
    results = False
    for f in os.listdir(os.path.join(DIRNAME, "data", "crosswords", "published")):
        ff = CROSSWORDS.play(f)
        ff.show_highscores()
        results = True
    return results
