'''
    script.py
'''

from xml.dom import minidom

from src.loader import extract
from src.loader import fetch_file
from src.loader import get_document
from src.loader import get_score
from src.render import render_by_level
from src.statistics import average
from src.statistics import standard_dev
from src.statistics import median
from src.utils import notice
from src.utils import error

import os
import platform


DIR = 'data/'


def main():
    ''' Main function '''
    extract(fetch_file(file_format='gz'))
    scores = get_score(get_document(fetch_file(file_format='xml')))

    print()
    print('Average: {:.2f}'.format(average(scores)))
    print('Median: {:.0f}'.format(median(scores)))
    print('STD Dev: {:.2f}'.format(standard_dev(scores)))
    print()

    scores_sum = [scores.count(i) for i in range(1, 11)]
    render_by_level(scores_sum)

    try:
        if platform.system() == 'Windows':
            pass
        else:
            os.system('open charts/*')
            notice('Opening chart files.')
    except (FileNotFoundError, OSError, PermissionError):
        error('Something unexpected happened, please try again.')

main()