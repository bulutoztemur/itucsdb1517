import psycopg2 as dbapi2
from classes.user import User
from classes.model_config import dsn, connection

class user_operations:
    def __init__(self):
        self.last_key=None

    def add_user(self,User):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO usertable (username, password, userroleid) VALUES (%s, %s, 1)""",(User.username,User.password))
            cursor.close()
            connection.commit()
            result = 'success'
        except dbapi2.IntegrityError:
            result = 'integrityerror'
            if connection:
                connection.rollback()
        except dbapi2.DatabaseError:
            result = 'databaseerror'
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
        return result

    def get_user(self, user, passw):
        global connection
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """select u.objectid, u.username, u.password, r.name, u.userroleid from usertable as u inner join userrole as r on u.userroleid=r.objectid where username=%s and password=%s"""
            cursor.execute(statement, (user, passw))
            row=cursor.fetchone()
            if row is not None:
                id, username, password, role, roleid=row
            else:
                id=0
                username=user
                password=passw
                role=''
                roleid=0
        except dbapi2.DatabaseError:
            if connection:
                connection.rollback()
        finally:
            if connection:
                connection.close()
        return User(id,username, password, role, roleid, '', '', '')
