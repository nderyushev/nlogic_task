import json

import click
from loguru import logger


def order_dict(data):
    if isinstance(data, dict):
        return sorted((k, order_dict(v)) for k, v in data.items())
    if isinstance(data, list):
        return sorted(order_dict(x) for x in data)
    if isinstance(data, float):
        return round(data, 5)
    return data


@click.command()
@click.argument("first_path")
@click.argument("second_path")
def start(first_path: str, second_path: str):
    with open(first_path) as f:
        first_json = json.loads(f.read())

    with open(second_path) as f:
        second_json = json.loads(f.read())

    is_equals = order_dict(first_json) == order_dict(second_json)

    logger.debug("Равны" if is_equals else "Не равны")


if __name__ == "__main__":
    start()
