class PasswordManager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        return self.old_passwords[-1]

    def set_password(self, password):
        if password not in self.old_passwords:
            self.old_passwords.append(password)
        else:
            print('Incorrect password')

    def is_correct(self, password):
        return password == self.get_password()


password_manager = PasswordManager()
password_manager.set_password('qwerty')
print(password_manager.get_password()) # -> qwerty
password_manager.set_password('user123')
print(password_manager.get_password()) # -> user123
password_manager.set_password('qwerty')     # -> Incorrect password
print(password_manager.is_correct('user123'))  # -> True
