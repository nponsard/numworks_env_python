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
    return b // 8 + g // 4 * 2**5 + r // 8 * 2**11


def set_pixel(x, y, color):
    red = (color // 2048)*8
    green = (color - (red * 2048 // 8)) // 32 * 4
    blue = (color - (red * 2048 // 8) - (green * 32 // 4))*8
    screen.set_at((x*scale, (y+18)*scale), (red, green, blue))
    #gfxdraw.pixel(screen, x, y+18, (red, green, blue))
    #pygame.draw.rect(usable, (red, green, blue), pygame.rect.Rect(x, y, 1, 1))


def draw_string(text, x, y):
    screen.blit(font.render(text, True, (0, 0, 0)), (x*scale, (y+18)*scale))
    pygame.display.flip()


def get_pixel(x, y):
    pxarray = pygame.PixelArray(screen)
    w = hex(pxarray[x*scale, (y+18)*scale])
    red = w[2] + w[3]
    green = w[4] + w[5]
    blue = w[6] + w[7]
    blue = int(blue, 16)//8
    green = int(green, 16)//4*2**5
    red = int(red, 16)//8*2**11
    return red + green + blue
