import schedule

import time

import request
from download import download_start
from alpha import Variables
from alpha import BColors


class Musics:
    """Music link storage"""
    musics = []
    melon_last_music = 0  # 마지막으로 재생한 멜론차트 순위를 기억


def init():
    """Starts initialization"""
    print('\n--ALL DONE--\n\n')
    Musics.musics = []
    print(Variables.schedule_time + "에 재생 예정")


def get_urls(amount, request_type, end):
    for i in range(0, amount):
        try:
            if request_type == 0:
                Musics.musics.append(request.link_request(i))
            else:
                Musics.musics.append(request.melon_request(i + end))
                Musics.melon_last_music += 1

        except IndexError:
            print(f'{BColors.WARNING}but playing only {len(Musics.musics)}{BColors.END}', end='')
            break

        except Exception as e:
            print(f'{BColors.WARNING}but Connection {BColors.FAIL}Failed{BColors.END}', end=' ')
            print('( ' + str(e), end=' )\n\n')
            if request_type == 0:
                print('Recovery System starting..')
            else:
                Musics.musics = []
            return
    print('\n------------------------------------------------')
    return 'Success'


def execute(file_dir, amount: int):
    """Starts at Scheduled Time"""
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    wday = time.localtime().tm_wday
    #wday = 0
    print('[' + week[wday] + ']')
    print('Checking api link: ', end='')
    try:
        request.link_request(1)
    except IndexError:
        init()
        return
    print(f'{BColors.GREEN}Success{BColors.END}\n')
    if wday == 5:
        print('waiting 20min')
        time.sleep(1200)
    elif wday == 6:
        print('waiting 60min')
        time.sleep(3600)

    print(f'Trying to play {amount} musics', end=' ')
    if Musics.melon_last_music > 30:  # 멜론에서 마지막으로 재생한 노래가 30번째가 넘어간다면 초기화
        Musics.melon_last_music = 0
    last_played = Musics.melon_last_music
    for i in range(0, 2):
        is_success = get_urls(amount, i, last_played)
        if is_success == 'Success':
            break

    for i in Musics.musics:
        for j in range(0, Variables.max_retry+1):
            try:
                is_success = download_start(file_dir, i)
                if is_success is False:
                    init()
                    return
                break

            except Exception as e:
                print(e.args)

                if j == Variables.max_retry:
                    init()
                    return print(f"{BColors.FAIL}Critical Fail{BColors.END}")

                time.sleep(1)
                print(f"{BColors.WARNING}Progress Failed!{BColors.END}", end=" ")
                print(f"{BColors.WARNING}retrying in 10 sec{BColors.END}")
                time.sleep(10)
    print('\n------------------------------------------------')
    init()


def before_execute():
    """Executes Function 'execute' with Parameters"""
    execute(Variables.FILE_DIR, Variables.play_song_amount)


if Variables.IS_os_WINDOWS is True:
    if not Variables.FILE_DIR.endswith("\\"):
        Variables.FILE_DIR += "\\"
else:
    if not Variables.FILE_DIR.endswith("/"):
        Variables.FILE_DIR += "/"

schedule.every().day.at(Variables.schedule_time).do(before_execute)
print(BColors.GREEN + "파일 경로: " + Variables.FILE_DIR + BColors.END)
print(Variables.schedule_time + "에 재생 예정")

while True:
    schedule.run_pending()
    time.sleep(0.1)
