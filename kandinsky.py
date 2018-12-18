import pygame
import math

pygame.init()
screen = pygame.display.set_mode((320, 240))
pygame.display.set_caption("kandinsky screen")
usable = pygame.surface.Surface((320, 222))
pygame.draw.rect(usable, (255, 255, 255), (0, 0, 320, 222))
screen.blit(usable, (0, 18))
pygame.draw.rect(screen, (255, 183, 52), (0, 0, 320, 18))

pygame.display.flip()


font = pygame.font.Font("SourceCodeVariable-Roman.ttf", 8)


def render():
    screen.blit(usable, (0, 18))
    pygame.display.flip()


def color(r, g, b):
    return b // 8 + g // 4 * 2**5 + r // 8 * 2**11


def set_pixel(x, y, color):
    red = (color // 2048)*8
    green = (color - (red * 2048 // 8)) // 32 * 4
    blue = (color - (red * 2048 // 8) - (green * 32 // 4))*8
    pygame.draw.rect(usable, (red, green, blue), pygame.rect.Rect(x, y, 1, 1))
    render()


def draw_string(text, x, y):
    screen.blit(font.render(text, True, (0, 0, 0)), (x, y+18))
    pygame.display.flip()


def get_pixel(x, y):
    pxarray = pygame.PixelArray(usable)
    w = hex(pxarray[x, y])
    red = w[2] + w[3]
    green = w[4] + w[5]
    blue = w[6] + w[7]
    blue = int(blue, 16)//8
    green = int(green, 16)//4*2**5
    red = int(red, 16)//8*2**11
    return red + green + blue
