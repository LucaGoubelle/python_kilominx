import copy
from kilominx.kilominx_rotate_utils import RotateUtils


''' move Up face '''
def move_U(minx):
    minx.up = RotateUtils.rotate(minx.up)

    new_front = RotateUtils.gen_empty_face()
    new_left = RotateUtils.gen_empty_face()
    new_right = RotateUtils.gen_empty_face()
    new_back_left = RotateUtils.gen_empty_face()
    new_back_right = RotateUtils.gen_empty_face()
    
    for i in range(2):
        new_front[i] = minx.right[i]
        new_left[i] = minx.front[i]
        new_right[i] = minx.back_right[i]
        new_back_left[i] = minx.left[i]
        new_back_right[i] = minx.back_left[i]
        
    minx.front = RotateUtils.transfert(minx.front, new_front)
    minx.left = RotateUtils.transfert(minx.left, new_left)
    minx.right = RotateUtils.transfert(minx.right, new_right)
    minx.back_left = RotateUtils.transfert(minx.back_left, new_back_left)
    minx.back_right = RotateUtils.transfert(minx.back_right, new_back_right)
    
    return minx


''' move Up face reverse '''
def move_U_prime(minx):
    for _ in range(4):
        minx = move_U(minx)
    return minx


''' move Right face '''
def move_R(minx):
    minx.right = RotateUtils.rotate(minx.right)
    
    front_copy = copy.deepcopy(minx.front)
    dr_copy = copy.deepcopy(minx.down_right)
    ar_copy = copy.deepcopy(minx.abs_right)
    br_copy = copy.deepcopy(minx.back_right)
    up_copy = copy.deepcopy(minx.up)
    
    new_up = ['', front_copy[1], front_copy[2], '', '']
    new_front = ['', dr_copy[0], dr_copy[1], '', '']
    new_down_right = [ar_copy[4], ar_copy[0], '', '', '']
    new_abs_right = [br_copy[0], '', '', '', br_copy[4]]
    new_back_right = [up_copy[2], '', '', '', up_copy[1]]
    
    minx.up = RotateUtils.transfert(minx.up, new_up)
    minx.front = RotateUtils.transfert(minx.front, new_front)
    minx.down_right = RotateUtils.transfert(minx.down_right, new_down_right)
    minx.abs_right = RotateUtils.transfert(minx.abs_right, new_abs_right)
    minx.back_right = RotateUtils.transfert(minx.back_right, new_back_right)
    
    return minx


''' move Right face reverse '''
def move_R_prime(minx):
    for _ in range(4):
        minx = move_R(minx)
    return minx


''' move Left face '''
def move_L(minx):
    minx.left = RotateUtils.rotate(minx.left)

    u_copy = copy.deepcopy(minx.up)
    f_copy = copy.deepcopy(minx.front)
    dl_copy = copy.deepcopy(minx.down_left)
    al_copy = copy.deepcopy(minx.abs_left)
    bl_copy = copy.deepcopy(minx.back_left)

    new_front = [u_copy[4],'','','',u_copy[3]]
    new_up = ['','','',bl_copy[1],bl_copy[2]]
    new_down_left = [f_copy[0],'','','',f_copy[4]]
    new_abs_left = [dl_copy[4],dl_copy[0], '','','']
    new_back_left = ['',al_copy[0],al_copy[1],'','']

    minx.up = RotateUtils.transfert(minx.up, new_up)
    minx.front = RotateUtils.transfert(minx.front, new_front)
    minx.down_left = RotateUtils.transfert(minx.down_left, new_down_left)
    minx.abs_left = RotateUtils.transfert(minx.abs_left, new_abs_left)
    minx.back_left = RotateUtils.transfert(minx.back_left, new_back_left)

    return minx


''' move Left face reverse '''
def move_L_prime(minx):
    for _ in range(4):
        minx = move_L(minx)
    return minx


''' move Front face '''
def move_F(minx):
    minx.front = RotateUtils.rotate(minx.front)
    
    u_copy = copy.deepcopy(minx.up)
    l_copy = copy.deepcopy(minx.left)
    r_copy = copy.deepcopy(minx.right)
    dl_copy = copy.deepcopy(minx.down_left)
    dr_copy = copy.deepcopy(minx.down_right)
    
    new_up = ['','',l_copy[1],l_copy[2],'']
    new_left = ['',dl_copy[0],dl_copy[1],'','']
    new_right = [u_copy[3],'','','',u_copy[2]]
    new_down_left = [dr_copy[4],dr_copy[0],'','','']
    new_down_right = [r_copy[0],'','','',r_copy[4]]
    
    minx.up = RotateUtils.transfert(minx.up, new_up)
    minx.left = RotateUtils.transfert(minx.left, new_left)
    minx.right = RotateUtils.transfert(minx.right, new_right)
    minx.down_left = RotateUtils.transfert(minx.down_left, new_down_left)
    minx.down_right = RotateUtils.transfert(minx.down_right, new_down_right)
    
    return minx


''' move Front face reverse '''
def move_F_prime(minx):
    for _ in range(4):
        minx = move_F(minx)
    return minx


''' move Down Left face '''
def move_DL(minx):
    minx.down_left = RotateUtils.rotate(minx.down_left)
    
    f_copy = copy.deepcopy(minx.front)
    l_copy = copy.deepcopy(minx.left)
    dr_copy = copy.deepcopy(minx.down_right)
    d_copy = copy.deepcopy(minx.down)
    al_copy = copy.deepcopy(minx.abs_left)
    
    new_front = ['','','',l_copy[2], l_copy[3]]
    new_left = ['','',al_copy[1], al_copy[2],'']
    new_down_right = ['','','',f_copy[3], f_copy[4]]
    new_down = [dr_copy[4], '', '', '', dr_copy[3]]
    new_abs_left = ['',d_copy[4], d_copy[0], '', '']
    
    minx.front = RotateUtils.transfert(minx.front, new_front)
    minx.left = RotateUtils.transfert(minx.left, new_left)
    minx.down_right = RotateUtils.transfert(minx.down_right, new_down_right)
    minx.down = RotateUtils.transfert(minx.down, new_down)
    minx.abs_left = RotateUtils.transfert(minx.abs_left, new_abs_left)
    
    return minx


''' move Down Left face reverse '''
def move_DL_prime(minx):
    for _ in range(4):
        minx = move_DL(minx)
    return minx


''' move Down Right face '''
def move_DR(minx):
    return minx


''' move Down Right face reverse '''
def move_DR_prime(minx):
    for _ in range(4):
        minx = move_DL(minx)
    return minx
