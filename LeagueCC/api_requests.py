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


