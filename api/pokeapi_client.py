"""Клиент для PokeAPI (https://pokeapi.co/docs/v2)"""


import requests

from api.base_client import BaseClient


class PokeApiClient(BaseClient):
    def get_pokemon(self, name_or_id: str | int) -> requests.Response:
        return self.get(f"/pokemon/{name_or_id}")

# Добавили None для возможности отправки метода без параметров
    def get_pokemon_list(self, limit: int | None = None, offset: int | None = None) -> requests.Response:
        return self.get("/pokemon/", params={"limit": limit, "offset": offset})


