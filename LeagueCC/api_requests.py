import requests
import os
import urllib.parse
import json
import datetime


def check_latest_version():
    """
    Checks whether the current version of the League of Legends client is up to date.

    Reads the last check time from a JSON file and compares it to the current time to see if it has been more than a week since the last check.
    If it has been more than a week, sends a GET request to the Riot API to retrieve the latest version of the client.
    If the request is successful, updates the last check time and the latest version in the JSON file.

    Returns:
    None

    Raises:
    Any exceptions that occur while reading from or writing to the JSON file.
    """

    file_path = os.path.join(os.path.dirname(__file__), "version.json")

    # last_check_time is stored in the version.json because program is not always running
    try:
        with open(file_path, "r") as f:
            last_check_time = datetime.datetime.fromisoformat(
                json.load(f)["last_check_time"]
            )
    except Exception as e:
        print(e)

    # League of Legends updates every two weeks but we check once a week for version updates incase of hotfix
    current_time = datetime.datetime.now(datetime.timezone.utc)
    time_since_last_check = current_time - last_check_time
    if time_since_last_check >= datetime.timedelta(weeks=1):
        endpoint = "https://ddragon.leagueoflegends.com/api/versions.json"

        response = requests.get(endpoint)

        if response.status_code == 200:
            version = response.json()[0]

        check_time = current_time.isoformat()

        # Storing the minimal data neccesary to keep our program up to date with League of Legends version
        last_checked = {"last_check_time": check_time, "latest_version": version}

        with open(file_path, "w") as f:
            json.dump(last_checked, f, indent=4)


def get_summonerID(name):
    """
    Retrieves the Summoner ID for a given Summoner name from the Riot Games API.

    Encodes the given Summoner name and constructs a URL to retrieve the Summoner ID from the Riot Games API.
    Sends a GET request to the constructed URL and checks whether the response is successful.
    If the response is successful, returns the Summoner ID.
    If the response is not successful, prints an error message to the console.

    Args:
    name (str): The name of the Summoner whose ID is being retrieved.

    Returns:
    str: The Summoner ID of the specified Summoner.

    Raises:
    Any exceptions that occur while sending the GET request or parsing the JSON response.
    """

    # Encode the summoner name to be URL-safe - neccesary for names with spaces and other special chars
    name = urllib.parse.quote(name)

    url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={os.environ.get('API_KEY')}"

    response = requests.get(url)

    # summoner ID is the only data extracted because it is required for active game look-up
    if response.status_code == 200:
        data = response.json()
        return data["id"]
    else:
        print(f"{response.status_code} Error: API request unsuccessful")


def get_activegame(summoner_id):
    """
    Retrieves the current active game for a given Summoner ID from the Riot Games API.

    Constructs a URL to retrieve the active game data for the given Summoner ID from the Riot Games API.
    Sends a GET request to the constructed URL and checks whether the response is successful.
    If the response is successful, returns the participant data for the active game.
    If the response is not successful, prints an error message to the console.

    Args:
    summoner_id (str): The Summoner ID of the Summoner whose active game data is being retrieved.

    Returns:
    dict: The participant data for the active game, which includes information about each player in the game.

    Raises:
    Any exceptions that occur while sending the GET request or parsing the JSON response.
    """

    url = f"https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{summoner_id}?api_key={os.environ.get('API_KEY')}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # the participants dict contains extensive data about each player in the active game
        return data["participants"]
    else:
        print(f"{response.status_code} Error: API request unsuccessful")


def get_champspells(champ_name):
    """
    Retrieves the abilities (spells) of a specified champion.

    Reads the latest version number from a local JSON file and constructs a URL to request champion data for the
    specified champion from the Riot Games Data Dragon API. Sends an HTTP GET request to the URL and extracts the
    ability data from the response. Returns a list of dictionaries, with each dictionary representing one ability.

    Args:
    champ_name (str): The name of the champion to retrieve ability data for.

    Returns:
    list: A list of dictionaries, with each dictionary representing an ability of the specified champion.

    Raises:
    None.
    """
    # with the version number we can get the latest version of champion abilities
    try:
        with open(os.path.join(os.path.dirname(__file__), "version.json"), "r") as f:
            version = json.load(f)["latest_version"]
    except FileNotFoundError:
        print("version.json file not found")
    url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion/{champ_name}.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # all champions have 4 abilities/spells each
        return data["data"][champ_name]["spells"]
    else:
        print(f"{response.status_code} Error: API request unsuccessful")
