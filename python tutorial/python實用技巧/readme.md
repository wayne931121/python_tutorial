### dir
函數dir可以得到物件能用的參數和函數及各個子項目，像是在以下範例中，`dir(a)`中可以看見`conjugate`，代表`a.conjugate`是存在的，`print(a.conjugate)`可得到`<built-in method conjugate of int object at 0x0000024807C300F0>`，這代表他是一個函數，可以執行。
```python
a = 1
print(dir(a))
```

### print
sep是分隔參數使用，預設為```" "```。end是結尾使用，預設為```"\n"```換行符號。
```python
print(1,2,3,sep="Hello")
print(1,2,3,sep="Hello",end="")
print(1,2,3,sep="Hello",end="")
```

#### Flash Print
```"\r"```是回車符，讓游標能回到當前這一行的起點，從而實現不換行，同一行一直刷新的效果。
```python
import time
print("\r",1,sep="",end="")
time.sleep(1)
print("\r",2,sep="",end="")
time.sleep(1)
print("\r",3,sep="",end="")
```

### Search
#### 使用python在資料中尋找含有特定文字的資料
```python
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

a = "1"
result = search("la","ya",mode="or",List=dir(a))
print(result)

result = search("bal","k",mode="or",List=["air","air ball","ball"])
print(result)
```

#### 使用Jupyter Notebook顯示尋找完的資料
```python
from IPython.display import display, HTML
def idisplay(result,color="#ccffff"):
    for i in result:
        display(HTML('<pre style="background-color: %s;">%s</pre><br>'%(color,i.replace("<","&lt;").replace(">","&gt;"))))
result = search("la","ya",mode="or",List=dir(a))
idisplay(result)
```
#### 搜尋尋找對應的值藉由給定邏輯、目標和陣列
```python
def findtl(target,lis,compare=lambda x:x,activate=lambda a,b:a==b):
    res = []
    for n,i in enumerate(lis):
        e = compare(i)
        if activate(target,e):
            return n,i
def searchtl(target,lis,compare=lambda x:x,activate=lambda a,b:a==b):
    res = []
    for n,i in enumerate(lis):
        e = compare(i)
        if activate(target,e):
            res.append([n,i])
    return res

print(findtl(1,[2,3,1,5,1,5]))
print(searchtl(1,[2,3,1,5,1,5]))
print()
a,b = 'w',[[['w'], '12'], [['n','o'], '青菜'], [['w'], '3']]
print(findtl(a,b,compare=lambda x:x[0], activate=lambda a,b:a in b))
print(searchtl(a,b,compare=lambda x:x[0], activate=lambda a,b:a in b))
```
#### 回傳值陣列藉由給定陣列和陣列項目操作(類似map，但參數順序不同並且直接回傳list)
```python
def listget(a,f=lambda x:x):
    return [f(i) for i in a]

print(listget([[1,2],[2,5]],lambda x:x[1]))
```

#### 將Class內的所有子項目設定到全域變數內
```python
# Be careful to use this function, if you don't understand this, don't use this, only use import keyword.
def make_attrs_global(obj, global_, skip=0, cover=0, message=""):
    #https://stackoverflow.com/questions/30098037/call-function-from-class-without-declaring-name-object?rq=3
    #https://stackoverflow.com/a/30098651/19470749
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
```
```python
class Say:
    thisIs365 = 365
    @staticmethod
    def hello():
        print("HELLO")
    @staticmethod
    def goodbye():
        print("GoodBye")
    @staticmethod
    def what():
        print("WHAT")

make_attrs_global(Say, globals())

print()
hello()
goodbye()
what()
print()

make_attrs_global(Say, globals(), skip=1, message="main.py -> ")

print()
hello()
goodbye()
what()
print()

make_attrs_global(Say, globals(), cover=1)

print()
hello()
goodbye()
what()
print()
```
