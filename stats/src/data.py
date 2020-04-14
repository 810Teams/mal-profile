'''
    `objects.py`
'''

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
    def __init__(self, data=list()):
        ''' Constructor '''
        self.data = data

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

    def get_anime_list(self, include_unrated=False, include_planned=False):
        ''' Get anime list with query '''
        return [
            i for i in self.data
            if (i.my_score != 0 or include_unrated) and (i.my_status != 'Plan to Watch' or include_planned)
        ]

    def get_scores(self, include_unrated=False, include_planned=False):
        ''' Get anime scores '''
        return [
            i.my_score 
            for i in self.get_anime_list(
                include_unrated=include_unrated,
                include_planned=include_planned
            )
        ]

    def get_summed_scores(self, include_unrated=False, include_planned=False):
        ''' Get summed anime scores '''
        return [
            self.get_scores(
                include_unrated=include_unrated,
                include_planned=include_planned
            ).count(i)
            for i in range(1 - include_unrated, 11)
        ]

    def get_grouped_scores(self, include_unrated=False, include_planned=False, group_by='series_type'):
        ''' Get grouped anime scores '''
        scores = dict()
        categories = list()

        anime_list_filtered = self.get_anime_list(
            include_unrated=include_unrated,
            include_planned=include_planned
        )

        for _ in anime_list_filtered:
            if eval('_.{}'.format(group_by)) not in categories:
                categories.append(eval('_.{}'.format(group_by)))
        
        categories.sort(
            key=lambda i: [eval('j.{}'.format(group_by)) for j in self.data].count(i),
            reverse=True
        )

        for i in categories:
            scores[i] = [j.my_score for j in self.data if eval('j.{}'.format(group_by)) == i]

        return scores
    
    def get_summed_grouped_scores(self, include_unrated=False, include_planned=False, group_by='series_type'):
        ''' Get summed grouped anime scores '''
        scores = self.get_grouped_scores(
            group_by=group_by,
            include_unrated=include_unrated,
            include_planned=include_planned
        )
        
        for i in scores:
            scores[i] = [scores[i].count(j) for j in range(1 - include_unrated, 11)]
        
        return scores

    def get_min(self, include_unrated=False, include_planned=False):
        ''' Get a minimum of the anime list scores '''
        return min(self.get_scores(
            include_unrated=include_unrated,
            include_planned=include_planned
        ))

    def get_max(self, include_unrated=False, include_planned=False):
        ''' Get a maximum of the anime list scores '''
        return max(self.get_scores(
            include_unrated=include_unrated,
            include_planned=include_planned
        ))

    def get_average(self, include_unrated=False, include_planned=False):
        ''' Get an average of the anime list scores '''
        scores = self.get_scores(
            include_unrated=include_unrated,
            include_planned=include_planned
        )
        return sum(scores) / len(scores)

    def get_median(self, include_unrated=False, include_planned=False):
        ''' Get a median of the anime list scores '''
        scores = sorted(self.get_scores(
            include_unrated=include_unrated,
            include_planned=include_planned
        ))

        if len(scores) % 2 == 0:
            return (scores[len(scores) // 2 - 1] + scores[len(scores) // 2]) / 2
        return scores[len(scores) // 2]

    def get_mode(self, include_unrated=False, include_planned=False):
        ''' Get a mode of the anime list scores '''
        return max(self.get_summed_scores(
            include_unrated=include_unrated,
            include_planned=include_planned
        ))

    def get_sd(self, include_unrated=False, include_planned=False):
        ''' Get a standard deviation of the anime list scores '''
        scores = self.get_scores(
            include_unrated=include_unrated,
            include_planned=include_planned
        )

        return sqrt(sum([
            (i - self.get_average(
                include_unrated=include_unrated,
                include_planned=include_planned
            )) ** 2
            for i in scores
        ]) / len(scores))


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
