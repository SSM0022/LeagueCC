import requests
import os
import urllib.parse
import json
import datetime


def check_latest_version():
    #  Set the file path for the version JSON file
    file_path = os.path.join(os.path.dirname(__file__), "version.json")

    # Load last_check_time from JSON file
    try:
        with open(file_path, "r") as f:
            last_check_time = datetime.datetime.fromisoformat(
                json.load(f)["last_check_time"]
            )
    except Exception as e:
        print(e)

    # Check if it has been more than a week since the last check
    current_time = datetime.datetime.now(datetime.timezone.utc)
    time_since_last_check = current_time - last_check_time
    if time_since_last_check >= datetime.timedelta(weeks=1):
        # Set the Riot API endpoint for retrieving the latest version
        endpoint = "https://ddragon.leagueoflegends.com/api/versions.json"
        
        # Send a GET request to the endpoint
        response = requests.get(endpoint)

        # If the request was successful, get the latest_version from the response
        if response.status_code == 200:
            version = response.json()[0]

        # Update last_check_time to be current_time
        check_time = current_time.isoformat()

        # Define dict to store new check_time & version
        last_checked = {"last_check_time": check_time, "latest_version": version}

        # Write the last_check_time & latest_version to version.json
        with open(file_path, "w") as f:
            json.dump(last_checked, f, indent=4)


def get_summonerID(name):
    name = urllib.parse.quote(name)
    url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={os.environ.get('API_KEY')}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["id"]
    else:
        print(f"{response.status_code} Error: API request unsuccessful")


def get_activegame(summoner_id):
    url = f"https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{summoner_id}?api_key={os.environ.get('API_KEY')}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["participants"]
    else:
        print(f"{response.status_code} Error: API request unsuccessful")


def get_champspells(champ_name):
    try:
        with open(os.path.join(os.path.dirname(__file__), "version.json"), "r") as f:
            version = json.load(f)["latest_version"]
    except FileNotFoundError:
        print("version.json file not found")
    url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion/{champ_name}.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["data"][champ_name]["spells"]
    else:
        print(f"{response.status_code} Error: API request unsuccessful")
