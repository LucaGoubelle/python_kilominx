""" entry point """
import sys
import pygame

from kilominx.kilominx import Kilominx
from kilominx.kilominx_drawer import KilominxDrawer
from kilominx.kilominx_moves import *
from kilominx.kilominx_axis_moves import *

# --- pygame init -----------------------
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Python Kilominx")
BGCOLOR = (32,32,32)
# ------------------------------------------


# ----- minx stuffs -----
minx = Kilominx.build()
minx_drawer = KilominxDrawer()
# -----------------------

# -------------- main loop -------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                minx = move_U(minx)
            if event.key == pygame.K_m:
                minx = move_U_prime(minx)
            if event.key == pygame.K_o:
                minx = move_R(minx)
            if event.key == pygame.K_l:
                minx = move_R_prime(minx)
            if event.key == pygame.K_s:
                minx = move_L(minx)
            if event.key == pygame.K_z:
                minx = move_L_prime(minx)
            if event.key == pygame.K_j:
                minx = move_F(minx)
            if event.key == pygame.K_f:
                minx = move_F_prime(minx)

            if event.key == pygame.K_LEFT:
                minx = move_y(minx)
            if event.key == pygame.K_RIGHT:
                minx = move_y_prime(minx)
            
    screen.fill(BGCOLOR)
    # ---------- graphics stuffs here -----------------
    minx_drawer.draw(screen, minx)
    # ------------------------------------------------
    pygame.display.update()
    clock.tick(60)
