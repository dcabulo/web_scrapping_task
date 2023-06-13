import json
from pathlib import Path

import requests

from constants import *
from models.new_model import New


def get_content(news_type: str):
    response = requests.get(MAIN_URL.format(type_news=news_type))
    response.raise_for_status()
    return response.json()


def get_news_format(news_data: dict):
    news_list = news_data["payload"][0]["body"]["results"]
    return [New(title=item["title"], body=item["summary"]).to_dict() for item in news_list]


def save_json(data: dict):
    with open(JSON_FILE_PATH, 'w') as f:
        json.dump(data, f, indent=4)


def check_file_exist() -> bool:
    path = Path(JSON_FILE_PATH)
    return path.is_file()


def check_news_exist(base_list: dict, compare_list: dict, news_type: str):
    for new in base_list[news_type]:
        if new not in compare_list:
            base_list[news_type].update(new)
    return base_list
