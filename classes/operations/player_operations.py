import psycopg2 as dbapi2
from classes.player import Player
from classes.team import Team
from classes.operations.team_operations import team_operations
from classes.country import Country
from classes.operations.country_operations import country_operations
from classes.gender import Gender
from classes.operations.gender_operations import gender_operations
from classes.position import Position
from classes.operations.position_operations import position_operations
from classes.hand import Hand
from classes.operations.hand_operations import hand_operations

from classes.model_config import dsn, connection
class player_operations:
    def __init__(self):
        self.last_key=None

    def get_players(self):
        players=[]
        global connection
        storeCountry = country_operations()
        storeTeam = team_operations()
        storeGender = gender_operations()
        storePosition = position_operations()
        storeHand = hand_operations()
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT objectid, name, surname, birthdate, height, weight, startdate, teamid, countryid, genderid, positionid, handid, number FROM player WHERE deleted = 0"""
            cursor.execute(statement)
            players = [(key, Player(key, name, surname, birthdate, height, weight, startdate, teamid, storeTeam.get_team(teamid),countryid, storeCountry.get_country(countryid), genderid, storeGender.get_gender(genderid), positionid, storePosition.get_position(positionid), handid, storeHand.get_hand(handid), number, 0)) for key, name, surname, birthdate, height, weight, startdate, teamid, countryid, genderid, positionid, handid, number in cursor]
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
        return players

    def add_player(self,Player):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO player (name, surname, birthdate, height, weight, startdate, teamid, countryid, genderid, positionid, handid, number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",(Player.name, Player.surname, Player.birthdate, Player.height, Player.weight, Player.startdate, Player.teamid, Player.countryid, Player.genderid, Player.positionid, Player.handid, Player.number))
            cursor.close()
            connection.commit()
        except dbapi2.DatabaseError:
            if connection:
                connection.close()
        finally:
            if connection:
                connection.close()
    def get_player(self, key):
        global connection
        storeCountry = country_operations()
        storeTeam = team_operations()
        storeGender = gender_operations()
        storePosition = position_operations()
        storeHand = hand_operations()
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT objectid,name, surname, birthdate, height, weight, startdate, teamid, countryid, genderid, positionid, handid, number FROM player WHERE (objectid=%s and deleted=0)"""
            cursor.execute(statement, (key,))
            id,name,surname,birthdate,height,weight,startdate,teamid,countryid,genderid,positionid,handid,number=cursor.fetchone()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()

        return Player(id, name, surname, birthdate, height, weight, startdate, teamid, storeTeam.get_team(teamid), countryid, storeCountry.get_country(countryid), genderid, storeGender.get_gender(genderid), positionid, storePosition.get_position(positionid), handid, storeHand.get_hand(handid), number, 0)

    def update_player(self, key, name, surname, birthdate, height, weight, startdate, teamid, countryid, genderid, positionid, handid, number):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """update player set (name, surname, birthdate, height, weight, startdate, teamid, countryid, genderid, positionid, handid, number) = (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) where (objectid=(%s))"""
            cursor.execute(statement, (name, surname, birthdate, height, weight, startdate, teamid, countryid, genderid, positionid, handid, number, key,))
            connection.commit()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()

    def delete_player(self,key):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """update player set deleted = 1 where (objectid=(%s))"""
            cursor.execute(statement, (key,))
            connection.commit()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()