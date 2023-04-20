from api_requests import get_summonerID, get_activegame, get_champspells, check_latest_version
from champions import find_champnames, find_ccspells


def main():
    check_latest_version()
    sum_id = get_summonerID(input("Name: "))
    champ_names = find_champnames(get_activegame(sum_id))
    for champ in champ_names:
        spells = get_champspells(champ)
        print(find_ccspells(champ, spells))


if __name__ == "__main__":
    main()
