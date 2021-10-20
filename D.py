#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DONUT.py

using pygame 
"""

import pygame
import math

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

WIDTH =1200
HEIGHT =800


# define starting postion
x_start, y_start = 0,0
x_separator = 10
y_separator = 20

# define the size
rows = HEIGHT//y_separator
columns = WIDTH//x_separator

screen_size = rows * columns

x_offset = columns/2
y_offset = rows/2

# Rotating Animation
A, B = 0, 0 

theta_spacing = 10
phi_spacing = 1

chars = ".,-~:;=!*#$@"


screen = pygame.display.set_mode((WIDTH, HEIGHT))

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
# display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Donut')
font = pygame.font.SysFont('Arial', 18, bold=True)


def text_display(letter, x_start, y_start):
    text= font.render(str(letter), True, white)
    display_surface.blit(text, (x_start, y_start))
    

run = True
while run:
    screen.fill((black))
    
    # fills Donut space
    z =[0]*screen_size
    # Background fills empty space
    b =[' '] * screen_size
    
    
    # from 0 to 2pi
    for j in range(0, 628, theta_spacing):
        # from 0 to 2pi
        for i in range(0, 628, phi_spacing):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d * 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
        # 3D x coordinate after rotation
            x = int(x_offset * 40 * D * (l * h * m - t * n))
        # 3D y coordinate after rotation
            y = int(y_offset + 20 * D * (l * h * n + t * m))
        # 3D z coordinate after rotation
            o = int(x + columns * y)
        # luminance index
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            
        if rows > y and y > 0 and x > 0 and columns > x and D > z[o]:
            z[o] = D
            b[o] = chars[N if N>0 else 0]
            
        if y_start == rows * y_separator - y_separator:
            y_start = 0
        
        for i in range(len(b)):
            A += 0.000002
            B += 0.000001
            if i == 0 or i % columns:
                text_display(b[i], x_start, y_start)
                x_start += x_separator
            else:
                y_start += y_separator
                x_start = 0
                text_display(b[i], x_start, y_start)
                x_start += x_separator
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            
