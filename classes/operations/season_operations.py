import psycopg2 as dbapi2
from classes.season import Season
from classes.model_config import dsn, connection
class season_operations:
    def __init__(self):
        self.last_key=None

    def get_seasons(self):
        global connection
        seasons=[]
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT objectid, name FROM season WHERE deleted=0"""
            cursor.execute(statement)
            seasons = [(key, Season(key,name,0)) for key, name in cursor]
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
        return seasons

    def add_season(self,Season):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO season (name) VALUES (%s)""",(Season.name,))
            cursor.close()
            connection.commit()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()

    def get_season(self, key):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT objectid, name FROM season where (objectid=%s and deleted=0)"""
            cursor.execute(statement, (key,))
            id,name=cursor.fetchone()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
        return Season(id, name, 0)

    def update_season(self, key, name):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """update season set (name) = (%s) where (objectid=(%s))"""
            cursor.execute(statement, (name, key,))
            connection.commit()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()

    def delete_season(self,key):
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """update season set deleted = 1 where (objectid=(%s))"""
            cursor.execute(statement, (key,))
            connection.commit()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()