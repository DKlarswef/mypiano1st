# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 16:55:43 2020

@author: 杨龙辉
"""

import pygame
import sys
import time
from pygame.locals import *

keyDict={
	K_1:"c",
	K_2:"d",
	K_3:"e",
	K_4:"f",
	K_5:"g",
	K_6:"a",
	K_7:"b",
	K_8:"c1",
	K_9:"d1",
	K_0:"e1",
	K_MINUS:"f1",
	K_EQUALS:'g1',
	K_q:'a1',
	K_w:'b1',
	K_e:'c2',
	K_r:'d2',
	K_t:'e2',
	K_y:'f2',
	K_u:'g2',
	K_i:'a2',
	K_o:'b2',
	K_p:'c3',
	K_a:'d3',
	K_s:'e3',
	K_d:'f3',
	K_f:'g3',
	K_g:'a3',
	K_h:'b3',
	K_j:'c4',
	K_k:'d4',
	K_l:'e4',
	K_z:'f4',
	K_x:'g4',
	K_c:'a4',
	K_v:'b4',
	K_b:'c5'
}

pygame.init()
pygame.mixer.init()

bg_size = width, height = 300,200
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("Music")

pygame.mixer.set_num_channels(32)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            key = event.key
            if key in keyDict.keys():
                pygame.mixer.Sound("audios/" + keyDict[key] + ".wav").play(maxtime = 1500)
                
    time.sleep(0.01)