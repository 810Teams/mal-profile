'''
    script.py
'''

from pygal.style import DarkStyle
from xml.dom import minidom

from src.data import User
from src.loader import Loader
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

    render_machine = RenderMachine('charts/', style=DarkStyle)
    manual_sort = ['TV', 'Movie', 'Special', 'OVA', 'ONA', 'Music']

    render_machine.render_pie_chart(
        user.anime_list.get_grouped_anime_list(
            group_by='series_type',
            manual_sort=manual_sort,
            disassemble_key=['my_score', 'series_title']
        ),
        title='{}\'{} Series Types'.format(user.info.user_name, 's' * (user.info.user_name[-1] != 's')),
        file_name='{}_series types'.format(user.info.user_name.lower())
    )
    render_machine.render_bar_chart(
        user.anime_list.get_summed_scores(),
        title='{}\'{} Scored Titles'.format(user.info.user_name, 's' * (user.info.user_name[-1] != 's')),
        file_name='{}_scored'.format(user.info.user_name.lower())
    )
    render_machine.render_bar_chart(
        user.anime_list.get_summed_grouped_scores(
            group_by='series_type',
            manual_sort=manual_sort
        ),
        title='{}\'{} Scored Titles (By Series Type)'.format(user.info.user_name, 's' * (user.info.user_name[-1] != 's')),
        file_name='{}_scored_by_series_type'.format(user.info.user_name.lower())
    )
    render_machine.render_treemap(
        user.anime_list.get_grouped_anime_list(
            group_by='series_type',
            manual_sort=manual_sort,
            disassemble_key=['my_score', 'series_title']
        ),
        title='{}\'{} Treemap'.format(user.info.user_name, 's' * (user.info.user_name[-1] != 's')),
        file_name='{}_treemap'.format(user.info.user_name.lower())
    )

    try:
        if platform.system() == 'Windows':
            notice('Opening chart files automatically is unsupported on Windows.')
        else:
            os.system('open charts/*')
            notice('Opening chart files.')
    except (FileNotFoundError, OSError, PermissionError):
        error('Something unexpected happened, please try again.')

    experimental_zone()

    if platform.system() != 'Windows':
        print()


def experimental_zone(enable=False):
    ''' Experimental zone '''
    if not enable:
        return

    loader = Loader('data/')
    loader.create_document(auto_fetch=True)
    user = loader.get_user_object(
        include_watching=True,
        include_onhold=True,
        include_dropped=False,
        include_planned=False
    )
    
    # print()
    # print('- Partial Averages -')
    # print('  Top 10%: {:.2f}'.format(user.anime_list.get_partial_average(10, part='top')))
    # print('  Top 20%: {:.2f}'.format(user.anime_list.get_partial_average(20, part='top')))
    # print('  Top 50%: {:.2f}'.format(user.anime_list.get_partial_average(50, part='top')))
    # print('  Middle 50%: {:.2f}'.format(user.anime_list.get_partial_average(50, part='middle')))
    # print('  Bottom 50%: {:.2f}'.format(user.anime_list.get_partial_average(50, part='bottom')))
    # print('  Bottom 20%: {:.2f}'.format(user.anime_list.get_partial_average(20, part='bottom')))
    # print('  Bottom 10%: {:.2f}'.format(user.anime_list.get_partial_average(10, part='bottom')))

    # print()
    # anime_list = user.anime_list.get_anime_list(include_unscored=False)

    # for i in anime_list:
    #     print(i.series_title)
    # for i in anime_list:
    #     print(i.my_score)


main()
