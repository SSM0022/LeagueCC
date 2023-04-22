from api_requests import (
    get_summonerID,
    get_activegame,
    get_champspells,
    check_latest_version,
)
from champions import find_champnames, find_ccspells


def main():
    """
    The main function is the entry point of the program that executes several functions to retrieve information about a League of Legends game.

    The function executes the following steps:

    1. Check the latest version of the game.
    2. Get the summoner ID of a player by name.
    3. Retrieve the active game information for the given summoner ID.
    4. Find the champion names for all players in the active game.
    5. For each champion in the active game:
        a. Retrieve the champion's spells.
        b. Find any crowd control (CC) spells in the champion's spell list.
        c. Print the champion name and the CC spells with their descriptions.

    The function does not take any arguments.

    Returns: None.
    """

    check_latest_version()
    sum_id = get_summonerID(input("Name: "))
    champ_names = find_champnames(get_activegame(sum_id))
    for champ in champ_names:
        spells = get_champspells(champ)
        print(find_ccspells(champ, spells))


if __name__ == "__main__":
    main()
