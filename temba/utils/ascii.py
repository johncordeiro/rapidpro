__author__ = 'teehamaral'

import unidecode


def to_ascii(text):
    return unidecode.unidecode(text)
