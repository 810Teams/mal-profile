'''
    script.py
'''

from xml.dom import minidom
from render import render_by_level
from statistics import average
from statistics import standard_dev
from statistics import median

import os

DIR = 'data/'


def main():
    ''' Main function '''
    file_name = [i for i in os.listdir(DIR) if i[-4::] == '.xml'][-1]

    document = minidom.parse(DIR + file_name)
    items = document.getElementsByTagName('my_score')
    scores = [int(i.firstChild.data) for i in items if int(i.firstChild.data) > 0]

    print()
    print('Average: {:.2f}'.format(average(scores)))
    print('Median: {:.0f}'.format(median(scores)))
    print('STD Dev: {:.2f}'.format(standard_dev(scores)))
    print()

    scores_sum = [scores.count(i) for i in range(1, 11)]
    render_by_level(scores_sum)

main()
