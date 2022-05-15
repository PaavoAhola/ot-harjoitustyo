import os

from entities.user import User
from entities.repositories import UserRepository

DIRNAME = os.path.dirname(__file__)

USERS = UserRepository(os.path.join(DIRNAME, "data", "users.csv"))

def login():
    symbol = input("1: Kirjaudu sisään, 2: Luo uusi käyttäjä ")
    if symbol == "1":
        username = input("Käyttäjätunnus: ")
        passw = input("Salasana: ")
        if USERS.allow_login(username, passw):
            print(f"Tervetuloa, {username}!")
            user_info = users.fetch_user(username)
            return User(user_info[0],user_info[1])
        else:
            return False
    elif symbol == "2":
        return create_user(users)
        

def create_user(users):
    while True:
        name = input(
            "Syötä haluamasi käyttäjänimi (vähintään 3 merkkiä). Palaa takaisin syöttämällä 'X'.")
        if users.user_exists(name):
            print("Käyttäjänimi on jo olemassa. Valitse uusi.")
            continue
        if name == "X":
            return
        if len(name) > 2:
            break
        print("Liian lyhyt käyttäjänimi, kokeile uudestaan")
    number = False
    while not number:
        password = input(
            "Syötä haluamasi salasana. Käytä vähintään 8 merkkiä, joista vähintään yksi on numero.")
        if len(password) < 8:
            print("Liian lyhyt salasana, kokeile uudestaan.")
            continue
        if password == name:
            print("Älä käytä käyttäjätunnustasi salasanana. Syötä uusi salasana.")
            continue
        for i in password:
            try:
                number = int(i)
                number = True
            except:
                pass
        if not number:
            print("Salasanassa tulee olla ainakin 1 numero. Syötä uusi salasana.")

    print(f"Käyttäjätunnuksesi on nyt {name}. Hauskoja pelihetkiä!")
    users.create_user(name, password)
    new_user = User(name, password)
    return new_user
