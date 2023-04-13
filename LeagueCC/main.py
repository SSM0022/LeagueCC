from api_requests import get_summonerID, get_activegame, get_champjson
from champions import get_champnames


def main():
    sum_id = get_summonerID(input("Name: "))
    champ_list = (get_champnames(get_activegame(sum_id)))
    get_champjson(champ_list[0])


if __name__ == "__main__":
    main()
