import random
import requests

def getrandomquote(header):
    response = requests.get("https://the-one-api.dev/v2/quote", headers=header)
    #response.status_code response code variable
    records = response.json()
    returnText = ""
    code = -1
    name = ""

    if response.ok:
        # Choose a random record
        random_record = random.choice(records.get('docs', []))
        returnText = random_record.get('dialog')
        name = getCharakterByID(random_record.get('character'), header)
        code = 1
    else:
        returnText = "No quote has been found"
        print("No records found.")
    
    return [code, returnText, name]

def getCharakterByID(id, header):
        response = requests.get("https://the-one-api.dev/v2/character?_id=" + id, headers=header)
        returnText = ""
        if response.ok:
                record = response.json()
                returnText = record.get('docs', [])[0].get('name')
        else:
                returnText = "No charakters has been found"
        return returnText