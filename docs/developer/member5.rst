Parts Implemented by İsmail Tunahan Er
======================================
In this project Court, Match, and Statistic entities are done by me.

**Court Entity:**

Courts are kept in a table which has five columns:

   * Object ID(Primary Key)
   * Name
   * Adress
   * Capacity
   * Deleted

Courts are referenced to the several entities such as match, and team. "Deleted" column is inserted for possible lazy deletion operations in future for all entities.

SQL Code:

   .. code-block:: sql

      CREATE TABLE court (
       objectid integer NOT NULL,
       name character varying,
       address character varying,
       capacity numeric,
       deleted integer DEFAULT 0 NOT NULL
      );

Python classes and functions are used to make connection between the user and the database.

   *Court class to handle and process the information when it is necessary:

   .. code-block:: python

    class Court:
    def __init__(self, objectid, name, address, capacity, deleted):
        self.objectid = objectid
        self.name = name
        self.address = address
        self.capacity = capacity
        self.deleted = deleted

   *A court_operations class to keep add,update, delete and print operations for the table.

**"get_courts" function:**

Simply returns all the rows of the table with the SQL query below:

   .. code-block:: sql

      SELECT objectid, name, address, capacity FROM court WHERE deleted=0 ORDER BY objectid;

**"add_court" function:**

Adds the given court object which it takes as a parameter, to the table with the python code below:

   .. code-block:: python

      cursor.execute("""INSERT INTO court (name, address, capacity) VALUES (%s, %s, %s)""",(Court.name,Court.address,Court.capacity))

**"get_court" function:**

Takes Object ID as a parameter and gets the corresponding row to return with the code below:

   .. code-block:: python

      statement = """SELECT objectid, name, address, capacity FROM court where (objectid=%s and deleted=0)"""
      cursor.execute(statement, (key,))

**"update_court" function:**

Takes Object ID and name as a parameter and updates the corresponding row with the code below:

   .. code-block:: python

      statement = """update court set (name, address, capacity) = (%s,%s,%s) where (objectid=(%s))"""
      cursor.execute(statement, (name, address, capacity, key,))

It returns a string to the front end in order to inform it whether the update operation is successful or not. If so, it returns "success". If something wrong happened in the database, it returns "databaseerror". If there is an integrity error, it returns "integrityerror".


**"delete_court" function:**

Takes Object ID as a parameter and deletes the corresponding row with the code below:

   .. code-block:: python

      statement = """delete from court where (objectid=(%s))"""
      cursor.execute(statement, (key,))

It returns a string just like it does in the update function.

In default, it really deletes the row from the table. If preferred, delete operation can be done by just simply modifying "deleted" column. If so, additional operations may be needed to handle.

--------------------------------------------------------------------------

**Match Entity:**

Matches are kept in a table which has six columns:

   * Object ID(Primary Key)
   * Home Team ID (Foreign Key referenced to Team Table)
   * Away Team ID (Foreign Key referenced to Team Table)
   * Court ID (Foreign Key referenced to Court Table)
   * Match Date
   * Deleted


SQL Code:

   .. code-block:: sql

    CREATE TABLE match (
    objectid integer NOT NULL,
    hometeamid integer,
    awayteamid integer,
    courtid integer,
    matchdate date,
    deleted integer DEFAULT 0 NOT NULL
    );

Python classes and functions are used to make connection between the user and the database.

   *Match class to handle and process the information when it is necessary:

   .. code-block:: python

    class Match:
    def __init__(self, objectid, hometeamid, hometeam, awayteamid, awayteam, courtid, court, matchdate, deleted):
        self.objectid = objectid
        self.hometeamid = hometeamid
        self.hometeam = hometeam
        self.awayteamid = awayteamid
        self.awayteam = awayteam
        self.courtid = courtid
        self.court = court
        self.matchdate = matchdate
        self.deleted = deleted

   *A match_operations class to keep add,update, delete and print operations for the table.

**"get_matches" function:**

Simply returns all the rows of the table with the SQL query below. It uses the constructers of referenced tables and returns the whole referenced data.:

   .. code-block:: python

      statement = """SELECT objectid, hometeamid, awayteamid, courtid, matchdate FROM match WHERE deleted = 0 ORDER BY objectid"""
      cursor.execute(statement)
      matches = [(key, Match(key, hometeamid, storeTeam.get_team(hometeamid), awayteamid, storeTeam.get_team(awayteamid), courtid, storeCourt.get_court(courtid), matchdate, 0)) for key, hometeamid, awayteamid, courtid, matchdate in cursor]
      return matches

**"add_match" function:**

Adds the given gender object which it takes as a parameter, to the table with the python code below:

   .. code-block:: python

      cursor.execute("""INSERT INTO match (hometeamid, awayteamid, courtid, matchdate) VALUES (%s, %s, %s, %s)""",(Match.hometeamid, Match.awayteamid, Match.courtid, Match.matchdate))

**"get_match" function:**

Takes Object ID as a parameter and gets the corresponding row to return with the code below:

   .. code-block:: python

      statement = """SELECT objectid, hometeamid, awayteamid, courtid, matchdate FROM match WHERE (objectid=%s and deleted=0)"""
      cursor.execute(statement, (key,))

