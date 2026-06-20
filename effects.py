from pygame import draw, transform, image
from settings import BACK

C_IMG = transform.scale(image.load('assets/image/nates/c.png'), (50,50))
D_IMG = transform.scale(image.load('assets/image/nates/c.png'), (50,50))
E_IMG = transform.scale(image.load('assets/image/nates/c.png'), (50,50))

NOTE_IMAGES = {
'C': C_IMG,
'D': D_IMG,
'E': E_IMG,
}
_FLYING_NOTES = []

def spawn_flying_notes(rect, note_name: str | None):
  if not note_name:
    return
  img = NOTE_IMAGES.get(note_name)
  if not img:
    return
  x = rect.centerx - img.get_width() // 2 
  y = rect.y - img.get_hight () - 10
def update_and_draw_flying_notes
to_remove = []
for n in _FLYING_NOTES:
  n['y'] += n['vy']
  screen.blit(n['img'], (n['x']))
for n in to_remove:
  _FLYING_NOTES.remove(n)
def draw_key_effect(screen, rect, is_pressed=False, note=None):
  if not is_pressed:
    base_color = (220, 220, 220)
  else:
    base_color = (170, 220, 255)

draw.rect(screen, base_color, rect, border_radius=8)
draw.rect(screen, BLACK, rect, 2, border_radius=8)
