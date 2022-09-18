from tabulate import tabulate
import csv,os,time,random
def showbox(what):
        what = [[what]]
        print(tabulate(what,tablefmt='fancy_grid'))
        print('\n')
def insshowbox(what='',nextkey = False ):
        os.system('clear')
        print('\n\n\n')
        if what == '' :
            print()
            time.sleep(0.9)
            os.system('clear')
            return 
        what= [[what]]
        print(tabulate(what,tablefmt='fancy_grid'))
        if nextkey :
            input()
        else :
            time.sleep(0.9)
        os.system('clear')
    
def loadcsv(fname):
        fname = fname +'.csv'
        data = []
        with open(fname) as csvf:
            rows = csv.reader(csvf)
            for row in rows:
                data.append(row)
        return data

def txtload(fname):
    ds = loadcsv(fname)
    ds = random.choice(ds)
    return ds[0]
def star():
        os.system('clear')
        txt = txtload('startTxt')
        insshowbox(txt)


def Q(what):
    Qbox = [['[?] '+what]]
    com = input(tabulate(Qbox, tablefmt='fancy_grid'))
    com = com.replace('[I','')
    return com



