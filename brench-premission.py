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
for key in config ['repo']:
    array.extend([key])
    print(array)

users = config.get('users','alies')
print(users)
json_ = [
    {
        "id": 1,
        "type": "no-deletes",
        "matcher": {
            "id": config.get('branch','name'),
            "displayId": "master",
            "type": {
            "id": "BRANCH",
            "name": "Branch"
            },      
        "active": true
        },
        "users": users
        
    }]
json_patern =  [{
            "id": 2,
            "type": "read-only",
            "matcher": {
                "id": config.get('pattern','name'),
                "displayId": "/master**",
                "type": {
                    "id": "PATTERN",
                    "name": "Pattern"
                },
                "active": true
            },
            "users": users
        }
    ]
if config.has_option('',''):
    config

elif config.has_option('',''):
    config

elif config.has_option('',''):
    config


def full_url(repo) :
    url = website + '/rest/branch-permissions/2.0/projects/' + project + '/repos/'+ repo +'/restrictions'
    return url
    

for repo in array :
    url = full_url(repo)
    print(url)
    r = requests.post(url=url, json=json_, headers = headers)
    print(r.status_code)
    