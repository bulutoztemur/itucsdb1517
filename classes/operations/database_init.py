import psycopg2 as dbapi2
from classes.model_config import dsn, connection

class database_initialization:
    def __init__(self):
        self.last_key=None
    def init_db(self):

        global connection

        connection = dbapi2.connect(dsn)
        cursor = connection.cursor()
        cursor.execute(open("database/dump.sql", "r").read())
        cursor.close()
        connection.commit()

        connection.close()
