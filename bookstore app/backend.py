import sqlite3


class DataBase:

    def __init__(self, db):
        """ a function that creates the database if he doesn't exist yet and the bookstore table
        """
        self._conn = sqlite3.connect(db)
        self._cur = self._conn.cursor()
        self._cur.execute(
            "CREATE TABLE IF NOT EXISTS bookstore(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER,"
            " isbn INTEGER)")
        self._conn.commit()

    def view(self):
        """ a function that returns the contents of the table
        :return: rows of data
        :rtype: str
        """
        self._cur.execute("SELECT * FROM bookstore")
        text_to_view = self._cur.fetchall()
        return text_to_view

    def search(self, title='', author='', year='', isbn=''):
        """ a function that returns the specific data the user searched
        :param title: the title data
        :param author: author data
        :param year: year data
        :param isbn: isbn data
        :type title: str
        :type author: str
        :type year: int
        :type isbn: int
        :return: the data the user searched
        :rtype: str
        """
        self._cur.execute("SELECT * FROM bookstore WHERE title=? OR author=? OR year=? OR isbn=?",
                          (title, author, year, isbn))
        text_to_view = self._cur.fetchall()
        return text_to_view

    def insert(self, id, title='', author='', year='', isbn=''):
        """ a function that adds new data to the database
        :param id: the id number of the item
        :param title: the title data
        :param author: author data
        :param year: year data
        :param isbn: isbn data
        :type id: int
        :type title: str
        :type author: str
        :type year: int
        :type isbn: int
        """
        self._cur.execute("INSERT INTO bookstore VALUES(?,?,?,?,?)", (id, title, author, year, isbn))
        self._conn.commit()


    def update(self, title, author, year, isbn, id):
        """ a function that updates specific data
        :param title: the title data
        :param author: author data
        :param year: year data
        :param isbn: isbn data
        :param id: the id number of the item to update
        :type title: str
        :type author: str
        :type year: int
        :type isbn: int
        :type id: int
        """
        self._cur.execute("UPDATE bookstore SET title=?, author=?, year=?, isbn=? WHERE id=?",
                          (title, author, year, isbn, id))
        self._conn.commit()

    def delete(self, id):
        """ a function that deletes a specific row of data
        :param id: the id of the row
        :type id: int
        """
        self._cur.execute("DELETE FROM bookstore WHERE id=?", (id,))
        self._conn.commit()

    def __del__(self):
        self._conn.close()
