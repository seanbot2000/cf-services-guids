from getpass import getpass
import cf_api
import json
import os 

cloud_controller = os.environ['CF_API']
client_id='cf'
client_secret=''
verify_ssl = True
username = os.environ['CF_USER']
password = os.environ['CF_SECRET']

cc = cf_api.new_cloud_controller(
    cloud_controller,
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
).set_verify_ssl(verify_ssl)
    
    
# List all organizations
req = cc.organizations()
res = req.get()
orgs = res.resources
print('org', 'guid', sep=',')
for r in orgs:
    print(r.name, r.guid, sep=',')
    
    
# List all spaces
res = cc.spaces().get()
spaces = res.resources
print('space', 'guid', sep=',')
for r in spaces:
    print(r.name, r.guid, sep=',')


# List all services
res = cc.services().get()
services = res.resources
print('service', 'guid', sep=',')
for s in services:
    print(s.label,s.guid, sep=',')