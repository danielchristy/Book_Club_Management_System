from dataclasses import dataclass
@dataclass
class Book:
    title: str
    author: str
    read: str
    rating: int

def add_book(book, fiction_booklist, nonfiction_booklist) -> Book: #Allows users to add books to book lists
    #Getting Title, checking to see if a title is provided
    while True:
        inputTitle = input("What is the book's title? ").strip()
        if inputTitle:
            book.title = inputTitle
            break
        else:
            print("Title cannot be empty. Please enter a valid title.")
    #Getting Author, checking to see if an author is provided
    while True:
        inputAuthor = input("Who is the book's author? ").strip()
        if inputAuthor:
            book.author = inputAuthor
            break
        else:
            print("Author cannot be empty. Please enter a valid author.")
    #Getting Read status, MUST BE READ OR UNREAD
    while True:
        inputRead = input("Has this book been read by the group? (Read or Unread)").lower().strip()
        if inputRead in ['Read', 'read', 'Unread', 'unread']:
            book.read = inputRead.title()
            break
        else:
            print("Please enter 'Read' or 'Unread'.")
    #Getting Rating, MUST BE INT BETWEEN 0 - 10
    while True:
        inputRating = input("What would you rate the book? (On a scale of 0 - 10) ").strip()
        if inputRating.isdigit() and 0 <= int(inputRating) <= 10:
            # inputRating = int(inputRating)
            book.rating = int(inputRating)
            break
        else:
            print("Rating must be a number between 0 and 10.")

    #Instantiating
    book = Book(inputTitle, inputAuthor, inputRead, inputRating)

    #Getting genre to know which list to append to
    while True:
        genre = input("Is this book fiction or nonfiction? ").lower().strip()
        if genre in ["Fiction", "fiction", "Nonfiction", "nonfiction"]:
            break
        else:
            print("Invalid genre. Please enter 'fiction' or 'nonfiction. ")
    #Appending new book to its respective list 
    if genre == "fiction":
        fiction_booklist.append(book)
        print(f"{inputTitle} by {inputAuthor} successfully added successfully")
    elif genre == "nonfiction":
        nonfiction_booklist.append(book)
        print(f"{inputTitle} by {inputAuthor} successfully added successfully")
    
def update_book(fiction_booklist, nonfiction_booklist) -> Book: #Allows users to update information about a book
    userInput = input("Which book would you like to update? ").strip()

    foundBook = False
    #checking to see if input is in fiction book list, then updating
    for book in fiction_booklist:
        if book.title.lower() == userInput.lower(): #Case insensitive validation
            print(f"Found {book.title}. Please enter updated information:\n")
            foundBook = True
            updated = False #Flag to track if any update is made, used to break out of loop

            #Updating book information
            while not updated:
                print(f"Current title: {book.title}")
                newTitle = input("Enter new title or press Enter to keep: ").strip()
                if newTitle:
                    book.title = newTitle
                    print("Title updated")
                    updated = True
                elif newTitle == "": #Checking for enter to keep previous info
                    updated = True
                print(f"Current author: {book.author}")
                newAuthor = input("Enter new author or press Enter to keep: ").strip()
                if newAuthor:
                    book.author = newAuthor
                    print("Author updated.")
                    updated = True
                elif newAuthor == "":
                    updated = True
                newStatus = input("Enter a new read status (Read or Unread) or press Enter to keep: ").strip()
                if newStatus in ['Read', 'read', 'Unread', 'unread']:
                    book.read = newStatus.title()
                    print("Read status updated.")
                    updated = True
                elif newStatus == "":
                    updated = True
                else:
                    print("Invalid input. Read Status not updated.")
                print(f"Current rating: {book.rating}")
                newRating = input("Enter a new rating (0-10), or press Enter to keep: ").strip()
                if newRating.isdigit() and 0 <= int(newRating) <= 10:
                    book.rating = int(newRating)
                    print("Rating updated.")
                    updated = True
                elif newRating == "":
                    updated = True
                else: 
                    print("Rating must be a neumber between 0 and 10.")
             
            if not foundBook:
                print("Book not found.")
            # break

    #checking to see if input is in fiction book list, then updating
    for book in nonfiction_booklist:
        if book.title.lower() == userInput.lower(): #Case insensitive validation
            print(f"Found {book.title}. Please enter updated information:\n")
            foundBook = True
            updated = False

            while not updated:
                print(f"Current title: {book.title}")
                newTitle = input("Enter new title or press Enter to keep: ").strip()
                if newTitle:
                    book.title = newTitle
                    print("Title updated")
                    updated = True
                elif newTitle == "":
                    updated = True
                print(f"Current author: {book.author}")
                newAuthor = input("Enter new author or press Enter to keep: ").strip()
                if newAuthor:
                    book.author = newAuthor
                    print("Author updated.")
                    updated = True
                elif newAuthor == "":
                    updated = True
                newStatus = input("Enter a new read status (Read or Unread) or press Enter to keep: ").strip()
                if newStatus in ['Read', 'read', 'Unread', 'unread']:
                    book.read = newStatus.title()
                    print("Read status updated.")
                    updated = True
                elif newStatus == "":
                    updated = True
                else:
                    print("Invalid input. Read Status not updated.")
                print(f"Current rating: {book.rating}")
                newRating = input("Enter a new rating (0-10), or press Enter to keep: ").strip()
                if newRating.isdigit() and 0 <= int(newRating) <= 10:
                    book.rating = int(newRating)
                    print("Rating updated.")
                    updated = True
                elif newRating == "":
                    updated = True
                else: 
                    print("Rating must be a neumber between 1 and 10.")
            if not foundBook:
                print("Book not found.")

def remove_book(fiction_booklist, nonfiction_booklist) -> None: #Allows users to remove books from book lists
    userInput = input("Which book would you like to remove? ").strip()

    #checking to see if input is in fiction book list, then removing
    for book in fiction_booklist:
        if book.title.lower() == userInput.lower(): #Case insensitive validation
            fiction_booklist.remove(book)
            print(f"{book.title} has been successfully removed.")
            return
    #checking to see if input is in nonfiction book list , then removing
    for book in nonfiction_booklist:
        if book.title.lower() == userInput.lower(): #Case insensitive validation
            nonfiction_booklist.remove(book)
            print(f"{book.title} has been successfully removed.")
            return

    if userInput not in fiction_booklist and userInput not in nonfiction_booklist:
            print(f"Book with title '{userInput}' not found.")
