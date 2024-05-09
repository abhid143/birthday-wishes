import pyfiglet
from termcolor import colored
import time

text = "Thala For a Reason"

def print_with_animation(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)  
    print()  

ascii_art = pyfiglet.figlet_format(text, font="standard")

def print_ascii_art_with_animation(ascii_art):
    for line in ascii_art.split("\n"):
        print_with_animation(line)

msd_art = pyfiglet.figlet_format("MSD", font="standard", width=180)

print_with_animation(colored(ascii_art.strip(), color="yellow"))

print_ascii_art_with_animation(msd_art.strip())
