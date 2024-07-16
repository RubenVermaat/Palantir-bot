import random
import requests
import json
import os

header = {'Accept': 'application/json','Authorization': os.getenv('LOTR_API')}

# Automaticly loading in all the .json files in the following directory
# On server use directory_path = "/home/USERNAME/Palantir-bot/data/json"
directory_path = "./data/json"
# Create a dictionary to store JSON data with file names as keys
json_data = {}
# Loop through each file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".json"):
        file_path = os.path.join(directory_path, filename)

        # Read JSON content from the file
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        # Store the JSON data in the dictionary with the file name as the key
        json_data[filename] = data


def getRandomQuote():
    result = Result()
    response = requests.get("https://the-one-api.dev/v2/quote", headers=header)
    #response.status_code response code variable

    if response.ok:
        # Choose a random record
        records = response.json()
        random_record = random.choice(records.get('docs', []))
        result.data = random_record.get('dialog')
        result.name = getCharakterNameByID(random_record.get('character'))
    else:
        result.data = "No quote has been found"
        result.error = 1
    
    return result

def getJsonCharakters():
    response = requests.get("https://the-one-api.dev/v2/character", headers=header)
    result = Result()
    if response.ok:
        result.data = response.json()
    else:
        result.error = 1
        result.data = "Something went wrong collecting all the characters"
    return result

def getCharakterNameByID(id):
        response = requests.get("https://the-one-api.dev/v2/character?_id=" + id, headers=header)
        name = ""
        if response.ok:
                record = response.json()
                name = record.get('docs', [])[0].get('name')
        else:
                name = "Unknown"
        return name

def getRandomCountry():
    result = Result()
    country = getRandomItem(json_data['countries.json'])
    if country != "error":
        result.data = country
    else:
        result.error = 1
        result.data = "Something went wrong picked out a random country"
    return result

def getCountry(name):
    result = Result()
    country = [country for country in json_data['countries.json'] if country['name'].lower() == name.lower()]
    if len(country) > 0:
        result.data = country[0]
    else:
        result.error = 1
        result.data = "Something went wrong getting the country " + name
    return result


def getCountryByCode(code):
    result = Result()
    country = [country for country in json_data['countries.json'] if country['country_id'].lower() == code.lower()]
    if len(country) > 0:
        result.data = country[0]
    else:
        result.error = 1
        result.data = "Something went wrong getting the country " + code
    return result

def GetAllCountries():
    result = Result()
    if json_data['countries.json'] != None:
        result.data = json_data['countries.json']
    else:
        result.error = 1
        result.data = "Something went wrong getting the country"
    return result

def getRandomItem(data):
    if len(data) > 0:
        random_record = random.choice(data)
        return random_record
    else:
        return "error"
    
def selectRandomTypeQoute(self, type):
    result = Result()
    type_records = [quote for quote in json_data['responses.json'] if quote['type'].lower() == type.lower()]
    if len(type_records) > 0:
        random_record = getRandomItem(type_records)
        if random_record != "error":
            result.data = random_record.get('dialog')
        else:
            result.error = 1
            result.data = "Something went wrong selecting a random quote"
    else:
        result.error = 1
        result.data = "Something went wrong getting all the quotes"
    return result

def selectAchievementByName(self, name):
    result = Result()
    achievements = [achievement for achievement in json_data['achievements.json'] if name.lower() in achievement['name'].lower()]
    if len(achievements) > 0:
        selected_record = achievements[0]
        if selected_record != "error":
            result.data = selected_record
        else:
            result.error = 1
            result.data = "Something went wrong finding the achievement"
    else:
        result.error = 1
        result.data = "Something went wrong finding the achievement"
    return result

def selectRandomAchievement(self):
    result = Result()
    if len(json_data['achievements.json']) > 0:
        selected_record = random.choice(json_data['achievements.json'])
        if selected_record != "error":
            result.data = selected_record
        else:
            result.error = 1
            result.data = "Something went wrong finding the achievement"
    else:
        result.error = 1
        result.data = "Something went wrong finding the achievement"
    return result

class Result:
     def __init__(self):
          self.error = -1
          self.data = ""
          self.name = ""