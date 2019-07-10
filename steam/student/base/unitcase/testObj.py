class play:
    def __init__(self,x,y):
        self.x,self.y = x,y
    def moveUp(self):
        self.y+=1
    def moveDown(self):
        self.y-=1