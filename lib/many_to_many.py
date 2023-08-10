class Author:
    all = []

    def __init__(self, name) -> None:
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        related_contracts = self.contracts()
        return [contract.book for contract in related_contracts]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        related_contracts = self.contracts()
        return sum([contract.royalties for contract in related_contracts])


    

class Book:
    all = []
    def __init__(self, title) -> None:
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        related_contracts = self.contracts()
        return [contract.author for contract in related_contracts]


class Contract:
    all = []
    def __init__(self, author, book, date, royalties) -> None:
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author class")
        self.author = author
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of Book class")
        self.book = book
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        self.date = date
        if not isinstance(royalties, (int, float)):
            raise TypeError("Royalties must be a number")
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls):
        sorted_contracts = sorted(cls.all, key=lambda contract: contract.date)
        return sorted_contracts
