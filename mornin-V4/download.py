import youtube_dl

import os

import play
from alpha import BColors
from alpha import YtOptions


'''class DownLoad:
    def __init__(self, file_dir: str, link: str):
        self.file_dir = file_dir
        self.link = link
        self.downloaded = self._download_start()

    def _download_start(self):
        """Download Music File"""
        reset_dir(self.file_dir)
        download(self.link)
        link = str(link)
        music_id = link.split('https://youtube.com/watch?v=')[1]
        file_name = rename(music_id, file_dir)
        play.play_music(file_name)

    def _reset_dir(self, file_dir):
        """Reset Music Directory"""
        try:
            for file in os.listdir(file_dir):
                if file.endswith(".mp3") and not file.startswith("default.mp3"):
                    os.remove(file)
            return print(f"{BColors.GREEN}Music Directory Reset Complete{BColors.END}")

        except FileNotFoundError as e:
            print(f"{BColors.FAIL}File Directory is Wrong:{BColors.END} {e.filename}")
            exit()

    def _download(self, url):
        """Download as .mp3 file"""
        print("다운로드중..")
        with youtube_dl.YoutubeDL(YtOptions.ydl_opts) as ydl:
            ydl.download([url])
        print("다운로드 완료")

    def _rename(self, rank, file_dir):
        """Rename Downloaded .mp3 file"""
        for file in os.listdir(file_dir):
            if file.endswith(".mp3") and not file.startswith("default.mp3"):
                name = f"song{str(rank)}.mp3"
                os.rename(file, name)
                return name'''


import youtube_dl

import os

import play
from alpha import BColors
from alpha import YtOptions


def download_start(file_dir, link):
    """Download Music File"""
    reset_dir(file_dir)
    download(link)
    link = str(link)
    music_id = link.split('https://youtube.com/watch?v=')[1]
    file_name = rename(music_id, file_dir)
    play.play_music(file_name)


def reset_dir(file_dir):
    """Reset Music Directory"""
    try:
        for file in os.listdir(file_dir):
            if file.endswith(".mp3") and not file.startswith("default.mp3"):
                os.remove(file)
        return print(f"{BColors.GREEN}Music Directory Reset Complete{BColors.END}")

    except FileNotFoundError as e:
        print(f"{BColors.FAIL}File Directory is Wrong:{BColors.END} {e.filename}")
        exit()


def download(url):
    """Download as .mp3 file"""
    print("다운로드중..")
    with youtube_dl.YoutubeDL(YtOptions.ydl_opts) as ydl:
        ydl.download([url])
    print("다운로드 완료")


def rename(rank, file_dir):
    """Rename Downloaded .mp3 file"""
    for file in os.listdir(file_dir):
        if file.endswith(".mp3") and not file.startswith("default.mp3"):
            name = f"song{str(rank)}.mp3"
            os.rename(file, name)
            return name
