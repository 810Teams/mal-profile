'''
    script.py
'''

from xml.dom import minidom

from src.loader import Loader
from src.loader import User
from src.render import render_by_score
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
    print('- User Data -')
    print('  Username: {}'.format(user.info.user_name))
    print('  User ID: {}'.format(user.info.user_id))
    print()
    print('- Anime Overall Data -')
    print('  Total: {}'.format(user.info.user_total_anime))
    print('  Watching: {}'.format(user.info.user_total_watching))
    print('  Completed: {}'.format(user.info.user_total_completed))
    print('  On-Hold: {}'.format(user.info.user_total_onhold))
    print('  Dropped: {}'.format(user.info.user_total_dropped))
    print('  Planned: {}'.format(user.info.user_total_plantowatch))
    print()
    print('- Anime List Data -')
    print('  Total: {}'.format(len(user.anime_list.get_scores())))
    print('  Min: {}'.format(user.anime_list.get_min()))
    print('  Max: {}'.format(user.anime_list.get_max()))
    print('  Average: {:.2f}'.format(user.anime_list.get_average()))
    print('  Median: {:g}'.format(user.anime_list.get_median()))
    print('  SD: {:.2f}'.format(user.anime_list.get_sd()))
    print()

    render_by_score(
        user.anime_list.get_summed_scores(),
        title='Rated Titles',
        file_name='rated'
    )
    render_by_score(
        user.anime_list.get_summed_grouped_scores(group_by='series_type'),
        title='Rated Titles (By Series Type)',
        file_name='rated_by_series_type'
    )

    try:
        if platform.system() == 'Windows':
            notice('Opening chart files automatically is unsupported on Windows.')
        else:
            os.system('open charts/*')
            notice('Opening chart files.')
    except (FileNotFoundError, OSError, PermissionError):
        error('Something unexpected happened, please try again.')

    if platform.system() != 'Windows':
        print()


main()
