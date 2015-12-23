Parts Implemented by Burak Sayın
================================
I have worked on the necessary operations for the position, gender and player entities.

**Position Entity:**

Positions are kept in a table which has three columns:

   * Object ID(Primary Key)
   * Name
   * Deleted

Positions are referenced in the player table as a valid position of the corresponding player in order to avoid inconsistent player information.

SQL Code:

   .. code-block:: sql

      CREATE TABLE "position" (
    objectid integer NOT NULL,
    name character varying,
    deleted integer DEFAULT 0 NOT NULL
    );

Python classes and functions are used to make connection between the user and the database.

   *Position class to handle and process the information when it is necessary:

   .. code-block:: python

    class Position:
    def __init__(self, objectid, name, deleted):
        self.objectid = objectid
        self.name = name
        self.deleted = deleted

   *A position_operations class to keep add,update, delete and print operations for the table.

**"get_positions" function:**

Simply returns all the rows of the table with the SQL query below:

   .. code-block:: sql

      SELECT objectid, name FROM position WHERE position.deleted = 0 ORDER BY objectid;

**"add_position" function:**

Adds the given position object which it takes as a parameter, to the table with the python code below:

   .. code-block:: python

      cursor.execute("""INSERT INTO position (name) VALUES (%s)""",(Position.name,))

**"get_position" function:**

Takes Object ID as a parameter and gets the corresponding row to return with the code below:

   .. code-block:: python

      statement = """SELECT objectid, name FROM position where (objectid=%s and deleted=0)"""
      cursor.execute(statement, (key,))

**"update_position" function:**

Takes Object ID and name as a parameter and updates the corresponding row with the code below:

   .. code-block:: python

      statement = """update position set (name) = (%s) where (objectid=(%s))"""
      cursor.execute(statement, (name, key,))

It returns a string to the front end in order to inform it whether the update operation is successful or not. If so, it returns "success". If something wrong happened in the database, it returns "databaseerror". If there is an integrity error, it returns "integrityerror".


**"delete_position" function:**

Takes Object ID as a parameter and deletes the corresponding row with the code below:

   .. code-block:: python

      statement = """delete from position where (objectid=(%s))"""
      cursor.execute(statement, (key,))

It returns a string just like it does in the update function.

In default, it really deletes the row from the table. If preferred, delete operation can be done by just simply modifying "deleted" column. If so, additional operations may be needed to handle.

--------------------------------------------------------------------------

**Gender Entity:**

Genders are kept in a table which has three columns:

   * Object ID(Primary Key)
   * Type
   * Deleted

Genders are referenced in the player and coach tables as the gender of the corresponding player or coach in order to avoid inconsistent information. It has a structure very similiar to position entity.

SQL Code:

   .. code-block:: sql

    CREATE TABLE gender (
    objectid integer NOT NULL,
    type character varying,
    deleted integer DEFAULT 0 NOT NULL
    );

Python classes and functions are used to make connection between the user and the database.

   *Gender class to handle and process the information when it is necessary:

   .. code-block:: python

    class Gender:
    def __init__(self, objectid, type, deleted):
        self.objectid = objectid
        self.type = type
        self.deleted = deleted

   *A gender_operations class to keep add,update, delete and print operations for the table.

**"get_genders" function:**

Simply returns all the rows of the table with the SQL query below:

   .. code-block:: sql

      SELECT objectid, type FROM gender WHERE deleted=0 order by objectid;

**"add_gender" function:**

Adds the given gender object which it takes as a parameter, to the table with the python code below:

   .. code-block:: python

      cursor.execute("""INSERT INTO gender (type) VALUES (%s)""",(Gender.type,))

**"get_gender" function:**

Takes Object ID as a parameter and gets the corresponding row to return with the code below:

   .. code-block:: python

      statement = """SELECT objectid, type FROM gender where (objectid=%s and deleted=0)"""
      cursor.execute(statement, (key,))

**"update_gender" function:**

Takes Object ID and type as a parameter and updates the corresponding row with the code below:

   .. code-block:: python

      statement = """update gender set (type) = (%s) where (objectid=(%s))"""
      cursor.execute(statement, (type, key,))

It returns a string to the front end in order to inform it whether the update operation is successful or not. If so, it returns "success". If something wrong happened in the database, it returns "databaseerror". If there is an integrity error, it returns "integrityerror".

**"delete_gender" function:**

Takes Object ID as a parameter and deletes the corresponding row with the code below:

   .. code-block:: python

      statement = """DELETE FROM gender WHERE (objectid=(%s))"""
      cursor.execute(statement, (key,))

It returns a string just like it does in the update function.

In default, it really deletes the row from the table. If preferred, delete operation can be done by just simply modifying "deleted" column just like the position entity. If so, additional operations may be needed to handle.

--------------------------------------------------------------------------

