import psycopg2 as dbapi2
from classes.gender import Gender
from classes.model_config import dsn, connection
class gender_operations:
    def __init__(self):
        self.last_key=None

    def get_genders(self):
        global connection
        genders=[]
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT objectid, type FROM gender WHERE deleted=0 order by objectid"""
            cursor.execute(statement)
            genders = [(key, Gender(key,type,0)) for key, type in cursor]
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
        return genders

    def add_gender(self,Gender):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO gender (type) VALUES (%s)""",(Gender.type,))
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

    def get_gender(self, key):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT objectid, type FROM gender where (objectid=%s and deleted=0)"""
            cursor.execute(statement, (key,))
            id,type=cursor.fetchone()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
        return Gender(id, type, 0)

    def update_gender(self, key, type):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """update gender set (type) = (%s) where (objectid=(%s))"""
            cursor.execute(statement, (type, key,))
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
    def delete_gender(self,key):
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            #statement = """update gender set deleted = 1 where (objectid=(%s))"""
            statement = """DELETE FROM gender WHERE (objectid=(%s))"""
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