class LibraryBook:

    def __init__(self, bookId, bookName, author, price, issuedStatus=False):
        self.bookId = bookId
        self.bookName = bookName
        self.author = author
        self.price = price
        self.issuedStatus = issuedStatus

    def display_books(self):
        print(f"\nBook ID      : {self.bookId}")
        print(f"Book Name    : {self.bookName}")
        print(f"Author       : {self.author}")
        print(f"Price        : ₹{self.price}")

        if self.issuedStatus:
            print("Status       : Issued")
        else:
            print("Status       : Available")

    def issue_book(self):
        if not self.issuedStatus:
            self.issuedStatus = True
            print("\nBook Issued Successfully.")
        else:
            print("\nBook is already issued.")

    def return_book(self):
        if self.issuedStatus:
            self.issuedStatus = False
            print("\nBook Returned Successfully.")
        else:
            print("\nBook is already available.")

    def update_price(self, new_price):
        print(f"\nOld Price : ₹{self.price}")
        self.price = new_price
        print(f"New Price : ₹{self.price}")

    def discount(self, percent):
        print(f"\nOriginal Price : ₹{self.price}")
        self.price = self.price - (self.price * percent / 100)
        print(f"Price after {percent}% discount : ₹{self.price}")

    def __del__(self):
        print(f"\nBook '{self.bookName}' Object Deleted.")


# ---------------- Main Program ----------------

lb = LibraryBook(101, "Python Programming", "John", 599)

lb.display_books()

lb.issue_book()

lb.issue_book()

lb.return_book()

lb.return_book()

lb.update_price(700)

lb.discount(10)

lb.display_books()

del lb