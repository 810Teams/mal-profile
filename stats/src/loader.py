'''
    `loader.py`
'''

from xml.dom import minidom

from src.data import Anime
from src.data import AnimeList
from src.data import Info
from src.data import User
from src.utils import error

import os


class Loader:
    ''' Loader class '''
    def __init__(self, data_dir):
        ''' Constructor '''
        self.data_dir = data_dir
        self.document = None

    def fetch_file_name(self, file_format='xml', target=-1):
        ''' Fetch file names from the specified directory '''
        try:
            return [i for i in os.listdir(self.data_dir) if i[-len(file_format):] == file_format][target]
        except IndexError:
            return None

    def create_document(self, file_name=None, auto_fetch=True):
        ''' Create document object notation (DOM) object '''
        if auto_fetch:
            file_name = self.fetch_file_name(file_format='xml', target=-1)
        self.document = minidom.parse('{}{}'.format(self.data_dir, file_name))
    
    def get_element(self, document, element_name, convert_type=True, get_data=False, get_single=False):
        ''' Retrieve elements or data from the specified element name '''
        items = document.getElementsByTagName(element_name)

        # Procedure: Retrieve non-element data
        if get_data:
            # Exception Case: Null or composite element data retrieval attempt
            try:
                items = [i.firstChild.data for i in items]

                # Prodecure: Convert type attempt
                if convert_type:
                    try:
                        items = [int(i) for i in items]
                    except ValueError:
                        try:
                            items = [float(i) for i in items]
                        except ValueError:
                            pass
            except AttributeError:
                pass
        
        # Prodecure: Retrieve a single element or data
        if get_single:
            # Exception Case: Invalid element name
            try:
                items = items[0]
            except IndexError:
                pass

        return items
    
    def get_user_object(self):
        ''' Retrieve user object '''
        return User(
            info=self.get_info_object(),
            anime_list=self.get_anime_list_object()
        )
    
    def get_info_object(self):
        ''' Retrieve user information object '''
        my_info = self.get_element(self.document, 'myinfo', get_single=True)

        return Info(
            user_id=               self.get_element(my_info, 'user_id',                get_data=True, get_single=True),
            user_name=             self.get_element(my_info, 'user_name',              get_data=True, get_single=True),
            user_export_type=      self.get_element(my_info, 'user_export_type',       get_data=True, get_single=True),
            user_total_anime=      self.get_element(my_info, 'user_total_anime',       get_data=True, get_single=True),
            user_total_watching=   self.get_element(my_info, 'user_total_watching',    get_data=True, get_single=True),
            user_total_completed=  self.get_element(my_info, 'user_total_completed',   get_data=True, get_single=True),
            user_total_onhold=     self.get_element(my_info, 'user_total_onhold',      get_data=True, get_single=True),
            user_total_dropped=    self.get_element(my_info, 'user_total_dropped',     get_data=True, get_single=True),
            user_total_plantowatch=self.get_element(my_info, 'user_total_plantowatch', get_data=True, get_single=True)
        )
    
    def get_anime_list_object(self):
        ''' Retrieve user anime list object '''
        return AnimeList(data=[self.get_anime_object(i) for i in self.get_element(self.document, 'anime')])

    def get_anime_object(self, anime_element):
        ''' Retrieve anime object '''
        return Anime(
            series_animedb_id=  self.get_element(anime_element, 'series_animedb_id',   get_data=True, get_single=True),
            series_title=       self.get_element(anime_element, 'series_title',        get_data=True, get_single=True),
            series_type=        self.get_element(anime_element, 'series_type',         get_data=True, get_single=True),
            series_episodes=    self.get_element(anime_element, 'series_episodes',     get_data=True, get_single=True),
            my_id=              self.get_element(anime_element, 'my_id',               get_data=True, get_single=True),
            my_watched_episodes=self.get_element(anime_element, 'my_watched_episodes', get_data=True, get_single=True),
            my_start_date=      self.get_element(anime_element, 'my_start_date',       get_data=True, get_single=True),
            my_finish_date=     self.get_element(anime_element, 'my_finish_date',      get_data=True, get_single=True),
            my_rated=           self.get_element(anime_element, 'my_rated',            get_data=True, get_single=True),
            my_score=           self.get_element(anime_element, 'my_score',            get_data=True, get_single=True),
            my_dvd=             self.get_element(anime_element, 'my_dvd',              get_data=True, get_single=True),
            my_storage=         self.get_element(anime_element, 'my_storage',          get_data=True, get_single=True),
            my_status=          self.get_element(anime_element, 'my_status',           get_data=True, get_single=True),
            my_comments=        self.get_element(anime_element, 'my_comments',         get_data=True, get_single=True),
            my_times_watched=   self.get_element(anime_element, 'my_times_watched',    get_data=True, get_single=True),
            my_rewatch_value=   self.get_element(anime_element, 'my_rewatch_value',    get_data=True, get_single=True),
            my_tags=            self.get_element(anime_element, 'my_tags',             get_data=True, get_single=True),
            my_rewatching=      self.get_element(anime_element, 'my_rewatching',       get_data=True, get_single=True),
            my_rewatching_ep=   self.get_element(anime_element, 'my_rewatching_ep',    get_data=True, get_single=True),
            update_on_import=   self.get_element(anime_element, 'update_on_import',    get_data=True, get_single=True)
        )
