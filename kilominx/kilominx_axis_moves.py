""" kilominx axis moves """
import copy
from kilominx.kilominx_rotate_utils import RotateUtils


''' Move y axis '''
def move_y(minx):
    minx.up = RotateUtils.rotate(minx.up)
    minx.down = RotateUtils.rotate_async(minx.down)

    new_front = copy.deepcopy(minx.right)
    new_left = copy.deepcopy(minx.front)
    new_right = copy.deepcopy(minx.back_right)
    new_back_left = copy.deepcopy(minx.left)
    new_back_right = copy.deepcopy(minx.back_left)

    new_down_left = copy.deepcopy(minx.down_right)
    new_down_right = copy.deepcopy(minx.abs_right)
    new_abs_left = copy.deepcopy(minx.down_left)
    new_abs_right = copy.deepcopy(minx.back)
    new_back = copy.deepcopy(minx.abs_left)

    minx.front = RotateUtils.transfert(minx.front, new_front)
    minx.left = RotateUtils.transfert(minx.left, new_left)
    minx.right = RotateUtils.transfert(minx.right, new_right)
    minx.back_left = RotateUtils.transfert(minx.back_left, new_back_left)
    minx.back_right = RotateUtils.transfert(minx.back_right, new_back_right)
    
    minx.down_left = RotateUtils.transfert(minx.down_left, new_down_left)
    minx.down_right = RotateUtils.transfert(minx.down_right, new_down_right)
    minx.abs_left = RotateUtils.transfert(minx.abs_left, new_abs_left)
    minx.abs_right = RotateUtils.transfert(minx.abs_right, new_abs_right)
    minx.back = RotateUtils.transfert(minx.back, new_back)

    return minx


''' Move y axis reverse '''
def move_y_prime(minx):
    for _ in range(4):
        minx = move_y(minx)
    return minx
