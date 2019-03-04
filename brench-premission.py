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
users = config.get('users','alies')
print(users)

for key in config ['repo']:
    array.extend([key])
    print(array)

def full_url(repo) :
    url = website + '/rest/branch-permissions/2.0/projects/' + project + '/repos/'+ repo +'/restrictions'
    return url
    

def json(users,brench,desplayId,type):
    json = [
    {
        "id": 1,
        "type": type,
        "matcher": {
            "id": config.get(brench,'name'),
            "displayId": desplayId,
            "type": {
            "id": "BRANCH",
            "name": "Branch"
            },      
        "active": true
        },
        "users": users
        
    }]
    
if config.has_section('branch') & config.has_section('pattern'):
    for repo in array :
        url = full_url(repo)
        print(url)
        r = requests.post(url=url, json=json , headers = headers)
        print(r.status_code)

elif config.has_section('pattern'):
    for repo in array :
        url = full_url(repo)
        print(url)
        r = requests.post(url=url, json=json , headers = headers)
        print(r.status_code)

elif config.has_section('branch'):
    for repo in array :
        url = full_url(repo)
        print(url)
        r = requests.post(url=url, json=json() , headers = headers)
        print(r.status_code)