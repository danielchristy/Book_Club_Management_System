from dataclasses import dataclass

@dataclass
class User():
    username: str
    password: str

def login(users) -> User: #allows users to login if they have created a login
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    for user in users:
        if user.username == username and user.password == password:
            return user

def create_login() -> User: #allows users to create a login
    username = input("Choose a username: ").strip()
    password = input("Choose a password: ").strip()
    return User(username, password)