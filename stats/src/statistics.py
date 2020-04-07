'''
    statistics.py
'''

from math import sqrt


def median(raw_data):
    ''' Function: Calculates median '''
    raw_data_copy = sorted([i for i in raw_data])
    if len(raw_data_copy) % 2 == 0:
        return (raw_data_copy[len(raw_data_copy) // 2 - 1] + raw_data_copy[len(raw_data_copy) // 2]) / 2
    return raw_data_copy[len(raw_data_copy) // 2]


def average(raw_data):
    ''' Function: Calculates average '''
    return sum(raw_data) / len(raw_data)


def standard_dev(raw_data):
    ''' Function: Calculates standard deviation '''
    return sqrt(sum([(i - average(raw_data)) ** 2 for i in raw_data])/len(raw_data))
    