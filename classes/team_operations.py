import psycopg2 as dbapi2
from classes.team import Team
from classes.model_config import dsn, connection
class team_operations:
    def __init__(self):
        self.last_key=None

    def get_teams(self):
        teams=[]
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT objectid, name, shirtcolour, foundationdate, countryid, courtid FROM team where deleted=B'0'"""
            cursor.execute(statement)
            teams = [(key, Team(name,color,date,country,court,0)) for key, name, color, date, country, court in cursor]
            cursor.close()
        except dbapi2.DatabaseError:
            connection.rollback()
        finally:
            connection.close()
        return teams

    def add_team(self,Team):
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO team (name, shirtcolour, foundationdate, countryid, courtid, deleted) VALUES (%s, %s, %s, %s, %s, B'%s')""",(Team.name,Team.color,Team.date,Team.country,Team.court,Team.deleted))
            cursor.close()
            connection.commit()
        except dbapi2.DatabaseError:
            connection.rollback()
        finally:
            connection.close()

    def get_team(self, key):
        team=None
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            cursor.execute("""SELECT objectid, name, shirtcolour, foundationdate, countryid, courtid FROM team where objectid=%s %s and deleted=B'0'""", (key,' '))
            id, name, color, date, country, court = cursor
            teams = [(id, Team(name,color,date,country,court,0)) for id, name, color, date, country, court in cursor]
            team = teams[key]
            cursor.close()
        except dbapi2.DatabaseError:
            connection.rollback()
        finally:
            connection.close()
        return team