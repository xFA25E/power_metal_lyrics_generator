#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This program is supposed to make power metal songs, titles and albums.

import generator
from sys import argv

keywords = {
    '--song': generator.generate_song,
    '--title': generator.generate_title,
    '--album': generator.generate_album
}


def print_usage():
    print("{} [ --title | --song | --album ]".format(argv[0]))
    exit()

if __name__ == '__main__':

    if (len(argv) != 2 or
        argv[1] not in keywords):
        print_usage()
    else:
        print("Your {} is generating.\n".format(argv[1][2:]))

    print(keywords[argv[1]]())
