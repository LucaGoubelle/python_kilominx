""" kilominx drawer """
import pygame


class KilominxDrawer:
    """ drawing kilominx """
    
    '''
    initialize polygon coord
    '''
    def __init__(self):
        self.polygons_up = [
            [[250,7], [320,30], [250,73], [179,30]],
            [[320,30], [392,53], [365,91], [250,73]],
            [[365,91], [338,128], [250,128], [250,73]],
            [[250,128], [161,128], [135,91], [250,73]],
            [[135,91], [107,53], [179,30], [250,73]]
        ]
        self.polygons_front = [
            [[161,128], [250,128], [250,250], [134,212]],
            [[250,128], [338,128], [365,212], [250,250]],
            [[365,212], [392,296], [321,348], [250,250]],
            [[321,348], [250,399], [178,348], [250,250]],
            [[178,348], [107,296], [134,212], [250,250]]
        ]
        self.polygons_left = [
            [[107,53], [135,91], [83,194], [63,114]],
            [[135,91], [161,128], [134,212], [83,194] ],
            [[134,212], [107,296], [63,310], [83,194]], 
            [[63,310], [19,325], [19,249], [83,194]],
            [[19,249], [19,174], [63,114], [83,194]]
        ]
        self.polygons_right = [
            [[338,128], [365,91], [417,194], [365,212]], 
            [[365,91], [392,53], [437,114], [417,194]],
            [[437,114], [480,174], [480,250], [417,194]],
            [[480,250], [480,325], [436,310], [417,194]],
            [[436,310], [392,296], [365,212], [417,194]]
        ]
        self.polygons_down_left = [
            [[107,296], [178,348], [146,392], [63,310]], 
            [[178,348], [250,399], [250,446], [146,392]],
            [[250,446], [250,492], [177,469], [146,392]],
            [[177,469], [107,446], [63,386], [146,392]], 
            [[63,386], [19,325], [63,310], [146,392]]
        ]
        self.polygons_down_right = [
            [[392,296], [436,310], [353,392], [321,348]],
            [[436,310], [480,325], [436,386], [353,392]],
            [[436,386], [392,446], [321,469], [353,392]],
            [[321,469], [250,492], [250,446], [353,392]],
            [[250,446], [250,399], [321,348], [353,392]]
        ]
   
     
    '''
    draw kilominx
    '''
    def draw(self, screen, kilominx):
        self._draw_front(screen, kilominx.front)
        self._draw_up(screen, kilominx.up)
        self._draw_left(screen, kilominx.left)
        self._draw_right(screen, kilominx.right)
        self._draw_down_left(screen, kilominx.down_left)
        self._draw_down_right(screen, kilominx.down_right)
        
    
    '''
    draw front face
    '''
    def _draw_front(self, screen, face):
        for i in range(len(face)): 
            pygame.draw.polygon(screen, 
                pygame.Color(face[i]), self.polygons_front[i])
            pygame.draw.polygon(screen, 
                pygame.Color(0,0,0), self.polygons_front[i], 3)
            
    
    '''
    draw up face
    '''
    def _draw_up(self, screen, face):
        for i in range(len(face)): 
            pygame.draw.polygon(screen, 
                pygame.Color(face[i]), self.polygons_up[i])
            pygame.draw.polygon(screen, 
                pygame.Color(0,0,0), self.polygons_up[i], 3)
            
            
    '''
    draw left face
    '''
    def _draw_left(self, screen, face):
        for i in range(len(face)): 
            pygame.draw.polygon(screen, 
                pygame.Color(face[i]), self.polygons_left[i])
            pygame.draw.polygon(screen, 
                pygame.Color(0,0,0), self.polygons_left[i], 3)
            
    
    '''
    draw right face
    '''
    def _draw_right(self, screen, face):
        for i in range(len(face)): 
            pygame.draw.polygon(screen, 
                pygame.Color(face[i]), self.polygons_right[i])
            pygame.draw.polygon(screen, 
                pygame.Color(0,0,0), self.polygons_right[i], 3)
    
    
    '''
    draw down left face
    '''
    def _draw_down_left(self, screen, face):
        for i in range(len(face)): 
            pygame.draw.polygon(screen, 
                pygame.Color(face[i]), self.polygons_down_left[i])
            pygame.draw.polygon(screen, 
                pygame.Color(0,0,0), self.polygons_down_left[i], 3)
            
            
    '''
    draw down right face
    '''
    def _draw_down_right(self, screen, face):
        for i in range(len(face)): 
            pygame.draw.polygon(screen, 
                pygame.Color(face[i]), self.polygons_down_right[i])
            pygame.draw.polygon(screen, 
                pygame.Color(0,0,0), self.polygons_down_right[i], 3)
