import unittest , datetime ,random,os,time , csv ,pickle
from timeop import TIMEOP
from word import WORD
import logging
from tabulate import tabulate  
from you import YOU
from space import *
from ITEMs import *
from person import *
from timeop import *
testing = True

if testing :
    logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.DEBUG)
else :
    logging.basicConfig(level=logging.ERROR)

def de(message):
    logging.debug(message)

testing = True
you = None 
if testing :
    you = YOU()
class T(unittest.TestCase):

    def loggging(self):
        top = TIMEOP()
        howlong = top.calculpassTime('Teamstart')
        howlong = howlong/4
        self.Booking(howlong)

    def Booking(self,days):
        days = 4 
        for i in range(days):
            insshowbox()
            if len(you.teams) < 1 :
                insshowbox('探險隊 就此音訊全無.....',True)
                #return
            insshowbox('Day {}'.format(i+1))
            dice = random.randint(0,2)
            if dice == 0 :
                self.writespace()
            elif dice == 1 :
                self.writefight()
            elif dice == 2 :
                insshowbox('CITY',True)
            
        

    def writespace(self):
        A = txtload('A')
        B = txtload('B')
        C = txtload('D')
        insshowbox(A,True)
        insshowbox(B,True)
        insshowbox(C,True)

    def putdice(self,chance):

        if chance > random.randint(1,100) :
            return True
        return False

        
    def writefight(self):
        insshowbox('隊伍遇到了')
        if self.putdice(80) :
            emony = txtload('M')
            insshowbox(emony,True)
            bon  = len(you.teams)*3
            if self.putdice(70+(bon)):      
                insshowbox('消滅了{}'.format(emony))
                money = you.team_money * 2 /len(you.teams) 
                insshowbox('團隊獲得 {}元'.format(money))
            else :
                insshowbox('隊伍戰敗....')
                you.team = [] 
                you.saveteams()
        else :
            emony = txtload('N')
            emony += txtload('M')
            insshowbox(emony,True)
            bon  = len(you.teams)*3
            if self.putdice(30+(bon)):      
                insshowbox('消滅了{}'.format(emony))
                money = you.team_money * 5 /len(you.teams)
                insshowbox('團隊獲得 {}元'.format(money))
            else :
                insshowbox('隊伍戰敗....')
                you.teams = []
                you.saveteams()
    def test_writecity(self):
        pass



    def trastart(self): # Start Train!!!!
        you.loadteams()
        if len(you.teams) > 0 :
            insshowbox('Already go!!')
            return 
        self.choicepeop()
        if len(you.teams) < 1:
            insshowbox('No man!!!')
            return 

        com = Q('Spend Money ? (you have {})'.format(you.money))
        money = 0
        while True :
            
            if com.isdigit() :
                money = int(com)
                if money > you.money :
                    money = you.money
                money_ = money/len(you.teams)
            com = Q('{} for one Use ok?'.format(money_))
            if com == 'y' :
                you.money -= money
                you.setteam_money(money_)
                break 
            com = Q('Spend Money ? (you have {})'.format(you.money)) 

        top = TIMEOP()
        top.saveTime('Teamstart')
        you.save() 


    def traning(self):
        you.loadteams()
        if len(you.teams) > 0 :
            insshowbox('Already go !!!!')



    def test_tranback(self):
        you.loadteams()
        if len(you.teams) > 0 :
            com = Q('要把探險隊叫回來？ y ?')
            if com == 'y' :
                self.logging()
                self.teamdissolve()




    def teamdissolve(self):
        for peop in you.teams:
            peop = you.thinkwho(peop)
            insshowbox(peop.name)
            if peop.relation == -9:
                you.fin.append(peop.name)
            elif peop.relation == 2:
                you.gf.append(peop.name)
            elif peop.relation == 3:
                you.wf.append(peop.name)
            else :
                you.persons.append(peop.name)
        you.teams = [] 
        you.savepersons()
        you.savewife()
        you.savegf()
        you.savefin()
        you.saveteams()



    def choicepeop(self):
        persons = []
        if random.randint(0,3) > 0:
            you.loadgf()
            you.loadfin()
            you.loadwife()
            persons += you.gf 
            persons += you.fin
            persons += you.wf
        
        persons += you.persons
        com = Q('幾個人?? 2~8')
        if com.isdigit() :
            team = []
            com = int(com)
            if com > 2 and com < 9 :
                for _ in range(com):
                    if len(persons) > 0 :
                        who = random.choice(persons)
                        persons.remove(who)
                        insshowbox('{} 加入探險隊了'.format(who))
                        team.append(who)
                        if who in you.gf :
                            you.gf.remove(who)
                        elif who in you.fin:
                            you.fin.remove(who)
                        elif who in you.wf :
                            you.wf.remove(who)
                        elif who in you.persons:
                            you.persons.remove(who)
                you.teams = team

                insshowbox('{} 人出去探險了!!'.format(len(team)))
                you.saveteams()
                you.savepersons()
                you.savewife()
                you.savegf()
                you.savefin()
       

               

    


class GO:
    def __init__(self):
        self.you = YOU()
        self.gaming = True
        if self.you.working :
            self.you.position = WORKSPACE(True)
            self.you.position.done(self.you)
        else :
            self.you.position = HOME()
        self.dead = False 

    def __call__(self):
        com = ''
        while com != 'e' and self.gaming :
            if self.you.isdead():
                self.dead = True
                break



            if not testing :
                os.system('clear')
            
            stat = [self.you.name,'HP:'+str(self.you.hp),'$:'+str(self.you.money)]
            showbox('|'.join(stat))


            print('    {}'.format(self.you.position.name))

            if self.you.position.name == 'Home':
                wife = self.you.meetwife()
                gf = self.you.meetgf()
                fin = self.you.meetfin()
                whos = []
                if wife is not None and random.randint(0,2) > 0 :
                    whos.append(wife)
                elif gf is not None and random.randint(0,2) == 0:
                    whos.append(gf)
                elif fin is not None and random.randint(0,3) > 1 :
                    whos.append(fin)
                st = ''

                for who in whos :
                    who.say()

                for p in whos :
                    st += ' '+p.name
                if st != '' :
                    print(st)
                what = '1:MOVE 2:DO' 
                if len(whos) > 0 :
                    what += ' 3:DATE'
                
                if fin is not None and self.you.money > fin.marryed_cost:
                    what += ' 4:MARRY'

                what += ' e:exit'


                com = Q(what)
                if com == '1':
                    self.you.move()
                elif com == '2':
                    self.you.do(self)
                elif com == '3' and len(whos) > 0:
                    self.you.date(whos)
                elif com == '4' and fin is not None :
                    self.you.marry(fin)

            else :
                what = '1:MOVE 2:DO e:exit'

                com = Q(what)
            
                if com == '1' :
                    self.you.move()
                elif com == '2':
                    self.you.do(self)
        self.you.save()
        if self.dead:
            self.deading()


    def deading(self):
        os.remove('YOU.csv')
        os.remove(self.you.name+'.pk')
        os.remove('YOU_persons.pk')
        os.remove('GF.pk')
        os.remove('FIN.pk')
        os.remove('WIFE.pk')
        

if __name__ == '__main__':
    if testing:
        
        unittest.main()
    else :
        go = GO()
        go()
