'''
    `loader.py`
'''

from xml.dom import minidom

from src.utils import error

import os
import platform


DIR = 'data/'


def extract(file_name):
    try:
        if platform.system() == 'Windows':
            error('Auto-extract unsupported on Windows')
        else:
            os.system('unzip -o {}{}'.format(DIR, file_name))
    except (FileNotFoundError, OSError, PermissionError):
        pass


def fetch_file(file_format='gz', target=-1):
    try:
        return [i for i in os.listdir(DIR) if i[-len(file_format):] == file_format][target]
    except IndexError:
        return None

def get_document(file_name):
    return minidom.parse('{}{}'.format(DIR, file_name))


def get_score(document, include_unrated=False):
    items = document.getElementsByTagName('my_score')
    scores = [int(i.firstChild.data) for i in items if int(i.firstChild.data) > 0 or include_unrated]

    return scores
