import psycopg2 as dbapi2
from classes.transfer import Transfer
from classes.model_config import dsn, connection
class transfer_operations:
    def __init__(self):
        self.last_key=None

    def get_transfers(self):
        global connection
        transfers=[]
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT objectid, playerid, oldteamid, newteamid, seasonid FROM transfer where deleted=0"""
            cursor.execute(statement)
            transfers = [(key, Transfer(playerid, oldteamid, newteamid, seasonid, 0)) for key, playerid, oldteamid, newteamid, seasonid in cursor]
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
        return transfers

    def add_transfer(self,Transfer):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO transfer (playerid, oldteamid, newteamid, seasonid) VALUES (%s, %s, %s, %s)""",(Transfer.playerid,Transfer.oldteamid,Transfer.newteamid,Transfer.seasonid))
            cursor.close()
            connection.commit()
        except dbapi2.DatabaseError:
            if connection:
                connection.close()
        finally:
            if connection:
                connection.close()

    def get_transfer(self, key):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT objectid, playerid, oldteamid, newteamid, seasonid FROM transfer where (objectid=%s and deleted=0)"""
            cursor.execute(statement, (key,))
            id,playerid,oldteamid,newteamid,seasonid=cursor.fetchone()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
        return Transfer(playerid, oldteamid, newteamid, seasonid, 0)

    def update_transfer(self, key, playerid, oldteamid, newteamid, seasonid):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """update transfer set (playerid, oldteamid, newteamid, seasonid) = (%s,%s,%s,%s) where (objectid=(%s))"""
            cursor.execute(statement, (playerid, oldteamid, newteamid, seasonid, key,))
            connection.commit()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()

    def delete_transfer(self,key):
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """update transfer set deleted = 1 where (objectid=(%s))"""
            cursor.execute(statement, (key,))
            connection.commit()
            cursor.close()
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()