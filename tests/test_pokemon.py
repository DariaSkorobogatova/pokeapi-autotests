"""Тесты эндпоинта /pokemon/{name_or_id}."""
import pytest


def test_get_pokemon_by_name_returns_200(pokeapi):
    response = pokeapi.get_pokemon("pikachu")

    assert response.status_code == 200


def test_get_pokemon_by_name_returns_correct_name(pokeapi):
    response = pokeapi.get_pokemon("pikachu")

    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "pikachu"
    assert body["id"] == 25


def test_get_pokemon_by_id_returns_correct_name(pokeapi):
    response = pokeapi.get_pokemon("25")

    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "pikachu"
    assert body["id"] == 25


def test_get_unknown_pokemon_returns_404(pokeapi):
    response = pokeapi.get_pokemon("definitely-not-a-pokemon")

    assert response.status_code == 404
    body = response.json()
    assert body["message"] == "Not Found"


@pytest.mark.parametrize("name, expected_id", [
    ('ditto', 132),
    ('eevee', 133),
    ('vaporeon', 134),
    ('flareon', 136),
    ('porygon', 137)
])
def test_get_pokemons_by_name_returns_correct_ids(pokeapi, name, expected_id):
    response = pokeapi.get_pokemon(name)

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == expected_id

