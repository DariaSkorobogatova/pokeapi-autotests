# PokeAPI Autotests

![API tests](../../actions/workflows/tests.yml/badge.svg)

Учебный проект: автотесты бэкенда на Python для публичного [PokeAPI](https://pokeapi.co/).

## Стек
- Python 3.10+
- pytest - тестовый фреймворк
- requests - HTTP-запросы
- GitHub Actions - тесты запускаются при каждом push

## Структура
```
api/            # клиенты API: как отправлять запросы
  base_client.py
  pokeapi_client.py
tests/          # сами тесты: что проверяем
  conftest.py   # фикстуры
  test_pokemon.py
```

## Запуск
```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest
```
