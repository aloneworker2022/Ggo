from funcs import *

class PERSON:
    def __init__(self,name):
        self.name = name
        self.emotion = {}
        self.sex = ''
        self.relation = 0
        self.body = []
        self.head = []
        self.leg = []
        self.personal = []

    def do(self):
        pass

    def action(self):
        pass

    def emotion_plus(self,person,isyou=True):
        name = person.name
        if name in self.emotion :
            self.emotion[name] += 1 
        else :
            self.emotion[name] = 1 
        if isyou :
            self.emotion_up(person)
        
    def emotion_up(self,person):
        pass

    def say(self):
        input('Non')

class BOY(PERSON):

    def __init__(self,name):
        super().__init__(name)
        self.sex = 'M'

    def emotion_up(self,person):
        name = person.name
        point = self.emotion[name]
        if point > (self.relation+1)*2:
            self.relation += 1 
            self.emotion[name] = 0
            insshowbox('你和{}的感情又更好了!!'.format(self.name))

            if self.relation > 4 :
                self.relation = 4 




class GIRL(PERSON):

    def __init__(self,name):
        super().__init__(name)
        self.sex = 'W'
        self.fuck = {} 
        self.fucking = False 
        self.marryed_cost = random.randint(200,800)
    def emotion_up(self,person):
        name = person.name
        point = self.emotion[name]
        if point > (self.relation+1)*1 and self.relation != -9:
            if self.relation == 2 : # 好友 女友
                self.makegf(person)
            elif self.relation == 3 : # 求婚
                self.marry(person)
            else :
                self.relation += 1 
                self.emotion[name] = 0
                insshowbox('你和{}的感情又更好了!!'.format(self.name))

            if self.relation > 4 :
                self.relation = 4 

    def marry(self,person):
        befucks = 0 
        for who in self.fuck:
            befucks += self.fuck[who]
        change = 0 
        if befucks > 10 :
            change = 1 
        
        cost = self.marryed_cost/random.randint(12,20)

        cost = 0 # Test
        com = Q('求婚? 花費{}(1=y)'.format(cost))

        if com == '1'  :
            if person.money < cost :
                insshowbox('你的錢不夠 !')
                return
            chance = random.randint(0,1+change)
            if chance == 0 :
                insshowbox('{} 答應了!!!'.format(self.name))
                showbox('不過婚禮要花{}元'.format(self.marryed_cost))
                showbox('你有{}元'.format(person.money))
                if person.money >= self.marryed_cost:
                    self.marrying(person)
                self.relation = -9
                self.emotion[person.name] = 0
                if self.name in person.gf :
                    person.gf.remove(self.name)
                    person.savegf()
                person.fin.append(self.name)
                person.savefin()
            else :
                insshowbox('{} 害羞的低著頭..'.format(self.name))
                insshowbox('我們還是先這樣好嗎...')
                insshowbox()
                insshowbox('被拒絕了阿...')

    def marrying(self,person):

        com = Q('要結婚嗎?花費{}元 (1=y)'.format(self.marryed_cost))
        if person.money < self.marryed_cost:
            insshowbox('你的錢不夠....')
            return 
        if com == '1':
            person.money -= self.marryed_cost
            person.loadfin()
            person.loadgf()
            insshowbox('你和{}結為夫妻了!!!'.format(self.name))
            self.relation += 2 
            self.emotion[person.name] = 0
            person.wf.append(self.name)
            if self.name in person.gf :
                person.gf.remove(self.name)
                person.savegf()
                person.fin.remove(self.name)
                person.savefin()
            person.savewife()
            return 


    def makegf(self,person):
        name = person.name
        com = Q('告白? (1=y)')
        if com == '1':
            insshowbox('你跟{}說'.format(self.name),True)
            insshowbox('我喜歡你',True)
            if random.randint(0,2) == 0 :
                insshowbox('{}害羞地看著你'.format(self.name))
                insshowbox('我也喜歡你~~')
                insshowbox()
                insshowbox('你告白成功了')
                self.relation += 1 
                self.emotion[name] = 0
                person.gf.append(self.name) 
                person.savegf()
            else :
                insshowbox('{}:我覺得還不到時候...')
                self.emotion[name] = -3
            
    def date(self,you):
        cost = random.randint(0,5)
        cost = 0 
        showbox('要約會嗎？ 可以阿 (需要花費：{})'.format(cost))
        if you.money < cost :
            insshowbox('你的錢不夠阿..')
            return
        com = Q('你還有{}元 要約嗎？（1=y)'.format(you.money))
        self.reactionYou(you)

    def reactionYou(self,you):
        if random.randint(0,1) > 0 :
            insshowbox('{} 跟你約會很開心'.format(self.name))
            self.relation +=1 
        else :
            insshowbox('......')
            insshowbox('{}:好無聊的約會..'.format(self.name),True)



    def say(self):
        if random.randint(0,1) < 1:
            whats = loadcsv('girlsay')
            what = random.choice(whats)
            what = self.name + ':' + what[0]
            insshowbox(what,True)
