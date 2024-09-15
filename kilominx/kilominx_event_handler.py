""" event handler """
import pygame

from kilominx.moves.kilominx_moves import *
from kilominx.moves.kilominx_axis_moves import *


class KilominxEventHandler:
    """ event handler """


    ''' handle moves '''
    @staticmethod
    def handle_moves(event, minx):
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
        if event.key == pygame.K_d:
            minx = move_DL(minx)
        if event.key == pygame.K_q:
            minx = move_DL_prime(minx)
        if event.key == pygame.K_n:
            minx = move_DR(minx)
        if event.key == pygame.K_c:
            minx = move_DR_prime(minx)
        return minx
    

    ''' handle axis moves '''
    @staticmethod
    def handle_axis_moves(event, minx):
        if event.key == pygame.K_LEFT:
            minx = move_y(minx)
        if event.key == pygame.K_RIGHT:
            minx = move_y_prime(minx)
        return minx
