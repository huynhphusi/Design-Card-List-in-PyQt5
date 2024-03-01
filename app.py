from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import dataController as dc

from customWidget import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Book Manager")
        self.setFixedSize(600, 800)

        self.setStyleSheet("""
            QPushButton {
                font-size: 11pt;
                color: #fff;
                background-color: blue;
                border-radius: 5px;
                padding: 10px 0;
            }
            QPushButton:hover {
                background-color: green;
            }
            QLineEdit {
                padding: 5px;
                font-size: 11pt;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QLineEdit:focus {
                border: 1px solid #000;
            }
                           
            QLabel {
                font-size: 11pt;
            }
        """)

        self.mainFrame = QFrame()
        self.mainLayout = QVBoxLayout(self.mainFrame)

        self.bookName = QLineEdit()
        self.bookName.setPlaceholderText("Book name")
        self.bookAuthor = QLineEdit()
        self.bookAuthor.setPlaceholderText("Book author")
        self.bookPrice = QLineEdit()
        self.bookPrice.setPlaceholderText("$")
        
        self.buttonAdd = QPushButton(text="Add book")
        self.buttonAdd.setCursor(Qt.PointingHandCursor)
        self.buttonAdd.clicked.connect(self.addBook)

        self.mainLayout.addWidget(QLabel("Book name:"))
        self.mainLayout.addWidget(self.bookName)
        self.mainLayout.addWidget(QLabel("Book author:"))
        self.mainLayout.addWidget(self.bookAuthor)
        self.mainLayout.addWidget(QLabel("Book price:"))
        self.mainLayout.addWidget(self.bookPrice)
        self.mainLayout.addWidget(self.buttonAdd)
        
        scrollFrame = QFrame()
        self.scrollLayout = QVBoxLayout(scrollFrame)

        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollArea.setWidget(scrollFrame)
        scrollArea.setStyleSheet("QScrollArea{border: 0pt}")

        self.scrollLayout.addStretch()
        self.mainLayout.addWidget(scrollArea)

        self.setCentralWidget(self.mainFrame)

        self.loadBookList()

    def addBook(self):
        book_name = self.bookName.text()
        book_author = self.bookAuthor.text()
        book_price = self.bookPrice.text()

        if book_name and book_author and book_price:
            self.mainWindow.addBook(book_name, book_author, book_price)
            self.mainWindow.loadBookList()
            self.bookName.clear()
            self.bookAuthor.clear()
            self.bookPrice.clear()

    def loadBookList(self):
        # clear exist book cards before reload
        for i in reversed(range(self.scrollLayout.count())):
            widget = self.scrollLayout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        
        bookList = dc.getBookAll()

        for book in bookList:
            frame = BookCard(*book, self)
            self.scrollLayout.insertWidget(0, frame)

    def addBook(self, bookName, bookAuthor, bookPrice):
        dc.insertBook(bookName, bookAuthor, bookPrice)

    def updateBook(self, BookId, BookName, BookAuthor, BookPrice):
        dc.updateBook(BookId, BookName, BookAuthor, BookPrice)
        self.loadBookList()

if __name__ == "__main__":
    app = QApplication([])
    
    window = MainWindow()
    window.show()

    app.exec_()
