import MySQLdb


class Connection:
    def __init__(self, user, password, db, host='localhost', charset='utf8'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None
        self.charset = charset

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db,
                charset=self.charset
            )

    def disconnect(self):
        if self._connection:
            self._connection.close()


class GoodsSubjects:
    def __init__(self, db_connection, good_id, good_name, good_count, good_cost, good_char):
        self.db_connection = db_connection.connection
        self.good_id = good_id
        self.good_name = good_name
        self.good_count = good_count
        self.good_cost = good_cost
        self.good_char = good_char

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO myapp_goods values(%s,%s,%s,%s,%s)", (self.good_id,self.good_name, self.good_count, self.good_cost, self.good_char))
        self.db_connection.commit()
        c.close()


con = Connection(user='als', password=' ', db='test5_db')

with con:
    tutsub = GoodsSubjects(con, 23, "SQLlCon", "1", "1", "ewewew")


