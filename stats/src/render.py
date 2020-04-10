'''
    render.py
'''

from math import ceil
from math import floor
from pygal.style import DarkStyle

import pygal


def render_by_score(data, file_name='untitled', max_y_labels=15, style=DarkStyle, title=''):
    ''' Function: Renders '''
    chart = pygal.HorizontalStackedBar()

    # Chart Data
    if isinstance(data, list):
        chart.add('Rated', [{'value': i, 'label': '{:.2f}%'.format(i / (sum(data) + (sum(data) == 0)) * 100)} for i in data])
    elif isinstance(data, dict):
        for i in data:
            chart.add(i, [{'value': j, 'label': '{:.2f}%'.format(j / (sum(data[i]) + (sum(data[i]) == 0)) * 100)} for j in data[i]])

    # Chart Titles
    chart.title = title

    # Chart Labels
    chart.x_labels = [i for i in range(1, 11, 1)]

    if isinstance(data, list):
        chart.y_labels = y_labels(0, max(data), max_y_labels=max_y_labels)
    elif isinstance(data, dict):
        data_r = [data[i] for i in data]
        data_r = [[data_r[j][i] for j in range(len(data_r))] for i in range(len(data_r[0]))]
        data_r = [sum(i) for i in data_r]
        chart.y_labels = y_labels(0, max(data_r), max_y_labels=max_y_labels)
    
    # Chart Legends
    if isinstance(data, list):
        chart.show_legend = False
    elif isinstance(data, dict):
        chart.show_legend = True
    chart.legend_at_bottom = False
    chart.legend_box_size = 15

    # Chart Render
    chart.style = style
    chart.render_to_file('charts/{}.svg'.format(file_name.replace('.svg', '')))


def y_labels(data_min, data_max, max_y_labels=15, skip=False):
    ''' Function: Calculates y labels of the chart '''
    data_min = floor(data_min)
    data_max = ceil(data_max)
    
    preset = 1, 2, 5
    i = 0
    
    if not skip:
        data_range = list(range(0, data_min - 1, -1)) + list(range(0, data_max + 1, 1))

        while len(data_range) > max_y_labels:
            data_range = list(range(0, data_min - preset[i % 3] * 10 ** (i // 3), -1 * preset[i % 3] * 10 ** (i // 3)))
            data_range += list(range(0, data_max + preset[i % 3] * 10 ** (i // 3), preset[i % 3] * 10 ** (i // 3)))
            i += 1
    else:
        data_min = int(data_min/10) * 10
        data_range = list(range(data_min, data_max + 1, 1))

        while len(data_range) > max_y_labels:
            data_range = list(range(data_min, data_max + preset[i % 3] * 10 ** (i // 3), preset[i % 3] * 10 ** (i // 3)))
            i += 1
        
    data_range.sort()

    return data_range
