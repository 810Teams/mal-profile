'''
    `objects.py`
'''

from src.utils import error

from math import ceil
from math import floor
from math import sqrt


class User:
    ''' User class '''
    def __init__(self, info, anime_list):
        ''' Constructor '''
        self.info = info
        self.anime_list = anime_list


class Info:
    ''' User information class '''
    def __init__(
        self,
        user_id,
        user_name,
        user_export_type,
        user_total_anime,
        user_total_watching,
        user_total_completed,
        user_total_onhold,
        user_total_dropped,
        user_total_plantowatch
    ):
        ''' Constructor '''
        self.user_id = user_id
        self.user_name = user_name
        self.user_export_type = user_export_type
        self.user_total_anime = user_total_anime
        self.user_total_watching = user_total_watching
        self.user_total_completed = user_total_completed
        self.user_total_onhold = user_total_onhold
        self.user_total_dropped = user_total_dropped
        self.user_total_plantowatch = user_total_plantowatch


class AnimeList:
    ''' User anime list class '''
    def __init__(
        self,
        data=list(),
        include_watching=False,
        include_onhold=False,
        include_dropped=False,
        include_planned=False,
        tag_rules=None
    ):
        ''' Constructor '''
        self.data = data
        self.include_watching = include_watching
        self.include_onhold = include_onhold
        self.include_dropped = include_dropped
        self.include_planned = include_planned
        self.tag_rules = tag_rules

    def add_anime(self, anime):
        ''' Add anime object to the anime list by object '''
        self.data.append(anime)

    def get_anime(self, anime_id):
        ''' Get anime object from the anime list by anime ID '''
        for i in range(len(self.data)):
            if self.data[i].series_animedb_id == anime_id:
                return self.data[i]

        return None

    def delete_anime(self, anime_id):
        ''' Delete anime object from the anime list by anime ID '''
        for i in range(len(self.data)):
            if self.data[i].series_animedb_id == anime_id:
                return self.data.pop(i)

        return None

    def get_anime_list(self, include_unscored=False):
        ''' Get anime list '''
        return [
            i for i in self.data
            if (i.my_status != 'Watching' or self.include_watching)
            and (i.my_status != 'On-Hold' or self.include_onhold)
            and (i.my_status != 'Dropped' or self.include_dropped)
            and (i.my_status != 'Plan to Watch' or self.include_planned)
            and (i.my_score != 0 or include_unscored)
        ]
    
    def get_grouped_anime_list(
        self,
        include_unscored=False,
        group_by='series_type', 
        sort_method='most_common',
        sort_order='descending',
        manual_sort=None,
        disassemble_key=None
    ):
        ''' Get grouped anime list '''
        grouped_anime_list = dict()
        categories = list()

        filtered_anime_list = self.get_anime_list(include_unscored=include_unscored)

        # Category Retrieval
        for _ in filtered_anime_list:
            if eval('_.{}'.format(group_by)) not in categories:
                categories.append(eval('_.{}'.format(group_by)))
        
        # Category Sorting
        if sort_method == 'most_common':
            categories.sort(
                key=lambda i: [eval('j.{}'.format(group_by)) for j in filtered_anime_list].count(i),
                reverse=sort_order != 'ascending'
            )
        elif sort_method == 'alphabetical':
            categories.sort(
                reverse=sort_order != 'ascending'
            )
        else:
            error('Invalid sort_method `{}` of get_grouped_anime_list().'.format(sort_method))
            return None
        
        # Manual Sort Override
        if manual_sort != None:
            old_categories = [i for i in categories]
            categories = list()

            for i in manual_sort:
                if i in old_categories:
                    categories.append(i)
                    old_categories.remove(i)
            
            categories += old_categories

        # Packing Categories
        for i in categories:
            grouped_anime_list[i] = [j for j in filtered_anime_list if eval('j.{}'.format(group_by)) == i]

        # Desired Data Retrieval
        if disassemble_key != None:
            for i in grouped_anime_list:
                for j in range(len(grouped_anime_list[i])):
                    temp = ['grouped_anime_list[i][j].{}'.format(k) for k in disassemble_key]
                    for k in range(len(temp)):
                        temp[k] = eval(temp[k])
                    grouped_anime_list[i][j] = temp

        # Return
        return grouped_anime_list

    def get_scores(self, include_unscored=False):
        ''' Get anime scores '''
        return [i.my_score for i in self.get_anime_list(include_unscored=include_unscored)]

    def get_summed_scores(self, include_unscored=False):
        ''' Get summed anime scores '''
        return [
            self.get_scores(include_unscored=include_unscored).count(i)
            for i in range(1 - include_unscored, 11)
        ]

    def get_grouped_scores(
        self,
        include_unscored=False,
        group_by='series_type',
        sort_method='most_common',
        sort_order='descending',
        manual_sort=None
    ):
        ''' Get grouped anime scores '''
        grouped_anime_list = self.get_grouped_anime_list(
            include_unscored=False,
            group_by=group_by,
            sort_method=sort_method,
            sort_order=sort_order,
            manual_sort=manual_sort
        )
       
        for i in grouped_anime_list:
            for j in range(len(grouped_anime_list[i])):
                grouped_anime_list[i][j] = grouped_anime_list[i][j].my_score
        
        return grouped_anime_list
    
    def get_summed_grouped_scores(
        self,
        include_unscored=False,
        group_by='series_type',
        sort_method='most_common',
        sort_order='descending',
        manual_sort=None
    ):
        ''' Get summed grouped anime scores '''
        scores = self.get_grouped_scores(
            include_unscored=include_unscored,
            group_by=group_by,
            sort_method=sort_method,
            sort_order=sort_order,
            manual_sort=manual_sort
        )
        
        for i in scores:
            scores[i] = [scores[i].count(j) for j in range(1 - include_unscored, 11)]
        
        return scores

    def get_min(self):
        ''' Get a minimum of the anime list scores '''
        return min(self.get_scores())

    def get_max(self):
        ''' Get a maximum of the anime list scores '''
        return max(self.get_scores())

    def get_average(self):
        ''' Get an average of the anime list scores '''
        scores = self.get_scores()
        return sum(scores) / len(scores)

    def get_median(self):
        ''' Get a median of the anime list scores '''
        scores = sorted(self.get_scores())

        if len(scores) % 2 == 0:
            return (scores[len(scores) // 2 - 1] + scores[len(scores) // 2]) / 2
        return scores[len(scores) // 2]

    def get_mode(self):
        ''' Get a mode of the anime list scores '''
        return max(self.get_summed_scores())

    def get_sd(self):
        ''' Get a standard deviation of the anime list scores '''
        scores = self.get_scores()

        return sqrt(sum([(i - self.get_average()) ** 2 for i in scores]) / len(scores))

    def get_partial(self, percentage, part='top', rounding_method='roundx', include_unscored=False):
        ''' Get partial anime list '''
        # Anime List Initiation
        anime_list = self.get_anime_list(include_unscored=include_unscored)
        anime_list.sort(key=lambda i: i.my_score, reverse=True)
        
        # Anime Count Calculation
        anime_count = percentage / 100 * len(anime_list)

        # Anime Count Rounding Method
        if rounding_method == 'floor':
            anime_count = floor(anime_count)
        elif rounding_method == 'ceil':
            anime_count = ceil(anime_count)
        elif rounding_method == 'round':
            anime_count = round(anime_count)
        elif rounding_method == 'roundx':
            if anime_count % 0.5 == 0:
                anime_count = floor(anime_count)
            else:
                anime_count = round(anime_count)
        else:
            error('Invalid rounding_method `{}` of get_partial().'.format(rounding_method))
            return None

        # Anime List Slicing
        if part == 'top':
            return anime_list[:anime_count]
        elif part == 'bottom':
            anime_list.reverse()
            return anime_list[:anime_count]
        elif part == 'middle':
            middle = len(anime_list)//2
            upper = middle + floor(anime_count/2)
            lower = middle - ceil(anime_count/2)

            return anime_list[lower:upper]
        else:
            error('Invalid part `{}` of get_partial().'.format(part))
            return None
    
    def get_partial_average(self, percentage, part='top', rounding_method='roundx', include_unscored=False):
        ''' Get partial anime list average '''
        anime_list = self.get_partial(
            percentage=percentage,
            part=part,
            rounding_method=rounding_method,
            include_unscored=include_unscored
        )
        scores = [i.my_score for i in anime_list]

        return sum(scores)/len(scores)


class Anime:
    ''' Anime class '''
    def __init__(
        self,
        series_animedb_id=None,
        series_title=None,
        series_type=None,
        series_episodes=None,
        my_id=None,
        my_watched_episodes=None,
        my_start_date=None,
        my_finish_date=None,
        my_rated=None,
        my_score=None,
        my_dvd=None,
        my_storage=None,
        my_status=None,
        my_comments=None,
        my_times_watched=None,
        my_rewatch_value=None,
        my_tags=None,
        my_rewatching=None,
        my_rewatching_ep=None,
        update_on_import=None
    ):
        ''' Constructor '''
        self.series_animedb_id = series_animedb_id
        self.series_title = series_title
        self.series_type = series_type
        self.series_episodes = series_episodes
        self.my_id = my_id
        self.my_watched_episodes = my_watched_episodes
        self.my_start_date = my_start_date
        self.my_finish_date = my_finish_date
        self.my_rated = my_rated
        self.my_score = my_score
        self.my_dvd = my_dvd
        self.my_storage = my_storage
        self.my_status = my_status
        self.my_comments = my_comments
        self.my_times_watched = my_times_watched
        self.my_rewatch_value = my_rewatch_value
        self.my_tags = my_tags
        self.my_rewatching = my_rewatching
        self.my_rewatching_ep = my_rewatching_ep
        self.update_on_import = update_on_import
