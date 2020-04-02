import json
from os.path import dirname, exists

import pytest


@pytest.fixture
def schema_loader():
    def loader(schema_name):
        schema = f"schemas/{schema_name}.json"
        if not exists(schema):
            raise Exception(f"Schema don't exists in {dirname(__file__)}")
        with open(schema) as json_file:
            return json.loads(json_file.read())

    return loader
