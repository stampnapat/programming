import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_heart(scale):
    heart = [
        "  *****   *****  ",
        " ******* ******* ",
        "*****************",
        " **************** ",
        "  *************   ",
        "   ***********    ",
        "    *********     ",
        "     *******      ",
        "      *****       ",
        "       ***        ",
        "        *         "
    ]
    
    for line in heart:
        print(" " * int((1 - scale) * 10) + line)

def heart_animation():
    scales = [i * 0.1 for i in range(1, 11)]
    scales += scales[::-1]
    
    while True:
        for scale in scales:
            clear_screen()
            print_heart(scale)
            time.sleep(0.1)

if __name__ == "__main__":
    heart_animation()
