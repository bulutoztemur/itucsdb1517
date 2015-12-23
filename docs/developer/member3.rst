Parts Implemented by Bulut Öztemur
==================================
I have worked on transfer, hand, season entities on this project.

**Transfer Entity:**

Transfers table includes 6 columns:
   * objectid (Primary Key)
   * playerid (FK) (references player table)
   * oldteamid (FK) (references team table)
   * newteamid (FK) (references team table)
   * seasonid (FK) (references season table)
   * deleted

SQL Code:

   .. code-block:: sql

    CREATE TABLE transfer (
       objectid integer NOT NULL,
       playerid integer,
       oldteamid integer,
       newteamid integer,
       seasonid integer,
       deleted integer DEFAULT 0 NOT NULL
   );

Python classes and functions are used to make connection between the user and the database.

   *Transfer class to handle and process the information when it is necessary:

   .. code-block:: python

    class Transfer:
    def __init__(self, objectid, playerid, player, oldteamid, oldteam, newteamid, newteam, seasonid,season, deleted):
        self.objectid = objectid
        self.playerid = playerid
        self.player = player
        self.oldteamid = oldteamid
        self.oldteam = oldteam
        self.newteamid = newteamid
        self.newteam = newteam
        self.seasonid = seasonid
        self.season = season
        self.deleted = deleted

   *A transfer_operations class to keep add,update, delete and print operations for the table.

**"get_transfers" function:**

Simply returns all the rows of the table with the SQL query below:

   .. code-block:: sql

      SELECT transfer.objectid, transfer.playerid, transfer.oldteamid, transfer.newteamid, transfer.seasonid FROM transfer where transfer.deleted=0 ORDER BY objectid

**"add_transfer" function:**

Adds the given transfer object which it takes as a parameter, to the table with the python code below:

   .. code-block:: python

      cursor.execute("""INSERT INTO transfer (playerid, oldteamid, newteamid, seasonid) VALUES (%s, %s, %s, %s)""",(Transfer.playerid,Transfer.oldteamid,Transfer.newteamid,Transfer.seasonid))

**"get_transfer" function:**

Takes Object ID as a parameter and gets the corresponding row to return with the code below:

   .. code-block:: python

      statement = """SELECT objectid, playerid, oldteamid, newteamid, seasonid FROM transfer where (objectid=%s and deleted=0)"""
      cursor.execute(statement, (key,))

**"update_transfer" function:**

Takes Object ID and name as a parameter and updates the corresponding row with the code below:

      .. code-block:: python

         statement = """update transfer set (playerid, oldteamid, newteamid, seasonid) = (%s,%s,%s,%s) where (objectid=(%s))"""
         cursor.execute(statement, (playerid, oldteamid, newteamid, seasonid, key,))

It returns a string to the front end in order to inform it whether the update operation is successful or not. If so, it returns "success". If something wrong happened in the database, it returns "databaseerror". If there is an integrity error, it returns "integrityerror".


**"delete_transfer" function:**

Takes Object ID as a parameter and deletes the corresponding row with the code below:

   .. code-block:: python

      statement = """delete from transfer where (objectid=(%s))"""
      cursor.execute(statement, (key,))

It returns a string just like it does in the update function.

In default, it really deletes the row from the table. If preferred, delete operation can be done by just simply modifying "deleted" column. If so, additional operations may be needed to handle.

--------------------------------------------------------------------------

**Hand Entity:**

Hand table includes 3 columns:

   * objectid (Primary Key)
   * name
   * deleted

   Objectid column in hand table is referenced from player table because of specifying which hand player uses.

   SQL Code:

   .. code-block:: sql

    CREATE TABLE hand (
      objectid integer NOT NULL,
      name character varying,
      deleted integer DEFAULT 0 NOT NULL
    );

Python classes and functions are used to make connection between the user and the database.

   *Hand class to handle and process the information when it is necessary:

   .. code-block:: python

    class Hand:
    def __init__(self, objectid, name, deleted):
        self.objectid = objectid
        self.name = name
        self.deleted = deleted

    *A hand_operations class to keep add,update, delete and print operations for the table.

