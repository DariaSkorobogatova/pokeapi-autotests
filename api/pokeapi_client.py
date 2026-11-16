"""Клиент для PokeAPI (https://pokeapi.co/docs/v2)"""


import requests

from api.base_client import BaseClient


class PokeApiClient(BaseClient):
    def get_pokemon(self, name_or_id: str | int) -> requests.Response:
        return self.get(f"/pokemon/{name_or_id}")