**"update_match" function:**

Takes Object ID and type as a parameter and updates the corresponding row with the code below:

   .. code-block:: python

      statement = """update match set (hometeamid, awayteamid, courtid, matchdate) = (%s,%s,%s,%s) where (objectid=(%s))"""
      cursor.execute(statement, (hometeamid, awayteamid, courtid, matchdate, key,))

It returns a string to the front end in order to inform it whether the update operation is successful or not. If so, it returns "success". If something wrong happened in the database, it returns "databaseerror". If there is an integrity error, it returns "integrityerror".

**"delete_match" function:**

Takes Object ID as a parameter and deletes the corresponding row with the code below:

   .. code-block:: python

      statement = """delete from match where (objectid=(%s))"""
      cursor.execute(statement, (key,))

It returns a string just like it does in the update function.

In default, it really deletes the row from the table. If preferred, delete operation can be done by just simply modifying "deleted" column just like the court entity. If so, additional operations may be needed to handle.

--------------------------------------------------------------------------

**Statistic Entity:**

Statistics are kept in a table which has fourteen columns:

   * Object ID(Primary Key)
   * Assist Number
   * Block Number
   * Score
   * Card Number
   * Season ID (Foreign Key referenced to Season Table)
   * Player ID (Foreign Key referenced to Player Table)
   * Deleted

Season ID references to the seasons table and Player ID references to the player table.

SQL Code:

   .. code-block:: sql

    CREATE TABLE statistic (
    objectid integer NOT NULL,
    assistnumber integer,
    blocknumber integer,
    score integer,
    cardnumber integer,
    seasonid integer,
    playerid integer,
    deleted integer DEFAULT 0 NOT NULL
    );

Python classes and functions are used to make connection between the user and the database.

   *Player class to handle and process the information when it is necessary:

   .. code-block:: python

    class Statistic:
    class Statistic:
    def __init__(self, objectid, assistnumber, blocknumber, score, cardnumber, seasonid, season, playerid, player, deleted):
        self.objectid = objectid
        self.assistnumber = assistnumber
        self.blocknumber = blocknumber
        self.score = score
        self.cardnumber = cardnumber
        self.seasonid = seasonid
        self.season = season
        self.playerid = playerid
        self.player = player
        self.deleted = deleted

   *A statistic_operations class to keep add,update, delete and print operations for the table.

**"get_statistics" function:**

Returns all the rows of the table with the SQL queres and python codes below:

   .. code-block:: python

      statement = """SELECT statistic.objectid, statistic.assistnumber, statistic.blocknumber, statistic.score, statistic.cardnumber, statistic.seasonid, statistic.playerid FROM statistic where statistic.deleted=0 ORDER BY objectid"""
      cursor.execute(statement)
      statistics = [(key, Statistic(key, assistnumber, blocknumber,score, cardnumber, seasonid, storeSeason.get_season(seasonid), playerid, storePlayer.get_player(playerid), 0)) for key, assistnumber, blocknumber, score, cardnumber, seasonid, playerid in cursor]
      return statistics

**"add_statistic" function:**

Adds the given statistic object which it takes as a parameter, to the table with the python code below:

   .. code-block:: python

      cursor.execute("""INSERT INTO statistic (assistnumber, blocknumber, score, cardnumber, seasonid, playerid) VALUES (%s, %s, %s, %s, %s, %s)""",(Statistic.assistnumber,Statistic.blocknumber,Statistic.score,Statistic.cardnumber,Statistic.seasonid,Statistic.playerid))

**"get_player" function:**

Takes Object ID as a parameter and gets the corresponding row to return with the code below:

   .. code-block:: python

      statement = """SELECT objectid, assistnumber, blocknumber, score, cardnumber, seasonid, playerid FROM statistic where (objectid=%s and deleted=0)"""
      cursor.execute(statement, (key,))
      id,assistnumber,blocknumber, score, cardnumber, seasonid, playerid=cursor.fetchone()
      return Statistic(id, assistnumber, blocknumber, score, cardnumber, seasonid, storeSeason.get_season(seasonid), playerid, storePlayer.get_player(playerid), 0)

**"update_statistic" function:**

Takes Object ID and type as a parameter and updates the corresponding row with the code below:

   .. code-block:: python

      statement = """update statistic set (assistnumber, blocknumber, score, cardnumber, seasonid, playerid) = (%s,%s,%s,%s,%s,%s) where (objectid=(%s))"""
      cursor.execute(statement, (assistnumber, blocknumber, score, cardnumber, seasonid, playerid, key,))

It returns a string to the front end in order to inform it whether the update operation is successful or not. If so, it returns "success". If something wrong happened in the database, it returns "databaseerror". If there is an integrity error, it returns "integrityerror".

**"delete_player" function:**

Takes Object ID as a parameter and deletes the corresponding row with the code below:

   .. code-block:: python

      statement = """delete from statistic where (objectid=(%s))"""
      cursor.execute(statement, (key,))

It returns a string just like it does in the update function.




