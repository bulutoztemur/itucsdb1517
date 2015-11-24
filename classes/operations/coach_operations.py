import psycopg2 as dbapi2
from classes.coach import Coach
from classes.team import Team
from classes.operations.team_operations import team_operations
from classes.country import Country
from classes.operations.country_operations import country_operations
from classes.gender import Gender
from classes.operations.gender_operations import gender_operations
from classes.model_config import dsn, connection
class coach_operations:
    def __init__(self):
        self.last_key=None

    def get_coaches(self):
        coachs=[]
        global connection
        storeCountry = country_operations()
        storeTeam = team_operations()
        storeGender = gender_operations()
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT coach.objectid, coach.name, coach.surname, coach.countryid, coach.teamid, coach.birthday, coach.genderid FROM coach WHERE coach.deleted = 0"""
            cursor.execute(statement)
            coachs = [(key, Coach(key,name,surname,countryid, storeCountry.get_country(countryid), teamid, storeTeam.get_team(teamid), birthyear, genderid, storeGender.get_gender(genderid), 0)) for key, name,surname, countryid, teamid, birthyear, genderid in cursor]
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
            cursor.execute("""INSERT INTO coach (name, surname, countryid, teamid, birthday, genderid) VALUES (%s, %s, %s, %s, %s, %s)""",(Coach.name,Coach.surname,Coach.countryid,Coach.teamid, Coach.birthyear, Coach.genderid))
            cursor.close()
            connection.commit()
        except dbapi2.DatabaseError:
            if connection:
                connection.close()
        finally:
            if connection:
                connection.close()
    def get_coach(self, key):
        global connection
        storeCountry = country_operations()
        storeTeam = team_operations()
        storeGender = gender_operations()
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT objectid, name, surname,  countryid, teamid, birthday, genderid FROM coach where (objectid=%s and deleted=0)"""
            cursor.execute(statement, (key,))
            id,name,surname,countryid,teamid,birthyear,genderid=cursor.fetchone()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()

        return Coach(id,name,surname,countryid, storeCountry.get_country(countryid), teamid, storeTeam.get_team(teamid), birthyear, genderid, storeGender.get_gender(genderid), 0)

    def update_coach(self, key, name, surname, countryid, teamid, birthyear, genderid):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """update coach set (name, surname, countryid, teamid, birthday, genderid) = (%s,%s,%s,%s,%s, %s) where (objectid=(%s))"""
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