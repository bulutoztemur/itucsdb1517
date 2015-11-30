import psycopg2 as dbapi2
from classes.country import Country
from classes.model_config import dsn, connection
class country_operations:
    def __init__(self):
        self.last_key=None

    def get_countries(self):
        global connection
        countries=[]
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT objectid, name FROM country WHERE deleted=0 ORDER BY objectid"""
            cursor.execute(statement)
            countries = [(key, Country(key,name,0)) for key, name in cursor]
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
        return countries

    def add_country(self,Country):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO country (name) VALUES (%s)""",(Country.name,))
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

    def get_country(self, key):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT objectid, name FROM country where (objectid=%s and deleted=0)"""
            cursor.execute(statement, (key,))
            id,name=cursor.fetchone()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
        return Country(id, name, 0)

    def update_country(self, key, name):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """update country set (name) = (%s) where (objectid=(%s))"""
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

    def delete_country(self,key):
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
#             statement = """update country set deleted = 1 where (objectid=(%s))"""
            statement = """delete from country where (objectid=(%s))"""
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