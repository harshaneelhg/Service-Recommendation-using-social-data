'''
Created on 17-Mar-2015

@author: Harshaneel Gokhale
'''

import json
import urllib


def get_categories(mid):
    
    """
        Input: List of MIDs.
        Output: List of UNIQUE topics corresponding
            MIDs fall into.
        This function fires read query on freebase
        to identify root categories for particular
        mid (MAchine ID for every topic).
    """
    
    read_url = 'https://www.googleapis.com/freebase/v1/mqlread'
    read_query = 'query=[{"mid":"'+ mid +'","type":[]}]'
    url = read_url + '?' + read_query
    response = json.loads(urllib.urlopen(url).read())
    cat=[]
    if 'result' in response:
        for item in response['result']:
            if 'type' in item:
                for thing in item['type']:
                    words=thing.split('/')
                    if not (str(words[1]) == 'common' or str(words[1]) == 'base'):
                        cat.append(str(words[1]))
    return cat

def print_categories(search):
    
    """
        Input: Search keyword.
        Output: Prints list of UNIQUE Topics that
            keyword possibly falls into.
        This function queries using search API of freebase,
        selects MIDs of top five topics that query word falls
        into and calls get_categories() function to get
        list of UNIQUE topics.
    """
    
    key= open('api_key.txt','r')
    api_key = key.readline()
    query = search
    service_url = 'https://www.googleapis.com/freebase/v1/search'
    params = {
              'query': query,
              'key': api_key
              }
    url = service_url + '?' + urllib.urlencode(params)
    response = json.loads(urllib.urlopen(url).read())
    mid = []
    count = 0
    for result in response['result']:
        if count > 4:
            break
        #print( result['name'] +' (' + str(result['score']) + ')'+' (' + str(result['mid']) + ')')
        mid.append(str(result['mid']))
        count += 1
        #if 'notable' in result:
        #    print(' [' + result['notable']['name'] + '] '+' [' + result['notable']['id'] + '] ')


    categories=[]

    for val in mid:
        cat = get_categories(val)
        for c in cat:
            if not (c in categories):
                categories.append(c)

<<<<<<< HEAD
    print (categories)
=======
api_key = 'your_api_key'
query = 'state farm'
service_url = 'https://www.googleapis.com/freebase/v1/search'
params = {
        'query': query,
        'key': api_key
}
url = service_url + '?' + urllib.urlencode(params)
response = json.loads(urllib.urlopen(url).read())
mid = []
count = 0
for result in response['result']:
    if count > 4:
        break
    #print( result['name'] +' (' + str(result['score']) + ')'+' (' + str(result['mid']) + ')')
    mid.append(str(result['mid']))
    count += 1
    #if 'notable' in result:
    #    print(' [' + result['notable']['name'] + '] '+' [' + result['notable']['id'] + '] ')


categories=[]

for val in mid:
    cat = get_categories(val)
    for c in cat:
        if not (c in categories):
            categories.append(c)

print (categories)
>>>>>>> origin/master
    
print_categories('state farm')
