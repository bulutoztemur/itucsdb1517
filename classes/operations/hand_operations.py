import psycopg2 as dbapi2
from classes.hand import Hand
from classes.model_config import dsn, connection
class hand_operations:
    def __init__(self):
        self.last_key=None

    def get_hands(self):
        global connection
        hands=[]
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT objectid, name FROM hand WHERE deleted=0 ORDER BY objectid"""
            cursor.execute(statement)
            hands = [(key, Hand(key,name,0)) for key, name in cursor]
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
        return hands

    def add_hand(self,Hand):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO hand (name) VALUES (%s)""",(Hand.name,))
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

    def get_hand(self, key):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT objectid, name FROM hand where (objectid=%s and deleted=0)"""
            cursor.execute(statement, (key,))
            id,name=cursor.fetchone()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
        return Hand(id, name, 0)

    def update_hand(self, key, name):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """update hand set (name) = (%s) where (objectid=(%s))"""
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

    def delete_hand(self,key):
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
#             statement = """update hand set deleted = 1 where (objectid=(%s))"""
            statement = """delete from hand where (objectid=(%s))"""
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