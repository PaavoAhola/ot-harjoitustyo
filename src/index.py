import os

from classes.objects import User, Crossword
from classes.repositories import UserRepository
from functions.menu import create_user
from functions.using_crosswords import launch_crossword

dirname = os.path.dirname(__file__)

users = UserRepository(os.path.join(dirname, "data", "users.csv"))

login = False

while True:
    symbol = input("Valitse 1, jos haluat kirjautua sisään. Valitse 2, jos haluat luoda uuden käyttäjän")
    if symbol == "1":
        username = input("Käyttäjätunnus:")
        passw = input("Salasana:")
        if users.allow_login(username, passw):
            print(f"Tervetuloa, {username}!")
            login = True
            user_info = users.fetch_user(username)
            user = User(user_info[0],user_info[1])
            break
        print("Väärä käyttäjätunnus tai salasana.")
    elif symbol == "2":
        user = create_user()
        break

if login:
    choice = input("Luo sanaristikko valitsemalla 1")
    if choice == "1":
        crossword = Crossword()
        launch_crossword(crossword)
