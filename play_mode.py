import game_framework
from pico2d import *
import game_world
from boy import Boy
from grass import Grass

paused = False
paused_keyups = []
inventory_open = False
inventory_image = None


def handle_events():
    global paused, paused_keyups, inventory_open

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            inventory_open = not inventory_open
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            paused = not paused
            if not paused:
                for keyup in paused_keyups:
                    boy.handle_event(keyup)
                paused_keyups.clear()
        elif paused:
            if event.type == SDL_KEYUP:
                paused_keyups.append(event)
        elif (inventory_open and event.type == SDL_KEYDOWN and
              event.key == SDLK_2):
            boy.large_ball_selected = True
        elif (inventory_open and event.type == SDL_KEYDOWN and
              event.key == SDLK_1):
            boy.large_ball_selected = False
        else:
            boy.handle_event(event)


def init():
    global boy, paused, paused_keyups, inventory_open, inventory_image

    paused = False
    paused_keyups = []
    inventory_open = False
    game_world.clear()
    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)
    inventory_image = load_image('item_select.png')


def update():
    if not paused:
        game_world.update()


def render():
    clear_canvas()
    game_world.render()
    if paused:
        draw_rectangle(740, 540, 780, 580, 30, 30, 30, 220, True)
        draw_rectangle(750, 550, 757, 570, 255, 255, 255, 255, True)
        draw_rectangle(763, 550, 770, 570, 255, 255, 255, 255, True)
    if inventory_open:
        inventory_image.draw(400, 300)
    update_canvas()

def finish():
    global boy, inventory_image, inventory_open
    game_world.clear()
    boy = None
    inventory_image = None
    inventory_open = False
