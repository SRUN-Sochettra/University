class LibraryUser:
    total_users = 0

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self._borrowed_books = []
        LibraryUser.total_users += 1

    def borrow_book(self, book_name):
        """Override in subclasses to enforce limits."""
        raise NotImplementedError

    def return_book(self, book_name):
        if book_name in self._borrowed_books:
            self._borrowed_books.remove(book_name)
            print(f"{self.name} returned '{book_name}'.")
        else:
            print(f"{self.name} did not borrow '{book_name}'.")

    def list_borrowed_books(self):
        print(f"{self.name} has borrowed: {self._borrowed_books}")

    @classmethod
    def get_total_users(cls):
        return cls.total_users

class StudentUser(LibraryUser):
    MAX_BOOKS = 3

    def borrow_book(self, book_name):
        if len(self._borrowed_books) < self.MAX_BOOKS:
            self._borrowed_books.append(book_name)
            print(f"{self.name} borrowed '{book_name}'.")
        else:
            print(f"{self.name} has reached the borrow limit of {self.MAX_BOOKS} books.")
            print(f"{self.name} did not borrow '{book_name}'.")

class TeacherUser(LibraryUser):
    MAX_BOOKS = 5

    def borrow_book(self, book_name):
        if len(self._borrowed_books) < self.MAX_BOOKS:
            self._borrowed_books.append(book_name)
            print(f"{self.name} borrowed '{book_name}'.")
        else:
            print(f"{self.name} has reached the borrow limit of {self.MAX_BOOKS} books.")
            print(f"{self.name} did not borrow '{book_name}'.")

student = StudentUser("Alice", "S001")
teacher = TeacherUser("Mr. Bob", "T001")

student.borrow_book("Python Basics")
student.borrow_book("Data Science 101")
student.borrow_book("Machine Learning")
student.borrow_book("Extra Book")
student.return_book("Data Science 10")
student.return_book("Data Science 101")
student.list_borrowed_books()

teacher.borrow_book("Advanced Python")
teacher.list_borrowed_books()

print("Total users: ", teacher.get_total_users())