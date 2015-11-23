import os

VCAP_SERVICES = os.getenv('VCAP_SERVICES')
user="vagrant"
password="vagrant"
host="127.0.0.1"
port="54321"
dbname="itucsdb"
connection=None

if VCAP_SERVICES is not None:
    dsn = get_elephantsql_dsn(VCAP_SERVICES)
else:
    dsn = """user={0} password={1} host={2} port={3} dbname={4}""".format(user,password,host,port,dbname)
