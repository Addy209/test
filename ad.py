import json
from ldap3 import Server, Connection, ALL
from pyad import *

LDAP_URL = 'ldap://ldap.forumsys.com:389'

pyad.set_defaults(ldap_server=LDAP_URL,username="riemann",password="password")
user1 = pyad.aduser.ADUser.from_dn("cn=newton, ou=scientists, dc=example, dc=com")
print(pyad)
