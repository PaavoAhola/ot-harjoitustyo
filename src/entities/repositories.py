from os import listdir
from os.path import isfile, join
from pathlib import Path
import pickle

class UserRepository:
    def __init__(self, file_path):
        self._file_path = file_path

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def allow_login(self, username, password):
        if self.user_exists(username):
            if self.password_correct(username, password):
                return True
            else:
                return False
        else:
            return False

    def create_user(self,username,password):
        self._ensure_file_exists()
        with open(self._file_path, "a", encoding="utf8") as file:
            file.write(f"{username};{password}\n")

    def user_exists(self, username):
        self._ensure_file_exists()
        with open(self._file_path, encoding="utf8") as file:
            for row in file:
                parts = row.split(";")
                if parts[0] == username:
                    return True
            return False

    def password_correct(self, username, password):
        self._ensure_file_exists()
        with open(self._file_path, encoding="utf8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")
                if parts[0] == username:
                    if parts[1] == password:
                        return True
                    return False
            return False

    def fetch_user(self, username):
        self._ensure_file_exists()
        with open(self._file_path, encoding="utf8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")
                if parts[0] == username:
                    return parts


class CrosswordRepository:
    def __init__(self, file_path):
        self._file_path = file_path

    def save(self,crossword):
        for f in listdir(self._file_path + "/saved"):
            if f == f"{crossword.name}.txt":
                print("Haluatko korvata samannimisen ristikon?")
                choice = input("1: Kyllä, 2: Ei")
                if choice == "2":
                    return 
        filehandler = open(f"{self._file_path}/saved/{crossword.name}.txt", "wb")
        pickle.dump(crossword, filehandler)
        print("Ristikkosi on tallennettu.")

    def publish(self,crossword):
        for f in listdir(self._file_path + "/published"):
            if f == f"{crossword.name}.txt":
                print("Haluatko korvata samannimisen ristikon?")
                choice = input("1: Kyllä, 2: Ei")
                if choice == "2":
                    return
        filehandler =  open(f"{self._file_path}/published/{crossword.name}.txt", "wb")
        pickle.dump(crossword, filehandler)
        print("Ristikkosi on julkaistu muiden pelattavaksi.")

    def load(self,name):
        filehandler = open(f"{self._file_path}/saved/{name}", "rb")
        return pickle.load(filehandler)

    def play(self,name):
        filehandler = open(f"{self._file_path}/published/{name}", "rb")
        return pickle.load(filehandler)
