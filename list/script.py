'''
    script.py
'''

from pygal.style import DarkStyle

from src.loader import Loader
from src.render import RenderMachine
from src.utils import notice
from src.utils import error

import os
import platform

DISPLAY_ANIME_STATS = True
DISPLAY_MANGA_STATS = False
MUST_BE_TAGGED = ('Watching', 'Completed', 'On-Hold')
MUST_BE_UNTAGGED = ('Dropped', 'Planned')
APPLY_TAG_RULES = ('Watching', 'Completed', 'On-Hold')
ENABLE_AUTO_CHART_OPEN = False


def main():
    ''' Main function '''
    loader = Loader('data/')
    loader.create_document()
    user = loader.get_user_object(
        include_current=True,
        include_onhold=True,
        include_dropped=False,
        include_planned=False
    )
    
    improper_tagged_anime = ', '.join(get_improper_tagged(user, list_type='anime'))
    improper_tagged_manga = ', '.join(get_improper_tagged(user, list_type='manga'))

    render_machine = RenderMachine('charts/', style=DarkStyle)
    manual_sort_anime = ['TV', 'Movie', 'Special', 'OVA', 'ONA', 'Music']

    print()
    print('- User Data -')
    print('  Username: {}'.format(user.info.user_name))
    print('  User ID: {}'.format(user.info.user_id))
    print()

    if DISPLAY_ANIME_STATS:
        print('- Anime Data -')
        print('  List Data', end='\n  ')
        print('Total: {}'.format(user.anime_list.count('all')), end=' | ')
        print('Watching: {}'.format(user.anime_list.count('watching')), end=' | ')
        print('Completed: {}'.format(user.anime_list.count('completed')), end=' | ')
        print('On-Hold: {}'.format(user.anime_list.count('on-hold')), end=' | ')
        print('Dropped: {}'.format(user.anime_list.count('dropped')), end=' | ')
        print('Planned: {}'.format(user.anime_list.count('plan to watch')))
        print()
        print('  Scoring Data', end='\n  ')
        print('Total: {}'.format(len(user.anime_list.get_scores())), end=' | ')
        print('Range: {}~{}'.format(user.anime_list.get_min(), user.anime_list.get_max()), end=' | ')
        print('Average: {:.2f}'.format(user.anime_list.get_average()), end=' | ')
        print('Median: {:g}'.format(user.anime_list.get_median()), end=' | ')
        print('SD: {:.2f}'.format(user.anime_list.get_sd()))
        print()
        print('  Improper Tagged')
        print('  {}'.format(improper_tagged_anime) if len(improper_tagged_anime) > 0 else '  None, all anime are being tagged properly.')
        print()

    if DISPLAY_MANGA_STATS:
        print('- Manga Data -')
        print('  List Data', end='\n  ')
        print('Total: {}'.format(user.manga_list.count('all')), end=' | ')
        print('Reading: {}'.format(user.manga_list.count('reading')), end=' | ')
        print('Completed: {}'.format(user.manga_list.count('completed')), end=' | ')
        print('On-Hold: {}'.format(user.manga_list.count('on-hold')), end=' | ')
        print('Dropped: {}'.format(user.manga_list.count('dropped')), end=' | ')
        print('Planned: {}'.format(user.manga_list.count('plan to read')))
        print()
        print('  Scoring Data', end='\n  ')
        print('Total: {}'.format(len(user.manga_list.get_scores())), end=' | ')
        print('Range: {}~{}'.format(user.manga_list.get_min(), user.manga_list.get_max()), end=' | ')
        print('Average: {:.2f}'.format(user.manga_list.get_average()), end=' | ')
        print('Median: {:g}'.format(user.manga_list.get_median()), end=' | ')
        print('SD: {:.2f}'.format(user.manga_list.get_sd()))
        print()
        print('  Improper Tagged')
        print('  {}'.format(improper_tagged_manga) if len(improper_tagged_manga) > 0 else '  None, all manga are being tagged properly.')
        print()

    render_machine.render_pie_chart(
        user.anime_list.get_grouped_list(
            group_by='series_type',
            manual_sort=manual_sort_anime,
            disassemble_key=['my_score', 'series_title']
        ),
        title='{}\'{} Anime Series Types'.format(user.info.user_name, 's' * (user.info.user_name[-1] != 's')),
        file_name='anime_series_types'
    )
    render_machine.render_bar_chart(
        user.anime_list.get_summed_scores(),
        title='{}\'{} Scored Anime Titles'.format(user.info.user_name, 's' * (user.info.user_name[-1] != 's')),
        file_name='anime_scored'
    )
    render_machine.render_bar_chart(
        user.anime_list.get_summed_grouped_scores(
            group_by='series_type',
            manual_sort=manual_sort_anime
        ),
        title='{}\'{} Scored Anime Titles (By Series Type)'.format(user.info.user_name, 's' * (user.info.user_name[-1] != 's')),
        file_name='anime_scored_by_series_type'
    )
    render_machine.render_treemap(
        user.anime_list.get_grouped_list(
            group_by='series_type',
            manual_sort=manual_sort_anime,
            disassemble_key=['my_score', 'series_title']
        ),
        title='{}\'{} Scored Anime Treemap'.format(user.info.user_name, 's' * (user.info.user_name[-1] != 's')),
        file_name='anime_treemap'
    )
    render_machine.render_bar_chart(
        user.manga_list.get_summed_scores(),
        title='{}\'{} Scored Manga Titles'.format(user.info.user_name, 's' * (user.info.user_name[-1] != 's')),
        file_name='manga_scored'
    )


    if ENABLE_AUTO_CHART_OPEN:
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


def get_improper_tagged(user, list_type='anime'):
    ''' Get improper tagged anime/manga title list '''
    if list_type == 'anime':
        entry_list = user.anime_list.get_full_list(include_unscored=True)
    elif list_type == 'manga':
        entry_list = user.manga_list.get_full_list(include_unscored=True)
    else:
        return None

    improper = list()
    improper += [i for i in entry_list if not isinstance(i.my_tags, str) and i.my_status in MUST_BE_TAGGED] # not tagged in must tagged
    improper += [i for i in entry_list if isinstance(i.my_tags, str) and i.my_status in MUST_BE_UNTAGGED]   # tagged in must untagged
    
    tag_rules = [tuple(sorted([j.lower().strip() for j in i.split(',')])) for i in open('TAG_RULES.txt')]
    temp = [i for i in entry_list if isinstance(i.my_tags, str) and i.my_status in APPLY_TAG_RULES]

    for i in range(len(temp)):
        temp[i].my_tags = tuple(sorted([j.lower().strip() for j in temp[i].my_tags.split(',')]))

        if temp[i].my_tags not in tag_rules:
            improper.append(temp[i])
    
    if list_type == 'anime':
        return [i.series_title for i in improper]
    elif list_type == 'manga':
        return [i.manga_title for i in improper]

main()
