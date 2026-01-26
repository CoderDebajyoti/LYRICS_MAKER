import time
import sys
import io
import random
from colorama import Fore, Style, init

# Initialize colorama for Windows terminal compatibility
init(autoreset=True)

# Ensure UTF-8 encoding for console output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def play_song(typing_speed=0.11, line_delay=1.5):
    """
    Prints the song 'Twinkle Twinkle Little Star' with typing animation and delays.
    :param typing_speed: delay between characters (float)
    :param line_delay: delay between lines (float)
    """
    lyrics = [
        "Twinkle, twinkle, little star,",
        "How I wonder what you are!",
        "Up above the world so high,",
        "Like a diamond in the sky.",
        "Twinkle, twinkle, little star,",
        "How I wonder what you are!"
    ]
    
    time.sleep(1)  # Initial delay before starting

    for i, line in enumerate(lyrics):
        # Print each character with delay
        for char in line:
            sys.stdout.write(Fore.YELLOW + char)
            sys.stdout.flush()
            time.sleep(typing_speed + random.uniform(-0.02, 0.03))
        print(Style.RESET_ALL)
        time.sleep(line_delay)

if __name__ == "__main__":
    play_song()