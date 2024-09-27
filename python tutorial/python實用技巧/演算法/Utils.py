import copy
from random import randint

Utils_Glogals = globals()

class Utils:
    
    @staticmethod
    def randSort(a):
        b = []
        while len(a)>0:
            c = len(a)
            b.append(a.pop(randint(0,c-1)))
        return b
    @staticmethod
    def intersection(a,b):
        c = []
        for i in a:
            if i in b:
                c.append(i)
        return c
    @staticmethod
    def notIn(a,b): #a not in b
        c = []
        for i in a:
            if not i in b:
                c.append(i)
        return c
    @staticmethod
    def norepeat(a):
        b = []
        for i in a:
            if not i in b:
                b.append(i)
        return b
    @staticmethod
    def randSortByTime(lis,way=lambda length:round(time.time()*length)%length):
        a = lis+[""]
        t = way(len(a))
        t = t+1
        b = []
        while len(a)>0:
            for i in range(len(a)-1,-1,-t):
                b.append(a.pop(i))
        a = b[1:]
        return a
    @staticmethod
    def search(*words,List=[],mode="and",limit=10**10):
        result = []
        for token in List:
            if not len(token)<limit: continue
            token1 = token.lower() #不分大小寫
            flag = 0
            for word in words: #從所有關鍵字尋找
                keyWord = word.lower() #關鍵字不分大小寫
                if keyWord in token1: 
                    flag+=1
            if mode=="and" and flag==len(words): #全部找到
                result.append(token)
            elif mode=="or" and flag>0: #有找到
                result.append(token)
        return result
    @staticmethod
    def scan(word,maxLength=None):
        result = []
        for i in range(len(word)): # 0~last index of word
            for j in range(i+1,len(word)+1): # start:i, end:j ->  i+1~last index of word
                result.append(word[i:j])
                if j-i==maxLength: break
        return result
    @staticmethod
    # Be careful to use this function, if you don't understand this, don't use this, only use import keyword.
    def make_attrs_global(obj, global_, skip=0, cover=0, message=""):
        #https://stackoverflow.com/questions/30098037/call-function-from-class-without-declaring-name-object?rq=3
        for attr in dir(obj):
            if not attr.startswith('__'):
                if attr in global_:
                    if not cover:
                        if skip:
                            print(message, "Warning : SKIP", attr )
                        else:
                            raise Exception("This MUST NOT DO THIS Operate, SET (CHILD NAME) to GLOBALS USING SAME NAME AS PARENT NAME" + " " + attr)
                else:
                    global_[attr] = getattr(obj, attr)
    @staticmethod
    def randlist(start,end,length):
        return [randint(start,end) for i in range(length)]
    @staticmethod
    def randget(a):
        if len(a)==0: return None
        return a[randint(0,len(a)-1)]
    @staticmethod
    def Probability(dic={"item1":0.7,"item2":0.1,"item3":0.2},preci=2):
        p = dic.values()
        l = dic.keys()
        p = [int(i*(10**preci)) for i in p]
        start = 0
        for i in range(len(p)):
            p[i] = [start,start+p[i]]
            start = p[i][1]
        seed = randint(1,(10**preci))
        result = ""
        for i,b in zip(p,l):
            if seed>i[0] and seed<=i[1]:
                result = b
                break
        return result
    @staticmethod
    def findtl(target,lis,compare=lambda x:x,activate=lambda a,b:a==b):
        res = []
        for n,i in enumerate(lis):
            e = compare(i)
            if activate(target,e):
                return n,i
    @staticmethod
    def searchtl(target,lis,compare=lambda x:x,activate=lambda a,b:a==b):
        res = []
        for n,i in enumerate(lis):
            e = compare(i)
            if activate(target,e):
                res.append([n,i])
        return res
    @staticmethod
    def ProbabilityL(p=[0.1,0.2,0.7],l=[1,2,3],preci=2):
        p = [int(i*(10**preci)) for i in p]
        start = 0
        for i in range(len(p)):
            p[i] = [start,start+p[i]]
            start = p[i][1]
        seed = randint(1,(10**preci))
        index = 0
        result = ""
        for i in p:
            if seed>i[0] and seed<=i[1]:
                result = l[index]
                break
            index += 1
        return result
    @staticmethod
    def listget(a,f=lambda x:x):
        return [f(i) for i in a]
    @staticmethod
    def removeempty(a):
        return [i for i in a if i]
    @staticmethod
    def read(file):
        with open(file,"r",encoding="utf-8") as f:
            data = f.read()
        return data
    @staticmethod
    def write(file,data):
        with open(file,"w",encoding="utf-8") as f:
            f.write(data)
        return None
    @staticmethod
    def distance(point1,point2):
        return sum(map(lambda p:(p[1]-p[0])**2, zip(point1,point2)))**0.5
    @staticmethod
    def htmlpreproccess(string,*args):
        if "<" in args: string = string.replace("<","&lt;")
        if ">" in args: string = string.replace(">","&gt;")
        if "\n" in args: string = string.replace("\n","<br>")
        return string
    @staticmethod
    def break_point_last_dimension(point, way=lambda a:1/a):
        point_copied = point[:-1]
        weight = way(abs(point[-1])+1)
        return list(map(lambda a:a*weight, point_copied))
    @staticmethod
    def change_point_into_2D_dimension(point, way=lambda a:1/a): #turn position into 2d eyes position so 2d eyes can see
        while len(point)>2:
            point = break_point_last_dimension(point, way)
        return point

Utils.make_attrs_global(Utils)

if __name__=="__main__":
    print(distance([10,3],[4,6]))
