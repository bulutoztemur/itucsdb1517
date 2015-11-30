import psycopg2 as dbapi2
from classes.court import Court
from classes.model_config import dsn, connection
class court_operations:
    def __init__(self):
        self.last_key=None

    def get_courts(self):
        global connection
        courts=[]
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT objectid, name, address, capacity FROM court WHERE deleted=0 ORDER BY objectid"""
            cursor.execute(statement)
            courts = [(key, Court(key,name,address,capacity,0)) for key, name, address, capacity in cursor]
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
        return courts

    def add_court(self,Court):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO court (name, address, capacity) VALUES (%s, %s, %s)""",(Court.name,Court.address,Court.capacity))
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

    def get_court(self, key):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT objectid, name, address, capacity FROM court where (objectid=%s and deleted=0)"""
            cursor.execute(statement, (key,))
            id,name,address,capacity=cursor.fetchone()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
        return Court(id, name, address, capacity, 0)

    def update_court(self, key, name, address, capacity):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """update court set (name, address, capacity) = (%s,%s,%s) where (objectid=(%s))"""
            cursor.execute(statement, (name, address, capacity, key,))
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

    def delete_court(self,key):
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """delete from court where (objectid=(%s))"""
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