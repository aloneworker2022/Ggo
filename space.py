from funcs import *
from timeop import TIMEOP
import random,time
from ITEMs import *
class space:

    def __init__(self,name):
        self.name = name

    def do(self):
        pass

    def move(self,you):
        what = Q('1:回去')
        if what == '1' :
            home = HOME()
            you.position = home

    def see(self):
        pass


class testword(space):
    def __init__(self):
        super().__init__('TEST WORD')

    def do(self,you,ggg):
        what = Q('a : aa b:bb')


        you.position = home()
    def see(self):
        pass

class WORKSPACE(space):
    def __init__(self,working=False):
        super().__init__('worke space')
        if not working:
            insshowbox(txtload('WORKSPACE'))


    def done(self,you):
        insshowbox('You work back')
        time.sleep(0.4)
        top = TIMEOP()
        tim = top.calculpassTime('workt')
        if tim < 3 :
            money = 1 
        elif tim > 2 and tim < 9:
            money = int(tim/2)
        elif tim > 8 and tim < 25 :
            money = int(tim/random.randint(1,2))
        elif tim > 24 and time < 68 :
            money = int(tim)
        elif tim > 68 :
            money = int(tim*2)
        insshowbox('You get '+str(money))
        you.money += money
        time.sleep(0.4)
        you.working = False 

    def do(self,you,ggg):
        what = Q('要打工嗎？ (y=1)')
        if what == '1':
            insshowbox('開始打工！！！')
            top = TIMEOP()
            top.saveTime('workt')
            you.working = True
            ggg.gaming = False

    def see(self):
        pass

class SHOP(space):
    def __init__(self):
        super().__init__('商店')
        txt = txtload('SHOP')
        insshowbox(txt)

    def do(self,you,ggg):
        what = Q('1:買食物 2:買道具 3:賣')
        whats = {'1':self.buyfood,
                 '2':self.buyitem,
                 '3':self.sell}
        if what in whats:
            doing = whats[what]
            doing(you)

    def buyfood(self,you):
        box = putItem('FOODS')
        com = ''
        while com != 'e' :
            os.system('clear')
            print('[SHOP]')
            showbox(box.getname_list_cost())
            com = Q('Buy what? (#)')
            item = box.No_get_item(com)
            if item is not None :
                com = Q('{} 賣 {} 元 ok? (1=y)'.format(item.name,item.cost))
                if com == '1' and you.money >= item.cost :
                    you.money -= item.cost
                    you.putitem(item)
                    insshowbox('You buy {}'.format(item.name))

    def buyitem(self,you):
        pass

    def sell(self,you):
        box = you.box 
        com = ''
        while com != 'e':
            os.system('clear')
            print('[SHOP]')
            showbox(box.getname_cost())
            com = Q('Sell what?')
            item = box.popitem(com)
            if item is not None :
                insshowbox('You sell {}'.format(item.name))
                you.money += item.cost

class BAR(space):
    def __init__(self):
        super().__init__('Bar')
        insshowbox(txtload('BAR'))

    def do(self,you,ggg):
        ticket = random.randint(2,5)
        com = Q('入場請付 {} 元 (1=y)'.format(ticket))
        if com == '1' and you.money >= ticket :
            you.money -= ticket
        else :
            return 

        while com != 'e':
            know = random.randint(0,2)
            person ,cost ,know= you.meet(know)
            com = Q('要請旁邊的人喝一杯嗎？ 須花費 {} (1=y)'.format(cost))
            if com == '1' and you.money >= cost :
                you.money -= cost
                showbox('你請了對方喝一杯')
                if know == 1 :
                    insshowbox('你遇到熟人{}'.format(person.name),True)
                    you.emotion_plus(person)
                else :
                    insshowbox('你好 我叫{}'.format(person.name),True)
                    if person.sex == 'W':
                        insshowbox('你認識了 女子 {}'.format(person.name),True)
                        
                    else :
                        insshowbox('你認識了 {}'.format(person.name),True)
                        
                you.remember_person(person)

            else :
                insshowbox('你離開了！！')
                return  


    def see(self):
        pass

class HOME(space):

    def __init__(self):
        super().__init__('Home')
        insshowbox(txtload('HOME'))



    def do(self,you,ggg):
        what = ''
        while what != 'e':
            os.system('clear')
            what = Q('what 1:use')
            if what == '1':
                you.use(ggg)

    def move(self,you):
        what = Q("你要去？ 1:SHOP ,2:CASINO ,3:BAR ,4:WORK")
        where = {'1':SHOP,
                 '2':CASINO,
                 '3':BAR,
                 '4':WORKSPACE}
        if what in where :
            spac = where[what]
            you.position = spac()

    def see(self):
        pass

class CASINO(space):
    def __init__(self):
        super().__init__('casino')
        insshowbox(txtload('CASINO'))
        self.cards = []
        self.youhand = []
        self.cpuhand = []
        self.money = 0 
    def do(self,you,ggg):
        os.system('clear')
        if you.money < 1 :
            return 
        com = Q('你要賭嗎？ (y=1)')
        if com == '1' :
            com = Q('多少錢(you have{})？'.format(you.money))
            if com.isdigit():
                self.money = int(com)
                if self.money >= you.money :
                    self.money = you.money 
                you.money -= self.money
            else :
                insshowbox('su3')
                return
        else :
            return
        self.star()
        value = self.yourun(you)
        if value < 0 :
            showbox('You lose!!!!')
            return 
        if value > 0 :
            return 
        insshowbox('CPU turn!')
        self.cpurun(you)

    def see(self):
        pass
    def star(self):
        self.cards = []
        self.youhand = []
        self.cpuhand = []
        insshowbox('開始')
        self.cards = self.initcard()
    def initcard(self):
        card = [x for x in range(1,14)]
        card = card + card + card + card 
        card = [0.5 if x == 11 or x == 12 or x == 13 else x for x in card] 
        random.shuffle(card)
        return card
    def putcard(self):
        if len(self.cards) < 1 :
            self.cards = self.initcard()
        card = self.cards.pop(0)
        return card

    def yourun(self,you):
        com = ''
        while com != '1':
            card = self.putcard()
            insshowbox(card)
            self.youhand.append(card)
            print(self.printcards(self.youhand))
            if sum(self.youhand) > 10.5 :
                self.broken()
                return -1 
            if len(self.youhand) > 4 :
                insshowbox('You pass 5!!!')
                you.money += (self.money * 4)
                return 1
            com = Q('可以了？ {y=1}')
        return 0 
    def broken(self):
        insshowbox('你爆了！！！')

    def printcards(self,cards):
        return ''.join(['['+str(x)+']' for x in cards])
       
    def cpurun(self,you):
        while True:
            card = self.putcard()
            insshowbox('CPU get {}'.format(card))
            self.cpuhand.append(card)
            print('CPU cards:')
            showbox(self.printcards(self.cpuhand))
            print('\n\n\nYour cards:')
            showbox(self.printcards(self.youhand))
            input()
            value = sum(self.cpuhand)
            if value > 10.5 :
                insshowbox('對手爆了！！！')
                you.money += (self.money*2)
                return 
            elif value > 8 :
                youvalu = sum(self.youhand)
                if youvalu >= value :
                    insshowbox('You win!!!')
                    you.money += (self.money*2)
                else :
                    insshowbox('CPU win!!!')
                return 
