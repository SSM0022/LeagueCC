from api_requests import get_summonerID, get_activegame
from champions import get_champIDs

def main():
    sum_id = get_summonerID(input("Name: "))
    participants = get_activegame(sum_id)
    print(get_champIDs(participants))

if __name__ == "__main__":
    main()
  