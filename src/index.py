import os
from objects import User
from repositories import UserRepository

dirname = os.path.dirname(__file__)

users = UserRepository(os.path.join(dirname, "data", "users.csv"))


def create_user():
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


while True:
    symbol = input("Valitse 1, jos haluat kirjautua sisään. Valitse 2, jos haluat luoda uuden käyttäjän")
    if symbol == "1":
        username = input("Käyttäjätunnus:")
        passw = input("Salasana:")
        if users.allow_login(username, passw):
            print(f"Tervetuloa, {username}!")
            user_info = users.fetch_user(username)
            user = User(user_info[0],user_info[1])
            break
        print("Väärä käyttäjätunnus tai salasana.")
    elif symbol == "2":
        user = create_user()
        break

