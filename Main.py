import pygame as py

py.init()
screen = py.display.set_mode((500,500))
py.display.set_caption("Pixel Rush")
clock = py.time.Clock()


running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False



    py.display.flip()
    clock.tick(60)