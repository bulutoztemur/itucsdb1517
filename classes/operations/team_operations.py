import psycopg2 as dbapi2
from classes.team import Team
from classes.model_config import dsn, connection
class team_operations:
    def __init__(self):
        self.last_key=None

    def get_teams(self):
        teams=[]
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT objectid, name, shirtcolour, foundationdate, countryid, courtid FROM team where deleted=0"""
            cursor.execute(statement)
            teams = [(key, Team(name,color,date,country,court,0)) for key, name, color, date, country, court in cursor]
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.close()
        finally:
            if connection:
                connection.close()
        return teams

    def add_team(self,Team):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO team (name, shirtcolour, foundationdate, countryid, courtid) VALUES (%s, %s, %s, %s, %s)""",(Team.name,Team.color,Team.date,Team.country,Team.court))
            cursor.close()
            connection.commit()
        except dbapi2.DatabaseError:
            if connection:
                connection.close()
        finally:
            if connection:
                connection.close()

    def get_team(self, key):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT objectid, name, shirtcolour, foundationdate, countryid, courtid FROM team where (objectid=%s and deleted=0)"""
            cursor.execute(statement, (key,))
            id,name,color,date,country,court=cursor.fetchone()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
        return Team(name, color, date, country, court, 0)

    def update_team(self, key, name, color, date, country, court):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """update team set (name, shirtcolour, foundationdate, countryid, courtid) = (%s,%s,%s,%s,%s) where (objectid=(%s))"""
            cursor.execute(statement, (name, color, date, country, court, key,))
            connection.commit()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()

    def delete_team(self,key):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """update team set deleted = 1 where (objectid=(%s))"""
            cursor.execute(statement, (key,))
            connection.commit()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()