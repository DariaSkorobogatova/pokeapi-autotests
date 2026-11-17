"""Тесты эндпоинта /pokemon/{name_or_id}."""


def test_get_pokemon_by_name_returns_200(pokeapi):
    response = pokeapi.get_pokemon("pikachu")

    assert response.status_code == 200


def test_get_pokemon_by_name_returns_correct_name(pokeapi):
    response = pokeapi.get_pokemon("pikachu")
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
