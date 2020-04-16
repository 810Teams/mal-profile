'''
    script.py
'''

from pygal.style import DarkStyle
from xml.dom import minidom

from src.loader import Loader
from src.loader import User
from src.render import RenderMachine
from src.utils import notice
from src.utils import error

import os
import platform


def main():
    ''' Main function '''
    loader = Loader('data/')
    loader.create_document(auto_fetch=True)
    user = loader.get_user_object(
        include_watching=True,
        include_onhold=True,
        include_dropped=False,
        include_planned=False
    )

    print()
    print('- User Data -')
    print('  Username: {}'.format(user.info.user_name))
    print('  User ID: {}'.format(user.info.user_id))
    print()
    print('- Anime List Data -')
    print('  Total: {}'.format(user.info.user_total_anime))
    print('  Watching: {}'.format(user.info.user_total_watching))
    print('  Completed: {}'.format(user.info.user_total_completed))
    print('  On-Hold: {}'.format(user.info.user_total_onhold))
    print('  Dropped: {}'.format(user.info.user_total_dropped))
    print('  Planned: {}'.format(user.info.user_total_plantowatch))
    print()
    print('- Scoring Data -')
    print('  Total: {}'.format(len(user.anime_list.get_scores())))
    print('  Range: {}~{}'.format(user.anime_list.get_min(), user.anime_list.get_max()))
    print('  Average: {:.2f}'.format(user.anime_list.get_average()))
    print('  Median: {:g}'.format(user.anime_list.get_median()))
    print('  SD: {:.2f}'.format(user.anime_list.get_sd()))
    print()

    render_machine = RenderMachine(style=DarkStyle)

    render_machine.render_by_score(
        user.anime_list.get_summed_scores(),
        title='Scored Titles',
        file_name='scored'
    )
    render_machine.render_by_score(
        user.anime_list.get_summed_grouped_scores(group_by='series_type'),
        title='Scored Titles (By Series Type)',
        file_name='scored_by_series_type'
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
