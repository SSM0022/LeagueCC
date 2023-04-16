from api_requests import get_summonerID, get_activegame, get_champspells
from champions import find_champnames, find_cc


def main():
    sum_id = get_summonerID(input("Name: "))
    champ_list = (find_champnames(get_activegame(sum_id))) 
    spells = get_champspells(champ_list[0])
    print(find_cc(champ_list[0], spells))


if __name__ == "__main__":
    main()
