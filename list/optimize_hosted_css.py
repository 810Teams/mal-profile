'''
    optimize_hosted_css.py
'''

from src.loader import Loader
from src.utils import notice

import platform

DIR = 'web/hosted/'
ANIME_IL = 'covers_anime_dataimagelink.css'
MANGA_IL = 'covers_manga_dataimagelink.css'
ANIME_IL_OPT = 'covers_anime_dataimagelink_optimized.css'
MANGA_IL_OPT = 'covers_manga_dataimagelink_optimized.css'


def main():
    ''' Main function '''
    # Initialization
    loader = Loader('data/')
    loader.create_document()
    user = loader.get_user_object(
        include_current=True,
        include_onhold=True,
        include_dropped=True,
        include_planned=True
    )

    # Load anime/manga IDs
    anime_ids = [i.series_animedb_id for i in user.anime_list.get_full_list(include_unscored=True)]
    manga_ids = [i.manga_mangadb_id for i in user.manga_list.get_full_list(include_unscored=True)]

    # Load anime/manga data image link data
    anime_il_data = [i.replace('\n', '') for i in open(DIR + ANIME_IL)][2:]
    manga_il_data = [i.replace('\n', '') for i in open(DIR + MANGA_IL)][2:]

    # Formatting anime/manga data image link data
    anime_il_data = [i for i in anime_il_data if int(i.split()[1].split('/')[2]) in anime_ids]
    manga_il_data = [i for i in manga_il_data if int(i.split()[1].split('/')[2]) in manga_ids]

    # Read anime/manga optimized data image link CSS file (If exists)
    try:
        anime_il_old_len = len([i for i in open(DIR + ANIME_IL_OPT, encoding='utf-8')])
        manga_il_old_len = len([i for i in open(DIR + MANGA_IL_OPT, encoding='utf-8')])
    except:
        pass

    # Create anime/manga optimized data image link CSS file
    anime_il_file = open(DIR + ANIME_IL_OPT, 'w', encoding='utf-8')
    manga_il_file = open(DIR + MANGA_IL_OPT, 'w', encoding='utf-8')

    # Write anime/manga optimized data image link CSS file
    anime_il_file.write('\n'.join(anime_il_data))
    manga_il_file.write('\n'.join(manga_il_data))

    # Close anime/manga optimized data image link CSS file
    anime_il_file.close()
    manga_il_file.close()

    # Notice results
    print()
    try:
        anime_il_new_len = len([i for i in open(DIR + ANIME_IL_OPT, encoding='utf-8')])
        manga_il_new_len = len([i for i in open(DIR + MANGA_IL_OPT, encoding='utf-8')])

        notice('Successfully optimized anime data image link CSS, updated from {} to {} lines.'.format(anime_il_old_len, anime_il_new_len))
        notice('Successfully optimized manga data image link CSS, updated from {} to {} lines.'.format(manga_il_old_len, manga_il_new_len))
    except:
        notice('Successfully optimized anime data image link CSS, file created.')
        notice('Successfully optimized manga data image link CSS, file created.')

    # Windows' cmd fix
    if platform.system() != 'Windows':
        print()


main()
