import sqlite3

class DB_H:
    def __init__(self,db_name):
        self.conn = sqlite3.connect(db_name,check_same_thread = False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def names(self):
        return self.cursor.execute('select san,name from Info asc limit 25').fetchall()
    def get_names(self, user_id):
        return self.cursor.execute('select * from Info where san=?',(user_id, )).fetchone()
    def get_n(self, month,day):
        return self.cursor.execute('select * from Info where month=? and day=?',(month,day)).fetchone()
