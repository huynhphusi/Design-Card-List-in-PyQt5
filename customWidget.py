from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

import dataController as dc

class BookCard(QFrame):
    def __init__(self, BookId, BookName, BookAuthor, BookPrice, mainWindow):
        super().__init__()

        self.BookId, self.BookName, self.BookAuthor, self.BookPrice = BookId, BookName, BookAuthor, BookPrice
        self.mainWindow = mainWindow

        self.setStyleSheet("""
            background: #fff;
            border: 1px solid #ccc;
            border-radius: 5px;
            color: #000;
        """)

        layout = QVBoxLayout()
        labelName = QLabel(f"<b>{BookName}</b>")
        labelName.setStyleSheet("""
            border: 0;
            color: red;
            border-bottom: 1px solid #ccc;
            border-radius: 0px;
            padding: 10px 0;
            margin: 0 10px;
        """)
        labelAuthor = QLabel(f"<b>{BookAuthor}</b>")
        labelAuthor.setStyleSheet("""
            border: 0;
            padding: 10px;
        """)
        labelPrice = QLabel(f"<b>{BookPrice}</b>")
        labelPrice.setStyleSheet("""
            border: 0;
            padding: 10px;
        """)

        buttonLayout = QHBoxLayout()
        buttonDelete = QPushButton(text="Delete", clicked=self.deleteBook)
        buttonDelete.setStyleSheet("""
            QPushButton {
                font-size: 11pt;
                color: #000;
                background-color: #fff;
                border-radius: 0px;
                padding: 10px;
                border: 1px solid #ccc;
                border-bottom-right-radius: 5px;
                border-right: 0px;
                border-bottom: 0px;
            }
            QPushButton:hover {
                color: red;
            }
        """)
        buttonDelete.setCursor(Qt.PointingHandCursor)
        buttonEdit = QPushButton(text="Edit", clicked=self.editBook)
        buttonEdit.setStyleSheet("""
            QPushButton {
                font-size: 11pt;
                color: #000;
                background-color: #fff;
                border-radius: 0px;
                padding: 10px;
                border: 1px solid #ccc;
                border-bottom-left-radius: 5px;
                border-left: 0px;
                border-bottom: 0px;
            }
            QPushButton:hover {
                color: red;
            }
        """)
        buttonEdit.setCursor(Qt.PointingHandCursor)

        buttonLayout.addWidget(buttonEdit, stretch=1)
        buttonLayout.addWidget(buttonDelete, stretch=1)
        buttonLayout.setSpacing(0)

        layout.addWidget(labelName)
        layout.addWidget(labelAuthor)
        layout.addWidget(labelPrice)
        layout.addLayout(buttonLayout)
        layout.setContentsMargins(0,0,0,0)

        self.setLayout(layout)

    def deleteBook(self):
        dc.deleteBook(self.BookId)
        self.mainWindow.loadBookList()

    def editBook(self):
        dialog = DialogUpdateBook(self.mainWindow, self.BookId, self.BookName, self.BookAuthor, self.BookPrice)
        dialog.exec_()

class DialogUpdateBook(QDialog):
    def __init__(self, mainWindow, BookId, BookName, BookAuthor, BookPrice):
        super().__init__(mainWindow)
        self.BookId, self.BookName, self.BookAuthor, self.BookPrice = BookId, BookName, BookAuthor, BookPrice
        self.mainWindow = mainWindow

        self.setWindowTitle("Update Book")
        self.setFixedSize(600, 250)

        self.mainLayout = QVBoxLayout()

        self.bookName = QLineEdit()
        self.bookName.setText(self.BookName)
        self.bookAuthor = QLineEdit()
        self.bookAuthor.setText(self.BookAuthor)
        self.bookPrice = QLineEdit()
        self.bookPrice.setText(str(self.BookPrice))

        self.buttonLayout = QHBoxLayout()
        self.buttonSave = QPushButton(text="Save", clicked=self.saveUpdate)
        self.buttonSave.setCursor(Qt.PointingHandCursor)
        self.buttonCancel = QPushButton(text="Cancel", clicked=self.accept)
        self.buttonCancel.setCursor(Qt.PointingHandCursor)

        self.buttonLayout.addWidget(self.buttonSave)
        self.buttonLayout.addWidget(self.buttonCancel)

        self.mainLayout.addWidget(self.bookName)
        self.mainLayout.addWidget(self.bookAuthor)
        self.mainLayout.addWidget(self.bookPrice)
        self.mainLayout.addLayout(self.buttonLayout)

        self.setLayout(self.mainLayout)

    def saveUpdate(self):
        bookName = self.bookName.text()
        bookAuthor = self.bookAuthor.text()
        bookPrice = self.bookPrice.text()

        dc.updateBook(self.BookId, bookName, bookAuthor, bookPrice)
        self.mainWindow.loadBookList()
        self.accept() #close dialog