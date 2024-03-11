import sqlite3

def createTableBook():
    dataConnect = sqlite3.connect("data.db")

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
    dataConnect = sqlite3.connect("data.db")

    query = """
        INSERT INTO Book (BookName, BookAuthor, BookPrice) VALUES (?, ?, ?)
    """

    cursor = dataConnect.cursor()
    cursor.execute(query, (BookName, BookAuthor, BookPrice))

    dataConnect.commit()
    dataConnect.close()

def updateBook(BookId, BookName, BookAuthor, BookPrice):
    dataConnect = sqlite3.connect("data.db")

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
    dataConnect = sqlite3.connect("data.db")

    query = """
        DELETE FROM Book WHERE BookId = ?
    """

    cursor = dataConnect.cursor()
    cursor.execute(query, (BookId,)) # Có dấu ,

    dataConnect.commit()
    dataConnect.close()

def getBookAll():
    dataConnect = sqlite3.connect("data.db")

    query = """
        SELECT BookId, BookName, BookAuthor, BookPrice FROM Book
    """

    cursor = dataConnect.cursor()
    bookList = cursor.execute(query).fetchall()

    return bookList

def getBookName(bookName):
    dataConnect = sqlite3.connect("data.db")

    query = """
        SELECT BookId, BookName, BookAuthor, BookPrice FROM Book WHERE BookName LIKE ?
    """

    cursor = dataConnect.cursor()
    bookList = cursor.execute(query, ('%'+bookName+'%',)).fetchall()

    return bookList