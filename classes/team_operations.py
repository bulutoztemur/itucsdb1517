import psycopg2 as dbapi2
from classes.team import Team
class team_operations:
    def get_teams():
        dsn = """user=vagrant password=vagrant host=127.0.0.1 port=54321 dbname=itucsdb"""
        connection = dbapi2.connect(dsn)
        cursor = connection.cursor()
        statement = """SELECT objectid, name, shirtColour FROM team"""
        cursor.execute(statement)
        teams=[]
        for row in cursor:
            objectid, name, color = row
            teams.append((objectid, Team(name,color)))
        cursor.close()
        connection.close()
        return teams