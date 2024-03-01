from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFrame, QHBoxLayout, QDialog
from PyQt5.QtCore import Qt

import dataController as dc

class BookCard(QFrame):
    def __init__(self, BookId, BookName, BookAuthor, BookPrice, mainWindow):
        super().__init__()

        self.BookId, self.BookName, self.BookAuthor, self.BookPrice = BookId, BookName, BookAuthor, BookPrice
        self.mainWindow = mainWindow

        # Tạo QFrame con để áp dụng border
        #self.borderFrame = QFrame()
        #self.borderFrame.setStyleSheet("border: 1px solid #ccc;")

        self.setStyleSheet("background: #FFFFFF; border: 1px solid #ccc; border-radius: 5px; color: #000000;")

        layout = QVBoxLayout()
        labelName = QLabel(f"<b>{BookName}</b>")
        labelName.setStyleSheet("border: 0px; padding: 10px 10px 0 10px;")
        labelAuthor = QLabel(f"<i>{BookAuthor}</i>")
        labelAuthor.setStyleSheet("border: 0px; padding: 10px 10px 0 10px;")
        labelPrice = QLabel(f"<i>{BookPrice}</i>")
        labelPrice.setStyleSheet("border: 0px; padding: 10px;")
        
        buttonLayout = QHBoxLayout()
        buttonDelete = QPushButton(text="Delete", clicked=self.deleteBook)
        buttonDelete.setStyleSheet("""
                                   QPushButton {
                                        background: #fff; color: #000; padding: 10px; border: 1px solid #ccc; border-radius: 0px; border-bottom-right-radius: 5px; border-bottom: 0px; border-right: 0px
                                   }
                                   QPushButton:hover {
                                        color: red;
                                   }
                                   """)
        buttonDelete.setCursor(Qt.PointingHandCursor)
        buttonEdit = QPushButton(text="Edit", clicked=self.editBook)
        buttonEdit.setStyleSheet("""
                                 QPushButton {
                                        background: #fff; color: #000; padding: 10px; border: 1px solid #ccc; border-radius: 0px; border-bottom-left-radius: 5px; border-bottom: 0px; border-left: 0px
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
        layout.addStretch()
        layout.addLayout(buttonLayout)
        layout.setContentsMargins(0,0,0,0)

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
        self.mainWindow = mainWindow
        self.BookId, self.BookName, self.BookAuthor, self.BookPrice = BookId, BookName, BookAuthor, BookPrice

        self.setWindowTitle("Update Book")
        self.setFixedSize(600, 250)

        self.mainLayout = QVBoxLayout()
        self.edtBookName = QLineEdit()
        self.edtBookName.setText(self.BookName)
        self.edtBookAuthor = QLineEdit()
        self.edtBookAuthor.setText(self.BookAuthor)
        self.edtBookPrice = QLineEdit()
        self.edtBookPrice.setText(str(self.BookPrice))

        self.buttonLayout = QHBoxLayout()
        self.buttonSubmit = QPushButton(text="Save", clicked=self.saveUpdate)
        self.buttonCancel = QPushButton(text="Cancel", clicked=self.accept)
        self.buttonSubmit.setCursor(Qt.PointingHandCursor)
        self.buttonCancel.setCursor(Qt.PointingHandCursor)
        self.buttonLayout.addWidget(self.buttonSubmit)
        self.buttonLayout.addWidget(self.buttonCancel)

        self.mainLayout.addWidget(self.edtBookName)
        self.mainLayout.addWidget(self.edtBookAuthor)
        self.mainLayout.addWidget(self.edtBookPrice)
        self.mainLayout.addLayout(self.buttonLayout)

        self.setLayout(self.mainLayout)

    def saveUpdate(self):
        bookName = self.edtBookName.text()
        bookAuthor = self.edtBookAuthor.text()
        bookPrice = self.edtBookPrice.text()

        self.mainWindow.updateBook(self.BookId, bookName, bookAuthor, bookPrice)
        self.accept() # close dialog