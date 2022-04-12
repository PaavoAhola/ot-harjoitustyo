from objects import User


def create_user():
    while True:
        name = input(
            "Syötä haluamasi käyttäjänimi (vähintään 3 merkkiä). Palaa takaisin syöttämällä 'X'.")
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
                x = int(i)
                number = True
            except:
                pass
        if not number:
            print("Salasanassa tulee olla ainakin 1 numero. Syötä uusi salasana.")

    print(f"Käyttäjätunnuksesi on nyt {name}. Hauskoja pelihetkiä!")
    new_user = User(name, password)
    return new_user


create_user()