**Player Entity:**

Players are kept in a table which has fourteen columns:

   * Object ID(Primary Key)
   * Name
   * Surname
   * Birthdate
   * Height
   * Weight
   * Start Date
   * Team ID(Foreign key)
   * Country ID(Foreign key)
   * Gender ID(Foreign key)
   * Position ID(Foreign key)
   * Hand ID(Foreign key)
   * Number
   * Deleted

Team ID references to the teams table, Country ID references to the countries table, Gender ID references to the genders table, Position ID references to the positions table and Hand ID references to the hands table.

SQL Code:

   .. code-block:: sql

    CREATE TABLE player (
    objectid integer NOT NULL,
    name character varying,
    surname character varying,
    birthdate date,
    height numeric,
    weight numeric,
    startdate date,
    teamid integer,
    countryid integer,
    genderid integer,
    positionid integer,
    handid integer,
    number integer,
    deleted integer DEFAULT 0 NOT NULL
    );

Python classes and functions are used to make connection between the user and the database.

   *Player class to handle and process the information when it is necessary:

   .. code-block:: python

    class Player:
    def __init__(self, objectid, name, surname, birthdate, height, weight, startdate, teamid, team, countryid, country, genderid, gender, positionid, position, handid, hand, number, deleted):
        self.objectid = objectid
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.height = height
        self.weight = weight
        self.startdate = startdate
        self.teamid = teamid
        self.team = team
        self.countryid = countryid
        self.country = country
        self.genderid = genderid
        self.gender = gender
        self.positionid = positionid
        self.position = position
        self.handid = handid
        self.hand = hand
        self.number = number
        self.deleted = deleted

   *A player_operations class to keep add,update, delete and print operations for the table.

**"get_players" function:**

Returns all the rows of the table with the SQL queres and python codes below:

   .. code-block:: python

      statement = """SELECT objectid, name, surname, birthdate, height, weight, startdate, teamid, countryid, genderid, positionid, handid, number FROM player WHERE deleted = 0 ORDER BY objectid"""
      cursor.execute(statement)
      players = [(key, Player(key, name, surname, birthdate, height, weight, startdate, teamid, storeTeam.get_team(teamid),countryid, storeCountry.get_country(countryid), genderid, storeGender.get_gender(genderid), positionid, storePosition.get_position(positionid), handid, storeHand.get_hand(handid), number, 0)) for key, name, surname, birthdate, height, weight, startdate, teamid, countryid, genderid, positionid, handid, number in cursor]
      return players

**"add_player" function:**

Adds the given player object which it takes as a parameter, to the table with the python code below:

   .. code-block:: python

      cursor.execute("""INSERT INTO player (name, surname, birthdate, height, weight, startdate, teamid, countryid, genderid, positionid, handid, number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",(Player.name, Player.surname, Player.birthdate, Player.height, Player.weight, Player.startdate, Player.teamid, Player.countryid, Player.genderid, Player.positionid, Player.handid, Player.number))

**"get_player" function:**

Takes Object ID as a parameter and gets the corresponding row to return with the code below:

   .. code-block:: python

      statement = """SELECT objectid,name, surname, birthdate, height, weight, startdate, teamid, countryid, genderid, positionid, handid, number FROM player WHERE (objectid=%s and deleted=0)"""
      cursor.execute(statement, (key,))
      id,name,surname,birthdate,height,weight,startdate,teamid,countryid,genderid,positionid,handid,number=cursor.fetchone()
      return Player(id, name, surname, birthdate, height, weight, startdate, teamid, storeTeam.get_team(teamid), countryid, storeCountry.get_country(countryid), genderid, storeGender.get_gender(genderid), positionid, storePosition.get_position(positionid), handid, storeHand.get_hand(handid), number, 0)

**"update_player" function:**

Takes Object ID and type as a parameter and updates the corresponding row with the code below:

   .. code-block:: python

      statement = """update player set (name, surname, birthdate, height, weight, startdate, teamid, countryid, genderid, positionid, handid, number) = (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) where (objectid=(%s))"""
      cursor.execute(statement, (name, surname, birthdate, height, weight, startdate, teamid, countryid, genderid, positionid, handid, number, key,))

It returns a string to the front end in order to inform it whether the update operation is successful or not. If so, it returns "success". If something wrong happened in the database, it returns "databaseerror". If there is an integrity error, it returns "integrityerror".

**"delete_player" function:**

Takes Object ID as a parameter and deletes the corresponding row with the code below:

   .. code-block:: python

      statement = """delete from player where (objectid=(%s))"""
      cursor.execute(statement, (key,))

It returns a string just like it does in the update function.

In default, it really deletes the row from the table. If preferred, delete operation can be done by just simply modifying "deleted" column just like the position entity. If so, additional operations may be needed to handle.



