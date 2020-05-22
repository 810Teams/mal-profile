'''
    list.py
'''

from src.loader import Loader


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

    anime_imagelink = [i.replace('\n', '') for i in open('web/css_import/covers_anime_dataimagelink.css')][2:]
    manga_imagelink = [i.replace('\n', '') for i in open('web/css_import/covers_manga_dataimagelink.css')][2:]

    anime_imagelink = [i for i in anime_imagelink if int(i.split()[1].split('/')[2]) in anime_ids]
    manga_imagelink = [i for i in manga_imagelink if int(i.split()[1].split('/')[2]) in manga_ids]

    anime_imagelink_file = open('web/css_import_optimized/anime_imagelink.css', 'w', encoding='utf-8')
    manga_imagelink_file = open('web/css_import_optimized/manga_imagelink.css', 'w', encoding='utf-8')

    anime_imagelink_file.write(' '.join(anime_imagelink))
    manga_imagelink_file.write(' '.join(manga_imagelink))

    anime_imagelink_file.close()
    manga_imagelink_file.close()

main()