**"get_hands" function:**

Simply returns all the rows of the table with the SQL query below:

    .. code-block:: sql

      SELECT objectid, name FROM hand WHERE deleted=0 ORDER BY objectid

**"add_hand" function:**

Adds the given hand object which it takes as a parameter, to the table with the python code below:

   .. code-block:: python

      cursor.execute("""INSERT INTO hand (name) VALUES (%s)""",(Hand.name,))

**"get_hand" function:**

Takes Object ID as a parameter and gets the corresponding row to return with the code below:

   .. code-block:: python

      statement = """SELECT objectid, name FROM hand where (objectid=%s and deleted=0)"""
      cursor.execute(statement, (key,))

**"update_hand" function:**

Takes Object ID and type as a parameter and updates the corresponding row with the code below:

   .. code-block:: python

      statement = """update hand set (name) = (%s) where (objectid=(%s))"""
      cursor.execute(statement, (name, key,))

It returns a string to the front end in order to inform it whether the update operation is successful or not. If so, it returns "success". If something wrong happened in the database, it returns "databaseerror". If there is an integrity error, it returns "integrityerror".

**"delete_hand" function:**

Takes Object ID as a parameter and deletes the corresponding row with the code below:

   .. code-block:: python

      statement = """delete from hand where (objectid=(%s))"""
      cursor.execute(statement, (key,))

It returns a string just like it does in the update function.

In default, it really deletes the row from the table. If preferred, delete operation can be done by just simply modifying "deleted" column just like the transfer entity. If so, additional operations may be needed to handle.

--------------------------------------------------------------------------

**Season Entity:**

Season table includes 3 columns:

   * objectid (Primary Key)
   * name
   * deleted

   Objectid column on season table is referenced from match, transfer and statistic tables.

   SQL Code:

   .. code-block:: sql

    CREATE TABLE season (
      objectid integer NOT NULL,
      name character varying,
      deleted integer DEFAULT 0 NOT NULL
    );

Python classes and functions are used to make connection between the user and the database.

   *Season class to handle and process the information when it is necessary:

   .. code-block:: python

    class Season:
    def __init__(self, objectid, name, deleted):
        self.objectid = objectid
        self.name = name
        self.deleted = deleted

   *A season_operations class to keep add,update, delete and print operations for the table.

**"get_seasons" function:**

Returns all the rows of the table with the SQL queres and python codes below:

   .. code-block:: python

      statement = """SELECT objectid, name FROM season WHERE deleted=0 ORDER BY objectid"""

**"add_season" function:**

Adds the given season object which it takes as a parameter, to the table with the python code below:

   .. code-block:: python

      cursor.execute("""INSERT INTO season (name) VALUES (%s)""",(Season.name,))

**"get_season" function:**

Takes Object ID as a parameter and gets the corresponding row to return with the code below:

   .. code-block:: python

      statement = """SELECT objectid, name FROM season where (objectid=%s and deleted=0)"""
      cursor.execute(statement, (key,))

**"update_season" function:**

Takes Object ID and type as a parameter and updates the corresponding row with the code below:

   .. code-block:: python

      statement = """update season set (name) = (%s) where (objectid=(%s))"""
      cursor.execute(statement, (name, key,))

It returns a string to the front end in order to inform it whether the update operation is successful or not. If so, it returns "success". If something wrong happened in the database, it returns "databaseerror". If there is an integrity error, it returns "integrityerror".

**"delete_season" function:**

Takes Object ID as a parameter and deletes the corresponding row with the code below:

   .. code-block:: python

      statement = """delete from season where (objectid=(%s))"""
      cursor.execute(statement, (key,))

It returns a string just like it does in the update function.

In default, it really deletes the row from the table. If preferred, delete operation can be done by just simply modifying "deleted" column just like the transfer entity. If so, additional operations may be needed to handle.
