import requests
import urllib
import os
from bs4 import BeautifulSoup

THRONES_DB_LINK = "http://thronesdb.com"
THRONES_CORE_LINK = "/set/core"
THRONES_WESTEROS_CYCLE_LINK = "/cycle/westeros"
THRONES_IMAGE_LINK_PREFIX = THRONES_DB_LINK + "/bundles/cards/"

CORE_SET_PATH = "./core_set"

WESTEROS_CYCLE_PATH = "./westeros_cycle/"
TAKING_THE_BLACK_PATH = "taking_the_black/"


def main():

    scrape_core_set()
    scrape_westeros_cycle()


def scrape_core_set():

    path = CORE_SET_PATH

    try:
        os.makedirs(path)
    except OSError as e:
        print e.message

    request = requests.get(THRONES_DB_LINK + THRONES_CORE_LINK)
    content = request.content
    soup = BeautifulSoup(content)

    card_tags = soup.find_all("a", "card-tip")
    file_list = os.listdir(path)

    for card in card_tags:

        data_code = card['data-code']
        card_name = card.text.replace(" ", "_").replace("\"", "")

        image_link = THRONES_IMAGE_LINK_PREFIX + data_code + ".png"
        file_name = data_code + "_" + card_name + ".png"

        if file_name in file_list:
            continue

        urllib.urlretrieve(image_link, CORE_SET_PATH + data_code + "_" + card_name + ".png")


def scrape_westeros_cycle():

    try:
        os.makedirs(WESTEROS_CYCLE_PATH)
    except OSError as e:
        print e.message

    scrape_taking_the_black()


def scrape_taking_the_black():

    path = WESTEROS_CYCLE_PATH + TAKING_THE_BLACK_PATH

    try:
        os.makedirs(path)
    except OSError as e:
        print e.message

    request = requests.get(THRONES_DB_LINK + THRONES_WESTEROS_CYCLE_LINK)
    content = request.content
    soup = BeautifulSoup(content)

    card_tags = soup.find_all("a", "card-tip")
    file_list = os.listdir(path)

    for card in card_tags:
        pass

        data_code = card['data-code']
        card_name = card.text.replace(" ", "_").replace("\"", "")

        image_link = THRONES_IMAGE_LINK_PREFIX + data_code + ".png"
        file_name = data_code + "_" + card_name + ".png"

        if file_name in file_list:
            continue

        urllib.urlretrieve(image_link, WESTEROS_CYCLE_PATH + TAKING_THE_BLACK_PATH + data_code + "_" + card_name + ".png")

if __name__ == "__main__": main()