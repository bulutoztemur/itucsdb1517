import psycopg2 as dbapi2
from classes.match import Match
from classes.team import Team
from classes.operations.team_operations import team_operations
from classes.court import Court
from classes.operations.court_operations import court_operations

from classes.model_config import dsn, connection
class match_operations:
    def __init__(self):
        self.last_key=None

    def get_matches(self):
        matches=[]
        global connection
        storeCourt = court_operations()
        storeTeam = team_operations()
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT objectid, hometeamid, awayteamid, courtid, matchdate FROM match WHERE deleted = 0"""
            cursor.execute(statement)
            matches = [(key, Match(key, hometeamid, storeTeam.get_team(hometeamid), awayteamid, storeTeam.get_team(awayteamid), courtid, storeCourt.get_court(courtid), matchdate, 0)) for key, hometeamid, awayteamid, courtid, matchdate in cursor]
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
        return matches

    def add_match(self,Match):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO match (hometeamid, awayteamid, courtid, matchdate) VALUES (%s, %s, %s, %s)""",(Match.hometeamid, Match.awayteamid, Match.courtid, Match.matchdate))
            cursor.close()
            connection.commit()
        except dbapi2.DatabaseError:
            if connection:
                connection.close()
        finally:
            if connection:
                connection.close()
    def get_match(self, key):
        global connection
        storeCourt = court_operations()
        storeTeam = team_operations()
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT objectid, hometeamid, awayteamid, courtid, matchdate FROM match WHERE (objectid=%s and deleted=0)"""
            cursor.execute(statement, (key,))
            id,hometeamid,awayteamid,courtid,matchdate=cursor.fetchone()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()

        return Match(id, hometeamid, storeTeam.get_team(hometeamid), awayteamid, storeTeam.get_team(awayteamid), courtid, storeCourt.get_court(courtid), matchdate, 0)

    def update_match(self, key, hometeamid, awayteamid, courtid, matchdate):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """update match set (hometeamid, awayteamid, courtid, matchdate) = (%s,%s,%s,%s) where (objectid=(%s))"""
            cursor.execute(statement, (hometeamid, awayteamid, courtid, matchdate, key,))
            connection.commit()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
        connection = dbapi2.connect(dsn)
        cursor = connection.cursor()
        statement = """update match set (hometeamid, awayteamid, courtid, matchdate) = (%s,%s,%s,%s) where (objectid=(%s))"""
        cursor.execute(statement, (hometeamid, awayteamid, courtid, matchdate, key,))
        connection.commit()
        cursor.close()
        connection.close()

    def delete_match(self,key):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """update match set deleted = 1 where (objectid=(%s))"""
            cursor.execute(statement, (key,))
            connection.commit()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()