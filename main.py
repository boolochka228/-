from pygame import *
from settings import *
from sounds import load_sounds
from keys import draw_keys, create_key_rects

init()
screen = display.set_mode ((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption("Piano Game")

sounds = load_sounds(KEYS)
key_rects = create_key_rects(len(KEYS))
keys_list = list(KEYS.key())
my_font = font.SysFont("Arial", 24)
pressed_keys = set()

# кнопки меню
def start_game (): pass
def open_settings(): pass
def exit_game(): quit()

buttons = [
  Buttons(60, 20, 120, 40, "Settings",  open_settings)
]
running = True 
while running: 
  screen. fill(WHITE)

#кнопки
for button in buttons:
  buttton.draw(screen, my_font)

#клавіши
draw_keys(screen
