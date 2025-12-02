## Author: Vikash rawat
# Mini Project - Library Inventory Manager
import sys
import logging
from library_manager.inventory import LibraryInventory
from library_manager.book import Book

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.FileHandler("library.log"), logging.StreamHandler(sys.stdout)]
)

def input_nonempty(prompt):
    while True:
        s = input(prompt).strip()
        if s:
            return s

def menu():
    inv = LibraryInventory("catalog.json")
    while True:
        print("\n=== Library Inventory Manager ===")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All")
        print("5. Search Title")
        print("6. Search ISBN")
        print("7. Exit")

        c = input_nonempty("Choose: ")

        if c == "1":
            t = input_nonempty("Title: ")
            a = input_nonempty("Author: ")
            i = input_nonempty("ISBN: ")
            inv.add_book(Book(t, a, i))
            print("Added.")

        elif c == "2":
            i = input_nonempty("ISBN: ")
            b = inv.search_by_isbn(i)
            if b and b.issue():
                inv.save()
                print("Issued.")
            else:
                print("Cannot issue.")

        elif c == "3":
            i = input_nonempty("ISBN: ")
            b = inv.search_by_isbn(i)
            if b and b.return_book():
                inv.save()
                print("Returned.")
            else:
                print("Cannot return.")

        elif c == "4":
            for x in inv.display_all():
                print("-", x)

        elif c == "5":
            q = input_nonempty("Title: ")
            for x in inv.search_by_title(q):
                print("-", x)

        elif c == "6":
            i = input_nonempty("ISBN: ")
            b = inv.search_by_isbn(i)
            print(b if b else "Not found.")

        elif c == "7":
            break

if __name__ == "__main__":
    menu()