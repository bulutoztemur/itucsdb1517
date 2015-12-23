Parts Implemented by Berat TAŞFİLİZ
===================================
**Coach Entity:**

Coaches are kept in a table which has eight columns:

   * Object ID(Primary Key)
   * Name
   * Surname
   * Countryid(Foreign Key)
   * Teamid(Foreign Key)
   * Birthday
   * Genderid(Foreign Key)
   * Deleted

Object ID of Coach objects is referenced to team table. At the same time, countryid, teamid and genderid references to country, team, gender tables.

SQL Code:

   .. code-block:: sql

      CREATE TABLE coach (
          objectid integer NOT NULL,
          name character varying,
          surname character varying,
          countryid integer,
          teamid integer,
          birthday date,
          genderid integer,
          deleted integer DEFAULT 0 NOT NULL
      );

Python classes and functions are used to make connection between the user and the database. In coach class countryid,
teamid,genderid are used as foreign key. They references to obligatory tables.

   *Coach class to handle and process the information when it is necessary:

   .. code-block:: python

    class Coach:
    def __init__(self, objectid, name, surname, countryid, country, teamid, team, birthyear, genderid, gender, deleted):
        self.objectid = objectid
        self.name = name
        self.surname = surname
        self.countryid = countryid
        self.country = country
        self.teamid = teamid
        self.team = team
        self.birthyear = birthyear
        self.genderid = genderid
        self.gender = gender
        self.deleted = deleted

   *Coach_operations class to keep add,update, delete and print operations for the table.

**"get_coaches" function:**

Returns all the rows of the table with the SQL query below:

   .. code-block:: sql

      SELECT coach.objectid, coach.name, coach.surname, coach.countryid, coach.teamid, coach.birthday, coach.genderid FROM coach WHERE coach.deleted = 0 ORDER BY objectid;

**"add_coach" function:**

This function adds a new coach object to database by taking parameters

   .. code-block:: python

      cursor.execute("""INSERT INTO coach (name, surname, countryid, teamid, birthday, genderid) VALUES (%s, %s, %s, %s, %s, %s)""",(Coach.name,Coach.surname,Coach.countryid,Coach.teamid, Coach.birthyear, Coach.genderid))

**"get_coach" function:**

Takes Object ID as a parameter and gets the corresponding row to return with the code below:

   .. code-block:: python

      statement = """SELECT objectid, name, surname,  countryid, teamid, birthday, genderid FROM coach where (objectid=%s and deleted=0)"""
      cursor.execute(statement, (key,))

**"update_coach" function:**

Takes Object ID and name as a parameter and updates the corresponding row with the code below:

   .. code-block:: python
      statement = """update coach set (name, surname, countryid, teamid, birthday, genderid) = (%s,%s,%s,%s,%s, %s) where (objectid=(%s))"""
      cursor.execute(statement, (name, surname, countryid, teamid, birthyear, genderid, key,))


It returns a string to the front end in order to inform it whether the update operation is successful or not. If so, it returns "success". If something wrong happened in the database, it returns "databaseerror". If there is an integrity error, it returns "integrityerror".


**"delete_coach" function:**

Takes Object ID as a parameter and deletes the corresponding row with the code below:

   .. code-block:: python
      statement = """delete from coach where (objectid=(%s))"""
      cursor.execute(statement, (key,))

It returns a string just like it does in the update function.

In default, it really deletes the row from the table. If preferred, delete operation can be done by just simply modifying "deleted" column. If so, additional operations may be needed to handle.

**Country Entity:**

Countries are kept in a table which has three columns:

   Countries are kept in a table which has three columns:

   * Object ID(Primary Key)
   * Name
   * Deleted

Object ID of country objects are referenced to team, player and coach table. There is not any foreign key on this table.


SQL Code:

   .. code-block:: sql

      CREATE TABLE country (
          objectid integer NOT NULL,
          name character varying,
          deleted integer DEFAULT 0 NOT NULL
      );


Python classes and functions are used to make connection between the user and the database.

   *Country class to handle and process the information when it is necessary:

   .. code-block:: python

    class Country:
    def __init__(self, objectid, name, deleted):
        self.objectid = objectid
        self.name = name
        self.deleted = deleted

   *A country_operations class to keep add,update, delete and print operations for the table.

**"get_countries" function:**

Returns all the rows of the table with the SQL query below:

   .. code-block:: sql

      SELECT objectid, name FROM country WHERE deleted=0 ORDER BY objectid;

