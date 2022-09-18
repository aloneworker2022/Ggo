import datetime
class TIMEOP:
    def __init__(self):
        pass


    def getNowTime(self):
        temp = '%Y|%m|%d|%H|%M'
        now = datetime.datetime.now()
        return now

    def saveTime(self,fname='T'):
        fname = fname +'.t'
        temp = '%Y|%m|%d|%H|%M'
        now = datetime.datetime.now()
        now_st = now.strftime(temp)
        with open(fname,'w') as fi:
            fi.write(now_st)
            return 
        print('Save Time error')

    def loadTime(self,fname='T'):
        fname = fname +'.t'
        temp = '%Y|%m|%d|%H|%M'
        with open(fname,'r') as fi :
            tist = fi.read()
            time = datetime.datetime.strptime(tist,temp)
            return time
        return None

    def calculpassTime(self,fname='T'):
        now = datetime.datetime.now()
        time = self.loadTime(fname)
        timepass = int((now - time)/datetime.timedelta(minutes=30))
        return timepass


