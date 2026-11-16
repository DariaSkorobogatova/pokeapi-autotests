"""Базовый HTTP-клиент: общая логика для API"""

import requests


class BaseClient:
    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        # Session переиспользует соединение, поэтому тесты работают быстрее
        self.session = requests.Session()

    def get(self, path: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self.session.get(url, timeout=self.timeout, **kwargs)
