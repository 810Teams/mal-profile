'''
    script.py
'''

from xml.dom import minidom

from src.loader import Loader
from src.loader import User
from src.render import render_by_level
from src.utils import notice
from src.utils import error

import os
import platform


def main():
    ''' Main function '''
    loader = Loader('data/')
    loader.create_document(auto_fetch=True)
    user = loader.get_user_object()

    print()
    print(' - {}\'s Anime List Statistics -'.format(user.info.user_name))
    print()
    print('   Total: {}'.format(user.info.user_total_anime))
    print('   Average: {:.2f}'.format(user.anime_list.get_average()))
    print('   Median: {:.0f}'.format(user.anime_list.get_median()))
    print('   SD: {:.2f}'.format(user.anime_list.get_sd()))
    print()

    render_by_level(user.anime_list.get_summed_scores())

    try:
        if platform.system() == 'Windows':
            notice('Opening chart files automatically is unsupported on Windows.')
        else:
            os.system('open charts/*')
            notice('Opening chart files.')
    except (FileNotFoundError, OSError, PermissionError):
        error('Something unexpected happened, please try again.')

    print()

main()
