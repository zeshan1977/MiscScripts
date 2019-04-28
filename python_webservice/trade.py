class trade():
    def __init__(self,id,title,description,done):
        self.id=id
        self.title=title
        self.description=description
        self.done=True
    def printall(self):
        print self.__dict__

