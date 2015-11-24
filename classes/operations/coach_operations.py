import psycopg2 as dbapi2
from classes.coach import Coach
from classes.team import Team
from classes.country import Country
from classes.model_config import dsn, connection
class coach_operations:
    def __init__(self):
        self.last_key=None

    def get_coachs(self):
        coachs=[]
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT coach.objectid, coach.name, coach.surname, coach.countryid, country.name, coach.teamid, team.name, coach.birthyear, coach.genderid FROM coach INNER JOIN court ON team.courtid = court.objectid INNER JOIN country ON team.countryid = country.objectid WHERE team.deleted = 0 AND court.deleted = 0 AND country.deleted = 0"""
            cursor.execute(statement)
            coachs = [(key, Coach(key,name,surname,countryid,Country(countryid, countryname, 0),teamid,Team(teamid,teamname, color), 0)) for key, name,surname, countryid, countryname, teamid, teamname, teamcolor in cursor]
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
        return coachs

    def add_coach(self,Coach):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO coach (name, surname, countryid, teamid) VALUES (%s, %s, %s, %s)""",(Coach.name,Coach.surname,Coach.countryid,Coach.teamid))
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
            statement = """SELECT objectid, name, surname,  countryid, teamid, birthyear, genderid FROM coach where (objectid=%s and deleted=0)"""
            cursor.execute(statement, (key,))
            id,name,surname,countryid,teamid,birthyear,genderid=cursor.fetchone()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
        return Coach(None,name,surname,countryid,teamid,birthyear,genderid,0)

    def update_coach(self, key, name, surname, countryid, teamid, birthyear, genderid):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """update coach set (name, surname, countryid, teamid, birthyear, genderid) = (%s,%s,%s,%s,%s, %s) where (objectid=(%s))"""
            cursor.execute(statement, (name, surname, countryid, teamid, birthyear, genderid, key,))
            connection.commit()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()

    def delete_coach(self,key):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """update coach set deleted = 1 where (objectid=(%s))"""
            cursor.execute(statement, (key,))
            connection.commit()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()