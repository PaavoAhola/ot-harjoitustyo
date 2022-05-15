import os
from datetime import datetime

from entities.crosswords import Crossword
from entities.user import User
from entities.repositories import UserRepository, CrosswordRepository
from functions.menu import create_user
from functions.using_crosswords import create_crossword, play_crossword

def run_menu():
    dirname = os.path.dirname(__file__)

    users = UserRepository(os.path.join(dirname, "data", "users.csv"))
    crosswords = CrosswordRepository(os.path.join(dirname, "data", "crosswords"))


    login = False

    while True:
        symbol = input("1: Kirjaudu sisään, 2: Luo uusi käyttäjä ")
        if symbol == "1":
            username = input("Käyttäjätunnus: ")
            passw = input("Salasana: ")
            if users.allow_login(username, passw):
                print(f"Tervetuloa, {username}!")
                login = True
                user_info = users.fetch_user(username)
                user = User(user_info[0],user_info[1])
                break
            print("Väärä käyttäjätunnus tai salasana.")
        elif symbol == "2":
            user = create_user(users)
            login = True
            break

    if login:
        while True:
            print("-------------------------------------------------------------")
            print("1: Pelaa")
            print("2: Luo sanaristikko")
            print("3: Muokkaa keskeneräistä sanaristikkoa")
            print("4: Tilastot")
            print("5: Kirjaudu ulos")
            choice = input("Valitse 1-5: ")
            if choice == "1":
                options = False
                for f in os.listdir(os.path.join(dirname, "data", "crosswords", "published")):
                    ff = crosswords.play(f)
                    print(f"{ff.name} by {ff.creator}")
                    options = True
                if not options:
                    print("Ei saatavilla olevia ristikoita")
                    continue
                pick = input("Kirjoita haluamasi ristikon nimi (ei tekijän nimeä): ")
                crossword = crosswords.play(pick + ".txt")
                for i in range(10):
                    for j in range(10):
                        crossword.squares[i][j].insert_letter(" ")
                correct_crossword = crosswords.play(pick + ".txt")
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
                    crosswords.publish(correct_crossword)

            elif choice == "2":
                name = input("Anna sanaristikollesi nimi: ")
                crossword = Crossword(name, user.return_name())
                create_crossword(crossword)
                pick = input("1: Julkaise, 2: Tallenna, 3: Hylkää ")
                if pick == "1":
                    crosswords.publish(crossword)
                elif pick == "2":
                    crosswords.save(crossword)

            elif choice == "3":
                no_works = True
                for f in os.listdir(os.path.join(dirname, "data", "crosswords", "saved")):
                    ff = crosswords.load(f)
                    if ff.creator == user.return_name():
                        print(ff.name)
                        no_works = False
                if no_works:
                    print("Sinulla ei ole keskeneräisiä projekteja")
                else:
                    pick = input("Kirjoita haluamasi ristikon nimi: ")
                    crossword = crosswords.load(pick + ".txt")
                    create_crossword(crossword)
                    pick = input("1: Julkaise, 2: Tallenna, 3: Hylkää")
                    if pick == "1":
                        crosswords.publish(crossword)
                    elif pick == "2":
                        crosswords.save(crossword)

            elif choice == "4":
                results = False
                for f in os.listdir(os.path.join(dirname, "data", "crosswords", "published")):
                    ff = crosswords.play(f)
                    ff.show_highscores()
                    results = True
                if not results:
                    print("Ei tilastoja")

            elif choice == "5":
                user = None
                print("Sinut on kirjattu ulos. Nähdään taas!")
                break
