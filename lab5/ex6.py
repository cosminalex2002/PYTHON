class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checked_out = False

    def print_info(self):
        return f"Title: {self.title}\nAuthor/Director: {self.author}\nItem ID: {self.item_id}\nChecked Out: {'Yes' if self.checked_out else 'No'}"

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} is not checked out."


class Book(LibraryItem):
    def __init__(self, title, author, item_id, num_pages):
        super().__init__(title, author, item_id)
        self.num_pages = num_pages

    def print_info(self):
        return super().print_info() + f"\nNumber of Pages: {self.num_pages}"


class DVD(LibraryItem):
    def __init__(self, title, author, item_id, duration):
        super().__init__(title, author, item_id)
        self.duration = duration

    def print_info(self):
        return super().print_info() + f"\nDuration: {self.duration} minutes"

class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, publication_date):
        super().__init__(title, author, item_id)
        self.publication_date = publication_date

    def print_info(self):
        return super().print_info() + f"\nPublication Date: {self.publication_date}"

magazine = Magazine(title="Gazeta Sporturilor", author="Tolontan", item_id="3", publication_date="Sept 2023")
print(magazine.print_info())
print(magazine.check_out())
print(magazine.return_item())

