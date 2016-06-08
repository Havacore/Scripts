import requests
import os
import sys
import getopt
from bs4 import BeautifulSoup


NETRUNNER_DB_LINK="http://netrunnerdb.com/"
NETRUNNER_DB_CARD_SEARCH_LINK="en/search"
DRAFT_LINK="http://netrunnerdb.com/en/set/draft"


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hd:a", ["help", "deck=", "all"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-d", "--deck"):
            build_deck(arg)
        elif opt in ("-a", "--all"):
            download_all_cards(arg)


def usage():
    print """
    usages:
    -h: help
    -d --deck: the link to a deck on http://netrunnerdb.com
    -a --all: download all netrunner cards
    """


def build_deck(opt):
    print "Gathering cards for deck: {}".format(opt.split('/')[-1])


def download_all_cards(arg):
    print "downloading all cards..."

    request = requests.get(NETRUNNER_DB_LINK + NETRUNNER_DB_CARD_SEARCH_LINK)
    soup = BeautifulSoup(request.content)
    set_tags = soup.find("div", "col-md-4")
    set_tags = set_tags.find_all("a")
    for set in set_tags:
        set_name = set['href'].split('/')[-1]
        if set_name != "draft":
            if set['href'].split('/')[-2] == "set":
                download_set(set_name, set)


def download_set(set_name, set):
    print set

if __name__ == "__main__":
    main(sys.argv[1:])