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

ENABLE_AUTO_CHART_OPEN = False
MUST_TAGGED = ('Watching', 'Completed', 'On-Hold')
MUST_UNTAGGED = ('Dropped', 'Planned')
APPLY_TAG_RULES = ('Watching', 'Completed', 'On-Hold')

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
    
    improper_tagged = ', '.join(get_improper_tagged())

    render_machine = RenderMachine('charts/', style=DarkStyle)
    manual_sort = ['TV', 'Movie', 'Special', 'OVA', 'ONA', 'Music']

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
    print('- Improper Tagged Anime -')
    print('  {}'.format(improper_tagged) if len(improper_tagged) > 0 else '  None, all anime are being tagged properly.')
    print()

    render_machine.render_pie_chart(
        user.anime_list.get_grouped_anime_list(
            group_by='series_type',
            manual_sort=manual_sort,
            disassemble_key=['my_score', 'series_title']
        ),
        title='{}\'{} Series Types'.format(user.info.user_name, 's' * (user.info.user_name[-1] != 's')),
        file_name='series_types'
    )
    render_machine.render_bar_chart(
        user.anime_list.get_summed_scores(),
        title='{}\'{} Scored Titles'.format(user.info.user_name, 's' * (user.info.user_name[-1] != 's')),
        file_name='scored'
    )
    render_machine.render_bar_chart(
        user.anime_list.get_summed_grouped_scores(
            group_by='series_type',
            manual_sort=manual_sort
        ),
        title='{}\'{} Scored Titles (By Series Type)'.format(user.info.user_name, 's' * (user.info.user_name[-1] != 's')),
        file_name='scored_by_series_type'
    )
    render_machine.render_treemap(
        user.anime_list.get_grouped_anime_list(
            group_by='series_type',
            manual_sort=manual_sort,
            disassemble_key=['my_score', 'series_title']
        ),
        title='{}\'{} Treemap'.format(user.info.user_name, 's' * (user.info.user_name[-1] != 's')),
        file_name='treemap'
    )

    try:
        if not ENABLE_AUTO_CHART_OPEN:
            pass
        elif platform.system() == 'Windows':
            notice('Opening chart files automatically is unsupported on Windows.')
        else:
            os.system('open charts/*')
            notice('Opening chart files.')
    except (FileNotFoundError, OSError, PermissionError):
        error('Something unexpected happened, please try again.')

    if platform.system() != 'Windows':
        print()


def get_improper_tagged():
    ''' Get improper tagged anime title list '''
    loader = Loader('data/')
    loader.create_document(auto_fetch=True)
    user = loader.get_user_object(
        include_watching=True,
        include_onhold=True,
        include_dropped=True,
        include_planned=True
    )
    anime_list = user.anime_list.get_anime_list(include_unscored=True)

    improper = list()
    improper += [i for i in anime_list if not isinstance(i.my_tags, str) and i.my_status in MUST_TAGGED] # not tagged in must tagged
    improper += [i for i in anime_list if isinstance(i.my_tags, str) and i.my_status in MUST_UNTAGGED]   # tagged in must untagged
    
    tag_rules = [tuple(sorted([j.lower().strip() for j in i.split(',')])) for i in open('TAG_RULES.txt')]
    temp = [i for i in anime_list if isinstance(i.my_tags, str) and i.my_status in APPLY_TAG_RULES]

    for i in range(len(temp)):
        temp[i].my_tags = tuple(sorted([j.lower().strip() for j in temp[i].my_tags.split(',')]))

        if temp[i].my_tags not in tag_rules:
            improper.append(temp[i])
    
    return [i.series_title for i in improper]

main()
