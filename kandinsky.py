#coding : utf-8
import pygame
import math
import threading
import time
from pygame import gfxdraw

scale = 1  # change the value to scale up the screen


pygame.init()
# pygame.display.init()
screen = pygame.display.set_mode((320*scale, 240*scale))
pygame.display.set_caption("kandinsky screen")
pygame.draw.rect(screen, (255, 255, 255), (0, 18*scale, 320*scale, 222*scale))
pygame.draw.rect(screen, (255, 183, 52), (0, 0, 320*scale, 18*scale))

pygame.display.flip()


font = pygame.font.Font("SourceCodeVariable-Roman.ttf", 8)


class flip(threading.Thread):
    r = 1

    def run(self):
        while self.r:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.r = 0
            pygame.display.flip()
            time.sleep(0.05)


f = flip()

f.start()


def color(r, g, b):
    return (r, g, b)


def set_pixel(x, y, color):
    red = color[0]
    green = color[1]
    blue = color[2]

    #screen.set_at((x*scale, (y+18)*scale), (red, green, blue))
    pygame.draw.rect(screen, (red, green, blue),
                     pygame.rect.Rect(x*scale, (y+18)*scale, scale, scale))
    #gfxdraw.pixel(screen, x, y+18, (red, green, blue))


def fill_rect(x, y, width, height, color):
    pygame.draw.rect(screen, color,
                     pygame.rect.Rect(x*scale, (y+18)*scale, width*scale, height * scale))


def draw_string(text, x, y, color1=(0, 0, 0), color2=(255, 255, 255)):
    screen.blit(font.render(text, True, color1, background=color2),
                (x*scale, (y+18)*scale))
    pygame.display.flip()


def get_pixel(x, y):
    w = screen.get_at((x*scale, (y+18)*scale))

    print(w)
    print(len(w))
    red = w[0]
    green = w[1]
    blue = w[2]
    return (red, green, blue)
