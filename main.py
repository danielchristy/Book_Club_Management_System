from dataclasses import dataclass
from Book import *
from User import *

def print_fiction(fiction_booklist) -> str: #prints the fiction book list
    print(" --- Here are all the Fiction Books ---")
    for book in fiction_booklist:
        print(f"Title: {book.title} by {book.author}, Status: {book.read}, Rating: {book.rating}")

def print_nonfiction(nonfiction_booklist) -> str: #prints a the nonfiction book list
    print(" --- Here are all the Nonfiction Books ---")
    for book in nonfiction_booklist:
        print(f"Title: {book.title} by {book.author}, Status: {book.read}, Rating: {book.rating}")


fiction_booklist = [
    Book("To Kill A Mockingbird", "Harper Lee", "Unread", 0),
    Book("The Adventures of Sherlock Holmes", "Arthur Conan Doyle", "Unread", 0),
    Book("Frankenstein", "Mary Shelley", "Unread", 0),
    Book("The Hobbit", "J.R.R. Tolkien", "Unread", 0),
    Book("The Silence of the Lambs", "Thomas Harris", "Unread", 0),
]
nonfiction_booklist = [
    Book("The Situation Room", "George Stephanopoulos", "Unread", 0),
    Book("Black Hawk Down", "Mark Bowden", "Unread", 0),
    Book("Empire State of Mind", "Zack O'Malley Greenburg", "Unread", 0),
    Book("Astrophysics for People in a Hurry", "Neil deGrasse Tyson", "Unread", 0),
    Book("Hiroshima", "John Hersey", "Unread", 0),
]


def main():
    users = [User("admin", "admin")] #list of users
    book = Book("", "", "", 0) #instantiation of Book dataclass

    login_running = True
    book_running = False
    current_user = None

    print("Welcome to The Book Club\n")
    while True:
        if login_running:
            userinput = input("[Login], [Create] login, or [Quit] > ").lower().strip()
            if userinput == "login":
                current_user = login(users)
                if current_user is not None:
                    print(f"{current_user.username} has successfully signed in.")
                    login_running = False
                    book_running = True
                else:
                    print("Invalid username or password. \n")
            elif userinput == "create":
                new_user = create_login()
                users.append(new_user)
                print(f"{new_user.username} has successfully been created.\n")
            elif userinput == "quit":
                break
            else:
                print("Invalid choice\n")
                
        elif book_running:
            userinput = input("\nView [Fiction], View [Nonfiction], [Add] Book, [Update] Book, [Remove] Book, Sign [Out] > ").lower().strip()
            if userinput == "fiction":
                print_fiction(fiction_booklist)
            elif userinput == "nonfiction":
                print_nonfiction(nonfiction_booklist)
            elif userinput == "add":
                add_book(book, fiction_booklist, nonfiction_booklist)
            elif  userinput == "update":
                update_book(fiction_booklist, nonfiction_booklist)
            elif userinput == "remove":
                remove_book(fiction_booklist, nonfiction_booklist)
            elif userinput == "out":
                current_user = None
                book_running = False
                login_running = True
                print("\n")
            else:
                print("Invalid choice\n")

if __name__ == "__main__":
    main()