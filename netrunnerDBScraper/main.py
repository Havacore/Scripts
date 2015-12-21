import requests
import os
import sys
import getopt


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hd:", ["help", "deck="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-d", "--deck"):
            build_deck(arg)


def usage():
    print """
    usages:
    -h: help
    -d --deck: the link to a deck on http://netrunnerdb.com
    """


def build_deck(opt):
    print "Gathering cards for deck: {}".format(opt.split('/')[-1])


if __name__ == "__main__":
    main(sys.argv[1:])