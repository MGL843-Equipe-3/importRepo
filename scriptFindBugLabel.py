############################################################################
## Script usage:                                                          ##
## python scriptFind Outputfile.json                                      ##
############################################################################
## Searchs for typescript repositories on github with more than 500 stars ##
## that uses de bug label for their issues                                ##
## (max 30)                                                               ##
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
outputFile = "repertoires.json"
keyLabel = "bug" # keyword you want present in at least 1 commit message
minOccurrence = 3 # minimum number of occurence of the keyword to consider that the repo uses it


# check if label exist
def checkLabel( owner, repoName, repoId, searchKeyword):
    
    try:
        verifQuery = f"{searchKeyword}&repository_id={repoId}"
        response2: requests.Response = requests.get(
            f"{BASE_URL}search/labels?q={verifQuery}&per_page=1",
            headers = {'Authorization': f'token {token}'}
        )

        resultVerif = json.loads(response2.content)

        totalCount = resultVerif["total_count"]

        #print(totalCount)

        if 1 <= totalCount:

            print(owner + "/" + repoName + " Valid! :)" + " Number of bug Labels: " + str(totalCount))
            return True
    except:
        print(owner + "/" + repoName + " Not Found!")
        return False

    print(owner + "/" + repoName + " Not Valid! No Match :(")
    return False

    #print(response2.content



# reading prog parameters
if len(sys.argv) == 2:
    outputFile = sys.argv[1]



# const and variables
BASE_URL = f"https://api.github.com/"

SEARCH_QUERY = "language:typescript+stars:>=500"

NUMBER_RES = 30

repertoires = []

# request
response: requests.Response = requests.get(
    f"{BASE_URL}search/repositories?q={SEARCH_QUERY}&sort=updated&per_page={NUMBER_RES}",
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

        if checkLabel(owner, nom, repo_id, keyLabel):

            repo = {"Name": nom, "Id": repo_id, "Url": repo_url, "Owner": owner, "Owner_id": owner_id}

            repertoires.append(repo)

#print(repertoires)
#print(outputFile)

# Json File creation
jsonRepertoires = {"repertoires_github": repertoires}

with open(outputFile, "w") as outfile:
    json.dump(jsonRepertoires, outfile)
