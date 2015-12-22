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


User stuff

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
