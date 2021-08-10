import sqlite3

class Sort_DB:

    def __init__(self, name):
        self.con = sqlite3.connect(name, check_same_thread=False)
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