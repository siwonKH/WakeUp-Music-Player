from playsound import playsound

import os

from alpha import Variables
from alpha import BColors


def play_music(name):
    """Plays Downloaded Music"""
    print(f"{BColors.GREEN}Now Playing{BColors.END}")
    try:
        if Variables.IS_os_WINDOWS is True:
            playsound(name)              # For Window OS
        else:
            os.system("mpg123 " + name)  # For Linux OS
        print("Complete", end='\n\n')

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return
