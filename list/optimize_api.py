'''
    list.py
'''

from src.loader import Loader
from src.utils import notice

import platform

DIR = 'web/api/'
ANIME_IL = 'covers_anime_dataimagelink.css'
MANGA_IL = 'covers_manga_dataimagelink.css'
ANIME_IL_OPT = 'covers_anime_dataimagelink_optimized.css'
MANGA_IL_OPT = 'covers_manga_dataimagelink_optimized.css'


def main():
    ''' Main function '''
    loader = Loader('data/')
    loader.create_document()
    user = loader.get_user_object(
        include_current=True,
        include_onhold=True,
        include_dropped=True,
        include_planned=True
    )

    anime_ids = [i.series_animedb_id for i in user.anime_list.get_full_list(include_unscored=True)]
    manga_ids = [i.manga_mangadb_id for i in user.manga_list.get_full_list(include_unscored=True)]

    anime_il_data = [i.replace('\n', '') for i in open(DIR + ANIME_IL)][2:]
    manga_il_data = [i.replace('\n', '') for i in open(DIR + MANGA_IL)][2:]

    anime_il_data = [i for i in anime_il_data if int(i.split()[1].split('/')[2]) in anime_ids]
    manga_il_data = [i for i in manga_il_data if int(i.split()[1].split('/')[2]) in manga_ids]

    anime_il_file = open(DIR + ANIME_IL_OPT, 'w', encoding='utf-8')
    manga_il_file = open(DIR + MANGA_IL_OPT, 'w', encoding='utf-8')

    anime_il_file.write('\n'.join(anime_il_data))
    manga_il_file.write('\n'.join(manga_il_data))

    anime_il_file.close()
    manga_il_file.close()

    print()
    notice('Successfully optimized anime data image link CSS.')
    notice('Successfully optimized manga data image link CSS.')

    if platform.system() != 'Windows':
        print()

main()
