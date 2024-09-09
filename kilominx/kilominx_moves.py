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
