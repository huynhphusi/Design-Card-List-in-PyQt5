import sqlite3
from prettytable import PrettyTable

dataName = "data.db"

def createTableBook():
    global dataName
    dataConnect = sqlite3.connect(dataName)

    query = """
        CREATE TABLE IF NOT EXISTS Book (
            BookId Integer Primary Key Autoincrement,
            BookName Text NOT NULL,
            BookAuthor Text NOT NULL,
            BookPrice Integer NOT NULL,
            createAt DateTime DEFAULT current_timestamp
        )
    """

    cursor = dataConnect.cursor()
    cursor.execute(query)

    dataConnect.close()

def insertBook(BookName, BookAuthor, BookPrice):
    global dataName
    dataConnect = sqlite3.connect(dataName)

    query = """
        INSERT INTO Book (BookName, BookAuthor, BookPrice) VALUES (?, ?, ?)
    """

    cursor = dataConnect.cursor()
    cursor.execute(query, (BookName, BookAuthor, BookPrice))

    dataConnect.commit()
    dataConnect.close()

def updateBook(BookId, BookName, BookAuthor, BookPrice):
    global dataName
    dataConnect = sqlite3.connect(dataName)

    query = """
        UPDATE Book SET 
            BookName = ?, 
            BookAuthor = ?, 
            BookPrice = ?
        WHERE BookId = ?
    """

    cursor = dataConnect.cursor()
    cursor.execute(query, (BookName, BookAuthor, BookPrice, BookId)) # Theo thứ tự của 4 dấu ?

    dataConnect.commit()
    dataConnect.close()

def deleteBook(BookId):
    global dataName
    dataConnect = sqlite3.connect(dataName)

    query = """
        DELETE FROM Book WHERE BookId = ?
    """

    cursor = dataConnect.cursor()
    cursor.execute(query, (BookId,)) # Có dấu ,

    dataConnect.commit()
    dataConnect.close()

def getBookAll():
    global dataName
    dataConnect = sqlite3.connect(dataName)

    query = """
        SELECT BookId, BookName, BookAuthor, BookPrice FROM Book
    """

    cursor = dataConnect.cursor()
    bookList = cursor.execute(query).fetchall()

    return bookList

def getBookName(bookName):
    global dataName
    dataConnect = sqlite3.connect(dataName)

    query = """
        SELECT BookId, BookName, BookAuthor, BookPrice FROM Book WHERE BookName LIKE ?
    """

    cursor = dataConnect.cursor()
    bookList = cursor.execute(query, ('%'+bookName+'%',)).fetchall()

    return bookList

def printBookList(bookList):
    table = PrettyTable(['BookId', 'BookName', 'BookAuthor', 'BookPrice'])

    for book in bookList:
        table.add_row(book, divider=False)

    table.align = "l"
    print(table)