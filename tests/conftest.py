import pytest

from api.pokeapi_client import PokeApiClient
from config import BASE_URL


@pytest.fixture(scope="session")
def pokeapi() -> PokeApiClient:
    # scope="session" - клиент создаётся один раз на весь прогон тестов
    return PokeApiClient(BASE_URL)
