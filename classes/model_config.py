import datetime
import os
import json
import os
import re

user="vagrant"
password="vagrant"
host="127.0.0.1"
port="54321"
dbname="itucsdb"
connection=None
dsn=None

def get_elephantsql_dsn(vcap_services):
    """Returns the data source name for ElephantSQL."""
    parsed = json.loads(vcap_services)
    uri = parsed["elephantsql"][0]["credentials"]["uri"]
    match = re.match('postgres://(.*?):(.*?)@(.*?)(:(\d+))?/(.*)', uri)
    user, password, host, _, port, dbname = match.groups()
    dsn = """user='{}' password='{}' host='{}' port={}
             dbname='{}'""".format(user, password, host, port, dbname)
    return dsn

VCAP_SERVICES = os.getenv('VCAP_SERVICES')
if VCAP_SERVICES is not None:
    dsn=get_elephantsql_dsn(VCAP_SERVICES)
else:
    dsn="""user='vagrant' password='vagrant'
                               host='localhost' port=54321 dbname='itucsdb'"""
