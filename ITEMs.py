from funcs import *
import pickle , os
def creatItem(typ,data):
        if typ == 'FOODS':
            name = data[0]
            cost = data[1]
            param = data[2]
            food = FOOD(name,cost,param)
            return food 
        return None 
    
def loaditem(typ):
        data = loadcsv(typ)
        items = []
        for item in data:
            item = creatItem(typ,item)
            if item is not None :
                items.append(item)
        return items

def putItem(typ):
        box = BOX()
        items = loaditem(typ)
        box.putitems(items)
        return box


class BOX:
    def __init__(self,name=''):
        self.items = []
        if name != '' :
            self.loadbox(name)

    def savebox(self,name):
        with open(name+'.pk','wb') as bu :
            pickle.dump(self.items,bu)


    def loadbox(self,name):
        if not os.path.isfile(name+'.pk'):
            self.savebox(name)
            return
        with open(name+'.pk','rb') as bu :
            self.items = pickle.load(bu)

    def putitem(self,item):
        self.items.append(item)
    def putitems(self,items):
        self.items = items
    def getname(self):
        names = [it.name for it in self.items]
        names = ['['+n+']' for n in names]
        return ''.join(names)

    def getname_cost(self):
        pass

    def getname_list_cost(self):
        nlc = [str(i)+'.'
              +self.items[i].name
              +' $'+str(self.items[i].cost)
               for i in range(len(self.items))]
        return nlc

    def getname_list(self):
        nl = [str(i)+'.'+self.items[i].name for i in range(len(self.items))] 
        return nl
    def No_get_item(self,no,pop=False):
        if not no.isdigit():
            return None
        no = int(no)
        if no < len(self.items):
            if pop :
                return self.items.pop(no)
            return self.items[no]
        return None


    def showname(self):
        names = self.getname()
        showbox(names)
    def showname_cost(self):
        nc = self.getname_cost()
        showbox(nc)
    def popitem(self,name):
        if name in self.items:
            return self.items.pop(name)
        return None

    def getitem(self,name):
        if name in self.items:
            return self.items[name]
        return None 
class FOOD:
    def __init__(self,name,cost,param):
        self.name = name 
        self.param = param
        self.cost = int(cost)
        self.typ = 'FOOD'
    def use(self,param=None):
        showbox('你吃了{}'.format(self.name))
        showbox('回復 {} 飢餓'.format(self.param))
        input()
        param.hungry -= int(self.param)

