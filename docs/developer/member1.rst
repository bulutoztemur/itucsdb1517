Parts Implemented by Ertuğrul Dalboy
====================================
I  worked on the user operations; *login*, *register*, and *permissions*.

There three tables to handle these operations which are *usertable*, *userrole* and *userinformation*.

**User Role Entity:**

User role table is used to keep user role data consistent. There two roles in our design now but if we add new one we can add it to this table simply.

   .. code-block:: sql

       CREATE TABLE userrole (
       objectid integer NOT NULL,
       name character varying,
       deleted integer DEFAULT 0 NOT NULL
       );

The SQL query that creates user role table is shown above. There 3 columns; objectid, name and deleted. objectid is primary key of table and it is auto-incremented, when a new role is added,it automatically increase the objectid. name is character varying which holds the role name. In our first database design we use lazy deleting which only marks tuple as deleted and then we changed the design but it stays same as before.

In the beginning we have 2 roles; user and admin. If you want to add a new role you shpuld use the phppgadmn or simply use the other postgresql interfaces. In our site interface there is no field to add new role.

User role relation is used as reference table to the usertable which holds the login information. We keep role data as string so we keep it as a seperate table to avoid miswriting.

There is no update, insert or delete operation on userrole table on site interface. It is used only in login and register operations to get userrole or to give user a role.

**User Entity:**

Login information, username, password and role, is kept in user table. We divide user operations into 3 tables. Roles are kept in userrole table because of consistency as I explained in User Role part.
We divide user information into 2 that is why to keep login operations fast and to keep sensitive information securely.
So in our design, user table keeps only login information, when a user logged in, program only selects the login information.

usertable create query is shown below:


   .. code-block:: sql

       CREATE TABLE usertable (
       objectid integer NOT NULL,
       username character varying,
       password bytea,
       userroleid integer,
       userinformationid integer,
       deleted integer DEFAULT 0 NOT NULL
       );

We keep user table as "usertable" since "user" has an special meaning in PostgreSQL. There 6 columns in this table and two of them are foreign keys which references to userrole and userinformation tables.
objectid is primary key and it is auto-incremented, username is character varying, and password is kept as bytea because of security.

There is python class which is User in our project. It keeps all necessary attributes of a user.

   .. code-block:: python

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

User class is used in login operations mostly so we give an default values for fields that not related to login operations and also give role to user as a default value because most of our visiters are users not admins.
This class is designed to used both login and register operations and also my profile page, which is not implemented because of the time.

**Login:** When a user tries log in, get_user function is called defined in user_operations.

   .. code-block:: python

      result=store.get_user(request.form['username'], request.form['password'])

Username and password that user writes to the login page are passed to get_user function as parameters.

**get_user:** Get user function takes user name and password as parameters and return a User object as a result.
If the username and password match any tuple in database then return his/her objectid, username, password, role name and role id as a result using following statements:

   .. code-block:: sql

      statement = """select u.objectid, u.username, u.password, r.name, u.userroleid from usertable as u inner join userrole as r on u.userroleid=r.objectid where username=%s and password=%s"""

If it does not match any tuple in database then it returns None and in this case function assigns
 username and password that user wrote to username and password and empty string to the role

   .. code-block:: sql

      if row is not None:
                id, username, password, role, roleid=row
      else:
                id=0
                username=user
                password=passw
                role=''
                roleid=0

Finally it creates an User object according to values and returns it back.

After get_user function works we have a User object in our main login function. We decide whether it is successful or not accordng to role field of user object.
If there is role assigned to user then it is a valid user registered in our database.

   .. code-block:: python

      if result.role is '':
                error = 'Invalid Credentials. Please try again.'
      else:
                session['logged_in'] = True
                session['username'] = request.form['username'];
                if result.role == 'admin':
                    session['admin'] = True
                return redirect(url_for('home_page'))

If it is not a valid username or password then it gives an error else it assigns logged_in, username and admin session variables
according to user role.
When a user logged in then a session variable logged_in is assigned to True and session variable username is assigned to
his/her username.
If the role of user is admin then there is one more information holds in session is admin. It is also boolean variable as logged_in.
It determines the user admin or not.

**User Information Entity:**

Extra user information which is not used in login are kept userinformation table, name, surname, birthdate and favorite team etc.
Use information is designed to use in "my profile" and also "register operation", but we can not make the my profile page so it is just implemented in database but never used
in site part.

   .. code-block:: sql

      CREATE TABLE userinformation (
       objectid integer NOT NULL,
       favoriteteamid integer,
       name character varying,
       surname character varying,
       birthdate date,
       deleted integer DEFAULT 0 NOT NULL
      );

We are planned to keep name, surname, birthdate and favorite team of user, and these fields are planned to editable from profile page.

**Register:** There is one function in server.py, in main route, to handle login and register operations. In our scenario, when a user registers login_page
function is called and it controls the submit button name whether it is "login" or not. If it is not login then it is register operation.

   .. code-block:: python

      if request.form['submit']=='login':
            #login
      else:
            #register

Then it calls the add_user function that takes User object as a parameter.

   .. code-block:: python

      result=store.add_user(User(0,request.form['username_r'], request.form['password_r'],1,'',request.form['name'],request.form['surname'],request.form['birthdate']))

**add_user:** Add user function simply add new user object to the usertable and gives "user" as a default role. It should also add related information to the
userinformation but it is not implemented it juct insert into the usertable.
Takes User object as parameter and add it to the database and returns operation is successfull or not as a string value.

Insert Command in add_user:

   .. code-block:: python

      cursor.execute("""INSERT INTO usertable (username, password, userroleid) VALUES (%s, %s, 1)""",(User.username,User.password))


Result types of add_user:

   .. code-block:: python

      result = 'success'
      except dbapi2.IntegrityError:
            result = 'integrityerror'
            if connection:
                connection.rollback()
      except dbapi2.DatabaseError:
            result = 'databaseerror'

After add_use executes, if it returns success then session variables are set and user is redirected to the home page. Since user role is "user" in default
session['admin'] variable is not set this part.

   .. code-block:: python

      if result=='success':
                session['logged_in'] = True
                session['username'] = request.form['username_r'];
                return redirect(url_for('home_page'))

**Permissions:**

In our design only users that logged in can see the content of our site. When a user tries to go into the site writing urls is not allowed if it not logged in.
To handle this situation we used decorator. To use a decorator firstly import wraps into our project config.py.

   .. code-block:: python

      from functools import wraps

Decorators are design patterns and add new features to the classes or functions at run-time. "@" indicates the decorator.


`More information about decorator`_.

.. _More information about decorator: https://www.python.org/dev/peps/pep-0318/

   .. code-block:: python

      @login_required
      def home_page():

It is placed before the function definition.

We use decorator named "login_required" that checks whether a user logged in or not and it is allow to user to pass
requested page. For instance when a user wants to navvigate to teams page then login_required function controls the session variables.

   .. code-block:: python

      def login_required(test):
       @wraps(test)
       def wrap(*args, **kwargs):
           if 'logged_in' in session:
               return test(*args, **kwargs)
           else:
               flash('You need to login first.')
               return redirect(url_for('login_page'))
       return wrap

And also we use admin_required function that controls the user role if it is admin then it allows user go into the admin module

   .. code-block:: python

      if 'admin' in session and session['admin']==True:
            return test(*args, **kwargs)

It is same as login_required only the lines above is different. It is places in the admin module server.py file.