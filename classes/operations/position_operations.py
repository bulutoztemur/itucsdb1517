import psycopg2 as dbapi2
from classes.position import Position
from classes.model_config import dsn, connection
class position_operations:
    def __init__(self):
        self.last_key=None

    def get_positions(self):
        positions=[]
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT objectid, name FROM position WHERE position.deleted = 0 ORDER BY objectid"""
            cursor.execute(statement)
            positions = [(key, Position(key,name,0)) for key, name in cursor]
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
        return positions

    def add_position(self,Position):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO position (name) VALUES (%s)""",(Position.name,))
            cursor.close()
            connection.commit()
            result = 'success'
        except dbapi2.IntegrityError:
            result = 'integrityerror'
            if connection:
                connection.rollback()
        except dbapi2.DatabaseError:
            result = 'databaseerror'
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
            return result

    def get_position(self, key):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT objectid, name FROM position where (objectid=%s and deleted=0)"""
            cursor.execute(statement, (key,))
            id,name=cursor.fetchone()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
        return Position(id, name, 0)

    def update_position(self, key, name):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """update position set (name) = (%s) where (objectid=(%s))"""
            cursor.execute(statement, (name, key,))
            connection.commit()
            cursor.close()
            result = 'success'
        except dbapi2.IntegrityError:
            result = 'integrityerror'
            if connection:
                connection.rollback()
        except dbapi2.DatabaseError:
            result = 'databaseerror'
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
            return result

    def delete_position(self,key):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
#             statement = """update position set deleted = 1 where (objectid=(%s))"""
            statement = """delete from position where (objectid=(%s))"""
            cursor.execute(statement, (key,))
            connection.commit()
            cursor.close()
            result = 'success'
        except dbapi2.IntegrityError:
            result = 'integrityerror'
            if connection:
                connection.rollback()
        except dbapi2.DatabaseError:
            result = 'databaseerror'
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
            return result