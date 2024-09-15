
class RotateUtils:
    """ rotate Utils """
    
    
    ''' 
    Gen Empty Face 
    '''
    @staticmethod
    def gen_empty_face():
        return [ "" for _ in range(5)]
    
    
    '''
    rotate face clockwise
    '''
    @staticmethod
    def rotate(face):
        new_face = [ "" for _ in range(5)]
        
        new_face[0] = face[4]
        new_face[1] = face[0]
        new_face[2] = face[1]
        new_face[3] = face[2]
        new_face[4] = face[3]
        
        return new_face
    
    
    '''
    rotate face counter clockwise
    '''
    @staticmethod
    def rotate_async(face):
        for _ in range(4):
            face = RotateUtils.rotate(face)
        return face
    
    
    '''
    rotate face clockwise twice
    '''
    @staticmethod
    def rotate_twice(face):
        for _ in range(2):
            face = RotateUtils.rotate(face)
        return face
    
    
    '''
    rotate face clockwise three times
    '''
    @staticmethod
    def rotate_three(face):
        for _ in range(3):
            face = RotateUtils.rotate(face)
        return face
    
    
    '''
    rotate face counter clockwise twice
    '''
    @staticmethod
    def rotate_twice_async(face):
        for _ in range(2):
            face = RotateUtils.rotate_async(face)
        return face


    '''
    rotate face counter clockwise three times
    '''
    @staticmethod
    def rotate_three(face):
        for _ in range(3):
            face = RotateUtils.rotate_async(face)
        return face


    '''
    transfert new_face to face 
    '''
    @staticmethod
    def transfert(face, new_face):
        for i in range(len(face)):
            face[i] = new_face[i] if new_face[i] != "" else face[i]
        return face
