import pytest
from LeagueCC.champions import find_champnames, find_ccspells
from LeagueCC.api_requests import get_champspells


def test_find_champnames():
    assert find_champnames(
        [
            {"championId": 120},
            {"championId": 497},
            {"championId": 18},
            {"championId": 84},
            {"championId": 85},
            {"championId": 29},
            {"championId": 110},
            {"championId": 56},
            {"championId": 79},
            {"championId": 45},
        ]
    ) == [
        "Hecarim",
        "Rakan",
        "Tristana",
        "Akali",
        "Kennen",
        "Twitch",
        "Varus",
        "Nocturne",
        "Gragas",
        "Veigar",
    ]


def test_find_ccspells():
    spell_list = [
        {
            "id": "LuxLightBinding",
            "description": "Lux releases a sphere of light that binds and deals damage to up to two enemy units.",
            "tooltip": "Lux fires a ball of light, <status>Rooting</status> the first two enemies",
        },
        {
            "id": "LuxPrismaticWave",
            "description": "Lux throws her wand and bends the light around any friendly target it touches, protecting them from enemy damage.",
            "tooltip": "Lux throws her wand, granting <shield>",
        },
        {
            "id": "LuxLightStrikeKugel",
            "description": "Fires an anomaly of twisted light to an area, which slows nearby enemies. Lux can detonate it to damage enemies in the area of effect.",
            "tooltip": "Lux creates a light zone that <status>Slows</status>",
        },
        {
            "id": "LuxR",
            "description": "After gathering energy, Lux fires a beam of light that deals damage to all targets in the area.",
            "tooltip": "Lux fires a dazzling ray of light, dealing <magicDamage>",
        },
    ]

    result = find_ccspells("Lux", spell_list)

    expected = {
        "Lux": {
            "LuxLightBinding": "Lux releases a sphere of light that binds and deals damage to up to two enemy units.",
            "LuxLightStrikeKugel": "Fires an anomaly of twisted light to an area, which slows nearby enemies. Lux can detonate it to damage enemies in the area of effect.",
        }
    }

    assert result == expected


def test_get_champspells():
    champ_name = "Ashe"

    result = get_champspells(champ_name)

    assert isinstance(result, list)
    assert len(result) == 4
    assert result[0]["id"] == "AsheQ"
    assert result[1]["id"] == "Volley"
    assert result[2]["id"] == "AsheSpiritOfTheHawk"
    assert result[3]["id"] == "EnchantedCrystalArrow"