**"add_country" function:**

This function adds a new country object to database by taking only name parameter.

   .. code-block:: python

      cursor.execute("""INSERT INTO country (name) VALUES (%s)""",(Country.name,))

**"get_country" function:**

Takes Object ID as a parameter and gets the corresponding row to return with the code below:

   .. code-block:: python

      statement = """SELECT objectid, name FROM country where (objectid=%s and deleted=0)"""
      cursor.execute(statement, (key,))

**"update_country" function:**

Takes Object ID and name as a parameter and updates the corresponding row with the code below:

   .. code-block:: python

      statement = """update country set (name) = (%s) where (objectid=(%s))"""
      cursor.execute(statement, (name, key,))

It returns a string to the front end in order to inform it whether the update operation is successful or not. If so, it returns "success". If something wrong happened in the database, it returns "databaseerror". If there is an integrity error, it returns "integrityerror".


**"delete_country" function:**

Takes Object ID as a parameter and deletes the corresponding row with the code below:

   .. code-block:: python

      statement = """delete from country where (objectid=(%s))"""
      cursor.execute(statement, (key,))

It returns a string just like it does in the update function.

In default, it really deletes the row from the table. If preferred, delete operation can be done by just simply modifying "deleted" column just like the coach entity. If so, additional operations may be needed to handle.


**Team Entity:**

Coaches are kept in a table which has seven columns:

   * Object ID(Primary Key)
   * Name
   * Shirt Color
   * Foundation Date
   * Countryid(Foreign Key)
   * Courtid(Foreign Key)
   * Deleted

Object ID of team entity is referenced to match table. At the same time, countryid and courtid references to country and court tables.

SQL Code:

   .. code-block:: sql

      CREATE TABLE team (
          objectid integer NOT NULL,
          name character varying,
          shirtcolour character varying,
          foundationdate date,
          countryid integer,
          courtid integer,
          deleted integer DEFAULT 0 NOT NULL
      );

Python classes and functions are used to make connection between the user and the database.

   *Team class to handle and process the information when it is necessary:

   .. code-block:: python

      class Team:
      def __init__(self, objectid, name, color, date, countryid, country, courtid, court, deleted):
        self.objectid = objectid
        self.name = name
        self.color = color
        self.date = date
        self.countryid = countryid
        self.country = country
        self.courtid = courtid
        self.court = court
        self.deleted = deleted

   *A team_operations class to keep add,update, delete and print operations for the table.


**"get_teams" function:**

Returns all the rows of the table with the SQL query below:

   .. code-block:: sql

      SELECT team.objectid, team.name, team.shirtcolour, team.foundationdate, team.countryid,team.courtid FROM team WHERE team.deleted = 0 ORDER BY objectid;

**"add_team" function:**

This function adds a new team object to database by taking parameters such as name, shirtcolour, foundationdate, countryid, courtid:

   .. code-block:: python

      cursor.execute("""INSERT INTO team (name, shirtcolour, foundationdate, countryid, courtid) VALUES (%s, %s, %s, %s, %s)""",(Team.name,Team.color,Team.date,Team.countryid,Team.courtid))

**"get_team" function:**

Takes Object ID as a parameter and gets the corresponding row to return with the code below:

   .. code-block:: python

      statement = """SELECT objectid, name, shirtcolour, foundationdate, countryid, courtid FROM team where (objectid=%s and deleted=0)"""
      cursor.execute(statement, (key,))

**"update_team" function:**

Takes Object ID and name as a parameter and updates the corresponding row with the code below:

   .. code-block:: python

      statement = """update team set (name, shirtcolour, foundationdate, countryid, courtid) = (%s,%s,%s,%s,%s) where (objectid=(%s))"""
      cursor.execute(statement, (name, color, date, countryid, courtid, key,))

It returns a string to the front end in order to inform it whether the update operation is successful or not. If so, it returns "success". If something wrong happened in the database, it returns "databaseerror". If there is an integrity error, it returns "integrityerror".


**"delete_team" function:**

Takes Object ID as a parameter and deletes the corresponding row with the code below:

   .. code-block:: python

      statement = """delete from team where (objectid=(%s))"""
      cursor.execute(statement, (key,))

It returns a string just like it does in the update function.

In default, it really deletes the row from the table. If preferred, delete operation can be done by just simply modifying "deleted" column just like the coach entity. If so, additional operations may be needed to handle.
