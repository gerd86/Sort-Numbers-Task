
import sqlite3


class Sort_DB:

    def __init__(self, name):
        self.con = sqlite3.connect(name)
        self.cur = self.con.cursor()

    def create_tb(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS sorted_lists
        (id INTEGER PRIMARY KEY AUTOINCREMENT, sort_order TEXT, sorted_list TEXT, sort_time TEXT)''')
        self.con.commit()

    def add_record(self, sort_order, sorted_list, sort_time):
        self.cur.execute("INSERT INTO sorted_lists (sort_order, sorted_list, sort_time) VALUES (?, ?, ?)", (sort_order,
                                                                                                            sorted_list,
                                                                                                            sort_time,))
        self.con.commit()

    def fetch_records(self):
        self.cur.execute("SELECT * FROM sorted_lists")
        return self.cur.fetchall()


class Sort:
    def __init__(self, number_list):
        self.number_list = number_list

    def str_to_list(self):
        lst = self.number_list.split()
        return lst

    # Sort ascending

    def sort_number_ascending(self):
        return sorted(self.str_to_list(), key=lambda k: int(k))

    # Sort descending

    def sort_number_descending(self):
        return sorted(self.str_to_list(), key=lambda k: int(k), reverse=True)


