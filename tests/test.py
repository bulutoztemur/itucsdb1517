
import psycopg2 as dbapi2

class deneme:
    def get_teams():
        dsn = """user=vagrant password=vagrant host=127.0.0.1 port=54321 dbname=itucsdb"""
        connection = dbapi2.connect(dsn)

        cursor = connection.cursor()
        statement = """SELECT objectid, name, shirtColour FROM team"""
        cursor.execute(statement)
        for id,name,color in cursor:
            print (name)
        cursor.close()
        connection.close()
        return teams
