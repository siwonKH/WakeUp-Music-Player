class Variables:
    """variables"""
    # ========================================================
    """스케줄 시간"""
    schedule_time = "21:13:20"
    """음악이 저장될 디렉토리"""
    FILE_DIR = r"C:\Users\kanghyun\PycharmProjects\Wakeup_Music_player"

    """운영체제가 윈도우라면 True 아니면 False"""
    IS_os_WINDOWS = True

    """api 에서 불러올 음악수"""
    play_song_amount = 3

    """오류시 다시시도 횟수"""
    max_retry = 3

    """디스코드 토큰"""
    Discord_Token = ""

    """api 링크 주소"""
    API_LINK = "https://wakeup.intraedu.kr/api/music/chart"
    # ========================================================


class YtOptions:
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': False,
        'no_warnings': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }


class BColors:
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
