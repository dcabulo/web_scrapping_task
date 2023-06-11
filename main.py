import json
import logging
from constants import *
from utils.helpers import save_json, get_news_format, get_content, check_file_exist, check_news_exist

logging.basicConfig(format=FORMAT, level=logging.INFO)


if __name__ == "__main__":
    if check_file_exist():
        logging.info("File news exist")
        exist_news = json.load(open(JSON_FILE_PATH))
        business_news = get_news_format(get_content(BUSINESS_TOKEN))
        tech_news = get_news_format(get_content(TECH_TOKEN))
        business_news_update = check_news_exist(exist_news, business_news, "business")
        tech_news_update = check_news_exist(exist_news, tech_news, "tech")
        if tech_news_update != exist_news:
            save_json(tech_news_update)
            logging.info("New News added succesfully")
        logging.info("No News added")
    else:
        logging.info("First time running getting all news")
        response_business = get_content(BUSINESS_TOKEN)
        business_news = get_news_format(response_business)
        response_tech = get_content(TECH_TOKEN)
        tech_news = get_news_format(response_tech)
        news_result = {"business": business_news, "tech": tech_news}
        save_json(news_result)
        logging.info("You got all the news in the right format")
