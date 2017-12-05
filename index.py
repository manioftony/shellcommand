import requests
from requests.auth import HTTPBasicAuth
import shutil
import os

# wget --user user --password pass http://example.com/

def urlmethod(url):
    response = requests.get(url,auth=HTTPBasicAuth('username', 'password'), stream=True)
    if response.status_code==200:
        img = os.path.basename(url)
        with open("a01-000u/"+img, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
    else:
        pass


data=["http://www.fki.inf.unibe.ch/DBs/iamDB/data/words/a01/a01-000u/a01-000u-0%i-0%i.png"%(i,j) for i in range(10) for j in range(10)]



[urlmethod(i) for i in data]

# [urlmethod("http://www.fki.inf.unibe.ch/DBs/iamDB/data/words/a01/a01-000u/a01-000u-00-0%i.png"%(i)) for i in range(10)]
# [urlmethod("http://www.fki.inf.unibe.ch/DBs/iamDB/data/words/a01/a01-000u/a01-000u-0%i-0%i.png"%(i,j) for i in range(10) for j in range(10))]

# urlmethod("http://www.fki.inf.unibe.ch/DBs/iamDB/data/words/a01/a01-000u/a01-000u-00-00.png")


