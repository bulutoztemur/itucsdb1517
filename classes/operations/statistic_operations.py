import psycopg2 as dbapi2
from classes.statistic import Statistic

from classes.operations.season_operations import season_operations
from classes.operations.player_operations import player_operations
from classes.model_config import dsn, connection
class statistic_operations:
    def __init__(self):
        self.last_key=None

    def get_statistics(self):
        global connection
        storeSeason = season_operations()
        storePlayer = player_operations()
        statistics=[]
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT statistic.objectid, statistic.assistnumber, statistic.blocknumber, statistic.score, statistic.cardnumber, statistic.seasonid, statistic.playerid FROM statistic where statistic.deleted=0"""
            cursor.execute(statement)
            statistics = [(key, Statistic(key, assistnumber, blocknumber,score, cardnumber, seasonid, storeSeason.get_season(seasonid), playerid, storePlayer.get_player(playerid), 0)) for key, assistnumber, blocknumber, score, cardnumber, seasonid, playerid in cursor]
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()

        return statistics

    def add_statistic(self,Statistic):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO statistic (assistnumber, blocknumber, score, cardnumber, seasonid, playerid) VALUES (%s, %s, %s, %s, %s, %s)""",(Statistic.assistnumber,Statistic.blocknumber,Statistic.score,Statistic.cardnumber,Statistic.seasonid,Statistic.playerid))
            cursor.close()
            connection.commit()
        except dbapi2.DatabaseError:
            if connection:
                connection.close()
        finally:
            if connection:
                connection.close()

    def get_statistic(self, key):
        global connection
        storeSeason = season_operations()
        storePlayer = player_operations()
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT objectid, assistnumber, blocknumber, score, cardnumber, seasonid, playerid FROM statistic where (objectid=%s and deleted=0)"""
            cursor.execute(statement, (key,))
            id,assistnumber,blocknumber, score, cardnumber, seasonid, playerid=cursor.fetchone()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
        return Statistic(id, assistnumber, blocknumber, score, cardnumber, seasonid, storeSeason.get_season(seasonid), playerid, storePlayer.get_player(playerid), 0)

    def update_statistic(self, key, assistnumber, blocknumber, score, cardnumber, seasonid, playerid):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """update statistic set (assistnumber, blocknumber, score, cardnumber, seasonid, playerid) = (%s,%s,%s,%s,%s,%s) where (objectid=(%s))"""
            cursor.execute(statement, (assistnumber, blocknumber, score, cardnumber, seasonid, playerid, key,))
            connection.commit()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()

    def delete_statistic(self,key):
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """update statistic set deleted = 1 where (objectid=(%s))"""
            cursor.execute(statement, (key,))
            connection.commit()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()