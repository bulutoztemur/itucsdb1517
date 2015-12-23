Developer Guide
===============

Database Design
---------------

There are minor tables which are Courts, Hand, Position, Country, Gender, Season. Also, there are major tables which use the information provided by these minor tables. These major tables are Player, Team, Coach, Statistics, Transfers, Match. Minor tables are referenced as foreign keys to necessary corresponding columns of major tables. PostgreSQL is used to manage the database in this project.

Detailed database relations can be seen in the image below:

   .. figure:: Diagram.png
      :scale: 100 %
      :alt: map to buried treasure

      Database Entity Relation Diagram

We have also user operations in our database design, it is seen in database diagram above. There are 3 tables to handle user operations in database which are usertable, userinformation and userrole. Login information, username and password, are kept in usertable and also it has reference from userrole to specify user role. User roles are kept in userrole table, when we initialize database there are two main roles; user and admin. Roles can be added manually from postgresql interface there is no interface for adding new role in our site design. Additional user information which are name, last name, birthdate etc. are kept in userinformation table. When a new user is registered information that he/she writes goes to this table.


Code
----

**explain the technical structure of your code**

**to include a code listing, use the following example**::

   .. code-block:: python

      class Foo:

         def __init__(self, x):
            self.x = x

.. toctree::

   member1
   member2
   member3
   member4
   member5
