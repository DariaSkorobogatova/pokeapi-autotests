"""Тесты эндпоинта /pokemon/{name_or_id}."""
import pytest
from urllib.parse import urlparse, parse_qs
from config import MAX_RESPONSE_TIME_SECONDS


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


def test_get_pokemon_returns_json_content_type(pokeapi):
    response = pokeapi.get_pokemon("bulbasaur")

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")


def test_get_unknown_pokemon_returns_404(pokeapi):
    response = pokeapi.get_pokemon("definitely-not-a-pokemon")

    assert response.status_code == 404
    body = response.json()
    assert body["message"] == "Not Found"


@pytest.mark.parametrize("name, expected_id", [
    ("ditto", 132),
    ("eevee", 133),
    ("vaporeon", 134),
    ("flareon", 136),
    ("porygon", 137)
])
def test_get_pokemons_by_name_returns_correct_ids(pokeapi, name, expected_id):
    response = pokeapi.get_pokemon(name)

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == expected_id


def test_time_to_first_byte_get_pokemon_by_name(pokeapi):
    response = pokeapi.get_pokemon("mew")

    assert response.status_code == 200
    elapsed = response.elapsed.total_seconds()
    assert elapsed < MAX_RESPONSE_TIME_SECONDS, (
        f"Ответ занял {elapsed:.2f} сек., допустимо до {MAX_RESPONSE_TIME_SECONDS} сек."
    )


@pytest.mark.parametrize("name, expected_type", [
    ("pikachu", "electric"),
    ("bulbasaur", "grass"),
    ("charmander", "fire")
])
def test_get_pokemon_type_by_name(pokeapi, name, expected_type):
    response = pokeapi.get_pokemon(name)

    assert response.status_code == 200
    body = response.json()
    # перебираем все типы на случай, если их у покемона несколько
    type_names = [item["type"]["name"] for item in body["types"]]
    assert expected_type in type_names


@pytest.mark.parametrize("wrong_id", [0, -1, 5000, 99_999])
def test_get_pokemon_by_invalid_id_returns_404(pokeapi, wrong_id):
    response = pokeapi.get_pokemon(wrong_id)

    assert response.status_code == 404
    assert response.json()["message"] == "Not Found"


def test_get_pokemon_list_returns_requested_number_of_results(pokeapi):
    limit = 5

    response = pokeapi.get_pokemon_list(limit=limit, offset=0)

    assert response.status_code == 200
    body = response.json()
    assert len(body["results"]) == limit


def test_get_pokemon_list_without_params_returns_default_number_of_results(pokeapi):
    expected_default_limit = 20

    response = pokeapi.get_pokemon_list()

    assert response.status_code == 200
    body = response.json()
    assert len(body["results"]) == expected_default_limit


def test_get_pokemon_list_offset_shifts_results(pokeapi):
    shift = 3

    full_response = pokeapi.get_pokemon_list(limit=10, offset=0)
    shifted_response = pokeapi.get_pokemon_list(limit=10, offset=shift)

    assert full_response.status_code == 200
    assert shifted_response.status_code == 200
    full_list = full_response.json()["results"]
    shifted_list = shifted_response.json()["results"]
    assert shifted_list[0] == full_list[shift]


def test_get_pokemon_list_offset_24th_pokemon_is_pikachu(pokeapi):
    shift = 24

    response = pokeapi.get_pokemon_list(limit=1, offset=shift)

    assert response.status_code == 200
    body = response.json()
    assert body["results"][0]["name"] == "pikachu"


def test_get_pokemon_list_first_page_has_no_previous(pokeapi):
    offset = 0

    response = pokeapi.get_pokemon_list(offset=offset)

    assert response.status_code == 200
    assert response.json()["previous"] is None


def test_get_pokemon_list_next_points_to_following_page(pokeapi):
    limit = 5
    offset = 10

    response = pokeapi.get_pokemon_list(limit=limit, offset=offset)

    assert response.status_code == 200
    next_url: str = response.json()["next"]
    # parse_qs превращает query-параметры в словарь: {"offset": ["15"], "limit": ["5"]}
    next_params = parse_qs(urlparse(next_url).query)
    # значения приходят строками и в списках, поэтому сравниваем со списком из строки
    assert next_params["offset"] == [str(offset + limit)]
    assert next_params["limit"] == [str(limit)]








