""" entry point """
import sys
import pygame

from kilominx.kilominx import Kilominx
from kilominx.kilominx_drawer import KilominxDrawer

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
            
    screen.fill(BGCOLOR)
    # ---------- graphics stuffs here -----------------
    minx_drawer.draw(screen, minx)
    # ------------------------------------------------
    pygame.display.update()
    clock.tick(60)
