'''
    render.py
'''

from math import ceil
from math import floor
from pygal.style import DefaultStyle

from src.utils import notice

import pygal


class RenderMachine:
    def __init__(
        self,
        legend_at_bottom=False,
        legend_box_size=15,
        max_y_labels=15,
        style=DefaultStyle,
        y_labels_preset=(1, 2, 5),
        y_labels_skip=False
    ):
        self.legend_at_bottom = legend_at_bottom
        self.legend_box_size = legend_box_size
        self.max_y_labels = max_y_labels
        self.style = style
        self.y_labels_preset = y_labels_preset
        self.y_labels_skip = y_labels_skip

    def render_by_score(self, data, file_name='untitled_chart', title=''):
        ''' Function: Renders '''
        chart = pygal.HorizontalStackedBar()

        # Chart Data
        if isinstance(data, list):
            chart.add('Rated', [{'value': i, 'label': '{}/{} ({:.2f}%)'.format(i, sum(data), i / (sum(data) + (sum(data) == 0)) * 100)} for i in data])
        elif isinstance(data, dict):
            for i in data:
                chart.add(i, [{'value': j, 'label': '{}/{} ({:.2f}%)'.format(j, sum(data[i]), j / (sum(data[i]) + (sum(data[i]) == 0)) * 100)} for j in data[i]])

        # Chart Titles
        chart.title = title

        # Chart Labels
        if isinstance(data, list):
            chart.x_labels = [i for i in range(1 - (len(data) == 11), 11, 1)]
            chart.y_labels = self.get_y_labels(0, max(data))
        elif isinstance(data, dict):
            chart.x_labels = [i for i in range(1 - (len(data[[j for j in data][0]]) == 11), 11, 1)]
            data_r = [data[i] for i in data]
            data_r = [[data_r[j][i] for j in range(len(data_r))] for i in range(len(data_r[0]))]
            data_r = [sum(i) for i in data_r]
            chart.y_labels = self.get_y_labels(0, max(data_r))
        
        # Chart Legends
        chart.show_legend = isinstance(data, dict)
        chart.legend_at_bottom = self.legend_at_bottom
        chart.legend_box_size = self.legend_box_size

        # Chart Render
        chart.style = self.style
        chart.render_to_file('charts/{}.svg'.format(file_name.replace('.svg', '')))

        # Notice
        notice('Chart \'{}\' successfully exported.'.format(file_name))


    def get_y_labels(self, data_min, data_max):
        ''' Function: Calculates y labels of the chart '''
        data_min = floor(data_min)
        data_max = ceil(data_max)
        
        preset = self.y_labels_preset
        i = 0
        
        if not self.y_labels_skip:
            data_range = list(range(0, data_min - 1, -1)) + list(range(0, data_max + 1, 1))

            while len(data_range) > self.max_y_labels:
                data_range = list(range(0, data_min - preset[i % 3] * 10 ** (i // 3), -1 * preset[i % 3] * 10 ** (i // 3)))
                data_range += list(range(0, data_max + preset[i % 3] * 10 ** (i // 3), preset[i % 3] * 10 ** (i // 3)))
                i += 1
        else:
            data_min = int(data_min/10) * 10
            data_range = list(range(data_min, data_max + 1, 1))

            while len(data_range) > self.max_y_labels:
                data_range = list(range(data_min, data_max + preset[i % 3] * 10 ** (i // 3), preset[i % 3] * 10 ** (i // 3)))
                i += 1
            
        data_range.sort()

        return data_range
