from space import *
from timeop import *
from ITEMs import BOX
import os,pickle
from person import *
class YOU:
    def __init__(self):
        self.name = '' 
        self.hp = 0
        self.atk = 0
        self.money = 0
        self.hungry = 0
        self.position = None
        self.working = False 
        self.persons = []
        self.team_money = 0 
        self.load()
        self.box = BOX(self.name)
        self.gf = []
        self.wf = []
        self.fin = [] 
        self.teams = [] 

    def remember_person(self,person):
        filepath = 'PERSONs/'+person.name+'.ps'
        with open(filepath,'wb') as bu :
            pickle.dump(person,bu)
        self.savepersons()
        self.savewife()
        self.savegf()
        self.savefin()
    def thinkwho(self,name):
        filepath = 'PERSONs/'+name+'.ps'
        if os.path.isfile(filepath):
            with open(filepath,'rb') as bu :
                who = pickle.load(bu)
                return who
        return None



    def meet(self,know=0):
        self.loadpersons()
        self.loadwife()
        self.loadfin()
        self.loadgf()
        if know==1 and len(self.persons)>0:
            who = random.choice(self.persons)
            person = self.thinkwho(who)
        else :
            person = self.creatperson()
            if person.name not in self.persons:
                self.persons.append(person.name)
            else :
                know = 1 
                who = person.name 
                person = self.thinkwho(who)
        if person.sex == 'W':
            money = random.randint(10,30)
        else :
            money = random.randint(4,20)
        return person , money , know 

    def meetwife(self,name=''):
        self.loadwife()
        if name == '' and len(self.wf) > 0 :
            wf = random.choice(self.wf)
            wife = self.thinkwho(wf)
            return wife 
        else :
            if name in self.wf :
                return self.thinkwho(name)
        return None
    def meetgf(self,name=''):
        self.loadgf()
        if name == '' and len(self.gf) > 0 :
            gf = random.choice(self.gf)
            gf = self.thinkwho(gf)
            return gf 
        else :
            if name in self.gf :
                return self.thinkwho(name)
        return None
    def meetfin(self,name=''):
        self.loadfin()
        if name == '' and len(self.fin) > 0 :
            fin = random.choice(self.fin)
            fin = self.thinkwho(fin)
            return fin 
        else :
            if name in self.fin :
                return self.thinkwho(name)
        return None


    def emotion_plus(self,person):
        person.emotion_plus(self)
        emot = person.emotion[self.name]


    def creatperson(self):
        gname = ['美','乃','奶','雪'
                 ,'蔻','冬','月','柔'
                ,'羽','寧','夢']
        bname = ['棒','肉棒','犯','間',
                '明',' 吃','王']
        who = None
        #if random.randint(0,1) == 0 :   ========== Testing =======
        if True :   
            name = [random.choice(gname) for _ in range(random.randint(2,3))]
            name = ''.join(name)
            who = GIRL(name)
        else :
            name = [random.choice(bname) for _ in range(random.randint(2,3))]
            name = ''.join(name)
            who = BOY(name)
        return who

    def move(self):
        self.position.move(self)
    def use(self,ggg):
        what = ''
        showbox(self.box.getname_list())
        what = Q('Use what?')
        item = self.box.No_get_item(what,True)
        if item is not None :
            item.use(self)
    def do(self,ggg):
        if self.position is not None :
            self.position.do(self,ggg)
    def date(self,girls):
        os.system('clear')
        names = [ str(i)+'.'+girls[i].name for i in range(len(girls))]
        showbox('|'.join(names))
        com = Q('你要約哪位呢？ ')
        if com.isdigit() :
            com = int(com)
            if com < len(girls):
                girl = girls[com]
                girl.date(self)


    def marry(self,fin):
        fin.marrying(self)

    def save(self,typ='w'):
        #self.box.savebox(self.name)
        top = TIMEOP()
        top.saveTime('hungry')
        with open('YOU.csv',typ) as f:
            wr = csv.writer(f)
            wr.writerow(['name',self.name])
            wr.writerow(['money',self.money])
            wr.writerow(['hp',self.hp])
            wr.writerow(['atk',self.atk])
            wr.writerow(['working',self.working])
            wr.writerow(['hungry',self.hungry])
            wr.writerow(['teammoney',self.team_money])
    def savepersons(self):
        with open('PKs/YOU_persons.pk','wb') as bu:
            pickle.dump(self.persons,bu)

    def savewife(self):
        with open('PKs/WIFE.pk','wb') as f:
            pickle.dump(self.wf,f)

    def saveteams(self):
        with open('PKs/TEAMS.pk','wb') as f:
            pickle.dump(self.teams,f)
    def loadteams(self):
        fil = 'PKs/TEAMS.pk'
        if not os.path.isfile(fil):
            self.teams = []
            return 
        if os.path.getsize(fil) > 0 :
            with open(fil,'rb') as bu:
                self.teams = pickle.load(bu)
        else :
            self.teams = [] 

    def loadwife(self):
        fil = 'PKs/WIFE.pk'
        if not os.path.isfile(fil):
            self.wf = []
            return 
        if os.path.getsize(fil) > 0 :
            with open(fil,'rb') as bu:
                self.wf = pickle.load(bu)
        else :
            self.wf = [] 
    
    def savefin(self):
        with open('PKs/FIN.pk','wb') as f:
            pickle.dump(self.fin,f)

    def loadfin(self):
        fil = 'PKs/FIN.pk'
        if not os.path.isfile(fil):
            self.fin = []
            return 
        with open(fil,'rb') as bu:
            self.fin = pickle.load(bu)


    def savegf(self):
        with open('PKs/GF.pk','wb') as f:
            pickle.dump(self.gf,f)

    def loadgf(self):
        fil = 'PKs/GF.pk'
        if not os.path.isfile(fil):
            self.gf = []
            return 
        with open(fil,'rb') as bu:
            self.gf = pickle.load(bu)





    def loadpersons(self):
        fil = 'PKs/YOU_persons.pk'
        if not os.path.isfile(fil):
            self.persons = []
            return 
        with open(fil,'rb') as bu:
            self.persons = pickle.load(bu)

    def putitem(self,item):
        self.box.putitem(item)

    def ishungry(self):
        top = TIMEOP()
        tims = top.calculpassTime('hungry')
        self.hungry += tims
        if self.hungry >0 and self.hungry<20:
            insshowbox('你有點餓')
        elif self.hungry> 19 and self.hungry <70:
            insshowbox('餓了')
        elif self.hungry >69 and self.hungry<90:
            insshowbox('你餓的全身發抖')

        if self.hungry > 80 :
            insshowbox('沒吃東西你會餓死')
            self.hp -= 5
        print(self.hungry)

    def load(self):
        f_exist = os.path.exists('YOU.csv')
        if f_exist:
            self.loadpersons()
            self.loadwife()
            self.loadfin()
            self.loadgf()
            with open('YOU.csv','r') as f:
                rows = csv.reader(f)
    
                sets = {'name':self.setname,
                        'hp':self.sethp,
                        'atk':self.setatk,
                        'money':self.setmoney,
                        'working':self.setworking,
                        'hungry':self.sethungry,
                        'teammoney':self.setteam_money}
                for r in rows:
                    if r[0] in sets :
                        setting = sets[r[0]]
                        setting(r[1])
        else :
            self.creatyou()
            self.savepersons()
            self.save()        

        self.ishungry()

    def creatyou(self):
        self.name = Q('Name??')
        self.hp = random.randint(5,16)
        self.money = random.randint(2,20)
        self.atk = random.randint(1,10)
        self.persons = []
        self.savepersons()

    def setteam_money(self,money):
        self.team_money = int(money)

    def setname(self,name):
        self.name = name 

    def sethp(self,hp):
        self.hp = int(hp) 

    def setatk(self,atk):
        self.atk = int(atk)

    def setmoney(self,money):
        self.money = int(money)

    def setworking(self,working):
        if working == 'True':
            self.working = True
    def sethungry(self,hungry):
        self.hungry = int(hungry)


    def getname(self):
        return self.name 

    def gethp(self):
        return self.hp

    def getatk(self):
        return self.atk

    def getmoney(self):
        return self.money
    def isdead(self):
        if self.hp < 1:
            insshowbox('!!!!!!!')
            time.sleep(0.4)
            insshowbox('你死了!!')
            return True
        return False 


