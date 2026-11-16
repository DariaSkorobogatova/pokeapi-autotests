import os

import pytest

from api.pokeapi_client import PokeApiClient

BASE_URL = os.getenv("POKEAPI_BASE_URL", "https://pokeapi.co/api/v2")


@pytest.fixture(scope="session")
def pokeapi() -> PokeApiClient:
    # scope="session" - клиент создаётся один раз на весь прогон тестов
    return PokeApiClient(BASE_URL)
