############################################################################
## Script usage:                                                          ##
## python scriptFind number_of_repo Outputfile.json                       ##
############################################################################
## Searchs for typescript repositories on github with more than 500 stars ##
############################################################################


# imports
import json
from dotenv import load_dotenv
import os
import requests
import sys


# load token
load_dotenv('token.env')
token = os.getenv('GITHUB_TOKEN')


# Default values
numberRes = 10
outputFile = "repertoires.json"


# reading prog parameters
if len(sys.argv) == 2:
    numberRes = int(sys.argv[1])

if len(sys.argv) >= 3:
    numberRes = int(sys.argv[1])
    outputFile = sys.argv[2]


# const and variables
BASE_URL = f"https://api.github.com/"

SEARCH_QUERY = "language:typescript+stars:>=500"

repertoires = []

# request
response: requests.Response = requests.get(
    f"{BASE_URL}search/repositories?q={SEARCH_QUERY}&sort=updated&per_page={numberRes}",
    headers = {'Authorization': f'token {token}'}
)

# parsing 
if (response.status_code == 200):
    result = json.loads(response.content)

    result_tab = result["items"]

    for rep in result_tab:
        owner = rep["owner"]["login"]
        owner_id = rep["owner"]["id"]
        nom = rep["name"]
        repo_id = rep["id"]
        repo_url = rep["html_url"]

        repo = {"Name": nom, "Id": repo_id, "Url": repo_url, "Owner": owner, "Owner_id": owner_id}

        repertoires.append(repo)

#print(repertoires)
#print(outputFile)

# Json File creation
jsonRepertoires = {"repertoires_github": repertoires}

with open(outputFile, "w") as outfile:
    json.dump(jsonRepertoires, outfile)
