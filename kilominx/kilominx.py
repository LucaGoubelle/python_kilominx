""" kilominx data model """

class Kilominx:
    """ kilominx data model """
    
    
    ''' 
    kilominx constructor
    '''
    def __init__(self, **kwargs):
        self.up = kwargs['up']
        self.front = kwargs['front']
        self.left = kwargs['left']
        self.right = kwargs['right']
        self.down_left = kwargs['down_left']
        self.down_right = kwargs['down_right']
        self.abs_left = kwargs['abs_left']
        self.abs_right = kwargs['abs_right']
        self.back_left = kwargs['back_left']
        self.back_right = kwargs['back_right']
        self.back = kwargs['back']
        self.down = kwargs['down']
    
    
    '''
    cast kilominx to dict
    '''
    def to_dict(self):
        return self.__dict__
    
    
    '''
    build an instance of Kilominx 
    (virgin, not scrambled)
    '''
    @staticmethod
    def build():
        return Kilominx(
            up=["grey" for _ in  range(5)],
            front=["magenta" for _ in  range(5)],
            left=["lime" for _ in  range(5)],
            right=["beige" for _ in  range(5)],
            down_left=["blue" for _ in  range(5)],
            down_right=["red" for _ in  range(5)],
            abs_left=["yellow" for _ in  range(5)],
            abs_right=["green" for _ in  range(5)],
            back_left=["orange" for _ in  range(5)],
            back_right=["cyan" for _ in  range(5)],
            back=["purple" for _ in  range(5)],
            down=["white" for _ in  range(5)]
        )
