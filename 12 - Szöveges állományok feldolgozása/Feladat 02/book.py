from datetime import datetime

class Book:
    def __init__(self) -> None:
        super().__init__()

        self.writerFirstName: str = None
        self.writerLastName: str = None
        self.writerBirthDate: datetime = None
        self.bookTitle: str = None
        self.isbn: str = None
        self.publsher: str = None
        self.publishYear: int = 0
        self.bookPrice: float = 0
        self.theme: str = None
        self.pageNumbers: int = 0
        self.writerMononarium: float = 0

    def __str__(self) -> str:
        return f"{self.writerFirstName} {self.writerLastName} - {self.bookTitle} [{self.publishYear}]" 