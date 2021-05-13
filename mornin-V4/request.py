import requests
from youtube_search import YoutubeSearch
from melon_top100 import get_songs
import json

from alpha import Variables
from alpha import BColors


def link_request(num: int):
    """Get music ID from API"""
    try:
        # print(f'{BColors.GREEN}Sending Request to: WAKEUP API{BColors.END}', end='')
        api_url = Variables.API_LINK
        data = requests.get(api_url)
        url = 'https://youtube.com/watch?v='
        url += data.json()[num]['info']['id']
        return url

    except IndexError:
        raise IndexError


def melon_request(num: int):
    """Get music title from melon"""
    try:
        print(f'{BColors.GREEN}Sending Request to: MELON{BColors.END}({num+1})')
        melon_data = get_songs()
        name = melon_data[num]['title']
        data = YoutubeSearch(name, max_results=1)
        url = 'https://youtube.com/watch?v='
        url += data.videos[0]['id']
        return url

    except IndexError:
        raise IndexError


def music_count():
    api_url = Variables.API_LINK
    data = requests.get(api_url)
    musics = 0
    try:
        for cnt in range(0, 5):
            url = data.json()[cnt]['info']['id']
            musics = cnt+1

    except IndexError:
        return musics


'''melon_data = requests.get('https://ko28melonapi.herokuapp.com/chart/live')
        name = melon_data.json()[str(num + 1)]['name']
        data = YoutubeSearch(name, max_results=1)
        # data = data.to_json(clear_cache=False)
        url = 'https://youtube.com/watch?v='
        url += data.videos[0]['id']'''