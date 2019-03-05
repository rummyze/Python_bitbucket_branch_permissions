import sys
import requests
import logging
import urllib3
from requests_oauthlib import OAuth1
import configparser
from configparser import ConfigParser

# instantiate
config = ConfigParser()

# parse existing file
config.read('./conf.ini')
# read values from a section
true = 'true'

access_token = config.get('token' ,'id')
headers = {
    'Content-type': 'application/vnd.atl.bitbucket.bulk+json',
    'Authorization': 'Bearer {}'.format(access_token)
}
website = config.get('website','link')
project = config.get('project','name')
array = []
users = config.get('users','alias').split(",")
print(users)

for key in config ['repo']:
    array.extend([key])
    print(array)

def full_url(repo) :
    url = website + '/rest/branch-permissions/2.0/projects/' + project + '/repos/'+ repo +'/restrictions'
    return url
    
def json(type_name,branch,type_id):
    json = [{
        "id": 1,
        "type": type_name,
        "matcher": {
            "id": branch,
            "displayId": branch,
            "type": {
            "id": type_id.upper(),
            "name": type_id.capitalize()
            },      
        "active": true
        },
        "users": users
        }]
    print (json)
    return json

def kakto (type):
    r = requests.post(url=url, json=json(type_name='read-only',branch=config.get(type,'name'),type_id=type) , headers = headers)
    print(r.status_code)
    print(r.content )

for repo in array :
    url = full_url(repo)
    print(url)
    if config.has_section('pattern'):
        kakto('pattern')
    if config.has_section('branch'):
        kakto('branch')