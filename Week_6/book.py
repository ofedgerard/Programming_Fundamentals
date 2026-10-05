class Book:
    def __init__(self, title, author, isbn, year, genre):
        self.title = title
        self.author = author 
        self.isbn = isbn
        self.year = year
        self.genre = genre
        self.available = True
        self.borrower = None

    def get_status(self):
        if self.available:
            return "Available"
        else:
            return "Unavailable"
    
    def __str__(self):
        return f'{self.isbn:<15}{self.title} by {self.author:<5}:   \n{self.year:>10}  {self.genre:<15} {self.get_status()}\n'
        #return f'{self.isbn:<16} {self.title:<35} \n{"":>6}by {self.author:<5}   {self.year:<5} {self.genre:<10} {self.available}'
        #return f'{self.__class__.__name__} isbn={self.isbn} (title={self.title}) author={self.author}  year={self.year} genre={self.genre}'

    def check_out(self, patron_name):
        if self.available == True:
            self.available = False
            self.borrower = patron_name
            return True
        elif self.available == False:
            return False
        
    def return_book(self):
        if not self.available:
            self.available = True
            self.borrower = None
            return f"'{self.title}' has been returned and is now available"
        else:
            return f"'{self.title}' is already available"
        

"""
print(f"{title:<30}{year:<10}{genres:<20}  {rating:<10}")
"""