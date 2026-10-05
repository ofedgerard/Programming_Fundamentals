"""
Author: Gerard Ortiz
Date: 10 /4/2026
Tier Level: Base

Description:
This program uses the book class to create a list of books, displays the list using __str__ method,
uses while loops to process check outs and returns, displays the sorted view of the list, 
and displasys a filtered view of the list
"""


from book import Book

# uses the check_out method and output from collect_return_info() to 
# print message that a book is or already checked out to a patron
def check_out_book (check_out, collection, index, borrower):
        if check_out is True:
            print("'",collection[index].title,"'", " is checked out to ", borrower)
        elif check_out is False:
            print("'",collection[index].title,"'", " is already checked out")
        return

# takes in the book collection and returns the index and borrorwer name
def collect_checkout_info (collection):
    borrower = input("\nEnter borrower name: ")
    isbn = input("Enter book isbn: ")
    #index = collection.index(isbn)
    for index in range(len(collection)):
        if collection[index].isbn == isbn:
            return index, borrower
        
# takes in the book collection and returns the index by using the input for isbn
def collect_return_info (collection):
    isbn = input("\nEnter book isbn: ")
    for index in range(len(collection)):
            if collection[index].isbn == isbn:
                return index

# sorts the collection in alphabetical order using sorted(). 
# uses the __str__ method of the book class
def Sort_by_title(collection):
    sorted_collection = sorted(collection, key=lambda b:b.title)
    for book in sorted_collection:
        print(book) 
    return

# displays only books in the collection where available = true. 
# uses __str__ method of the book class
def get_available(collection):
    for book in collection:
         if book.available:
              print(book) 
    return

# main function where the other functions are called
def main():
    # the starter data with 6 books
    collection = [Book("The Lightning Thief", "Rick Riordan", "9780786856299", 2005, "Adventure"),
            Book("The Sea of Monsters", "Rick Riordan", "9780786856862", 2006, "Adventure"),
            Book("The Titan's Curse", "Rick Riordan", "9781423101451", 2007, "Adventure"),
            Book("The Battle of the Labyrinth", "Rick Riordan", "9781423101468", 2008, "Adventure"),
            Book("The Last Olympian", "Rick Riordan", "9781423101475", 2009, "Adventure"),
            Book("The Chalice of the Gods", "Rick Riordan", "9781368098175", 2023, "Adventure"),
            Book("Wrath of the Triple Goddess", "Rick Riordan", "9781368107631", 2024, "Adventure")]

    # uses __str__ method to print the collection
    print("=== Full Collection ===")
    for book in collection:
        print(book)

    # uses collect_checkout_info(collection), check_out(borrower), 
    # and check_out_book(status, collection, index, borrower)
    print("=== Checkout Books ===")
    continue_collect = "Yes"
    while continue_collect == "Yes":
        index, borrower = collect_checkout_info(collection)
        status = collection[index].check_out(borrower)
        check_out_book(status, collection, index, borrower)
        continue_collect = input("Check out another book? (Yes/No): ").strip().title()

    # uses the return_book method to process output from index = collect_return_info(collection)

    print("\n","=== Return Books ===")
    continue_return = input("Return books? (Yes/No):  ").strip().title()
    while continue_return == "Yes":
        index = collect_return_info(collection)
        return_message = collection[index].return_book()
        print(return_message)
        continue_return = input("Check out another book? (Yes/No): ").strip().title()

    print("\n","=== Books By Title ===")
    Sort_by_title(collection)

    print("\n","=== Available Books ===")
    get_available(collection)

if __name__ == '__main__':
    main()
