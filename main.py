import pgzrun 
import random

FONT_option = (255,255,255)
WIDTH=1000
HEIGHT=700
TITLE="Shooting Star Game"

CENTER_X = WIDTH/2
CENTER_Y = HEIGHT/2
CENTER = (CENTER_X, CENTER_Y)

FINAL_LEVEL = 100
START_SPEED = 20


ITEMS = ["star" , "star" , "star", "star"] 

game_over=False
game_complete=False

current_level = 1

items=[]
animations=[]

def draw():
  global items,current_level, game_complete,game_over 
  screen.clear()
  screen. blit ("bground", (0,0))
  if game_over:
    display_message( "Game Over", "Try again")
  elif game_complete:
    display_message ("You Win", "Good Job'")
  else:
    for item in items:
      item.draw()


def display_message (heading, sub_heading) :
  screen.draw.text(heading, fontsize=60, center=CENTER, color="WHITE")
  screen.draw.text(sub_heading,fontsize=40,center=(CENTER_X, CENTER_Y+20),color="WHITE")

def update():
    global items 
    if len(items)==0:
      items=make_items(current_level)

def make_items (number_of_extra_items) :
  items_to_create=get_option_to_create(number_of_extra_items)
  new_items=create_items (items_to_create)
  layout_item(new_items) 
  animate_items(new_items)
  return new_items

def get_option_to_create(number_of_extra_items):
    items_to_create = ["sun"]
    for i in range(0, number_of_extra_items):
      random_option = random. choice(ITEMS)
      items_to_create.append (random_option)
    return items_to_create

def create_items(items_to_create):
    new_items=[]
    for i in items_to_create:
      item = Actor (i+"img")
      new_items. append (item)
    return new_items

def layout_item(items_to_layout):
    number_of_gaps = len(items_to_layout) + 1
    gap_size = WIDTH/ number_of_gaps
    random.shuffle(items_to_layout)
    for index, item in enumerate(items_to_layout):
      new_xpos = (index+1) * gap_size
      item.x = new_xpos

def handle_game_over():
    global game_over
    game_over=True

def on_mouse_down(pos):
  global items, current_level   
  for item in items:
      if item.collidepoint(pos):
          if "sun" in item.image:
              handle_game_complete()
          else:
              handle_game_over()



def handle_game_complete():
    global items, current_level, animations, game_complete 
    stop_animations (animations) 
    if current_level==FINAL_LEVEL:
        game_complete=True
    else:
        current_level+=1
        items= []
        animations=[]

def stop_animations(animation_to_stop):
      for animation in animation_to_stop:
          if animation.running:
              animation. stop()

def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        duration = START_SPEED -current_level
        item.anchor=("center", "bottom" )
        animation = animate(item,  duration=duration,on_finished=handle_game_over, y = HEIGHT)
        animations.append (animation)



pgzrun.go()
