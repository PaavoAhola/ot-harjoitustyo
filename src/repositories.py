from pathlib import Path

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
