import requests
import os

def get_summonerID(name):
    url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={os.environ.get('API_KEY')}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['id']
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

    
    

