
class OBJ:
    def __init__(self,name):
        self.name = name 

    def use(self,word):
        pass 

    def getname(self):
        return name
    
class FOOD(OBJ):
    def __init__(self):
        super().__init__('food')

    def use(self,word):
        y = word.home.you
        y.hungry -= 1

