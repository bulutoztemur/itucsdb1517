class User:
    def __init__(self, objectid, username, password, role='user', roleid=1, name='', surname='', birthdate=''):
        self.objectid = objectid
        self.username = username
        self.password = password
        self.roleid = roleid
        self.role = role
        self.name = name
        self.surname = surname
        self.birthdate = birthdate