### a和b交集(List,List)
```python
def intersection(a,b):
    c = []
    for i in a:
        if i in b:
            c.append(i)
    return c

result = intersection(["j","y","ele"],["ele","g","j"])
print(result)
```

### a不在b(List,List)
```python
def notIn(a,b):
    c = []
    for i in a:
        if not i in b:
            c.append(i)
    return c

result = notIn(["j","y","ele"],["ele","g","j"])
print(result)
```

### a不重複(List)
```python
def norepeat(a):
    b = []
    for i in a:
        if not i in b:
            b.append(i)
    return b

result = norepeat(["k","lion","b","lemon","lion","m","lemon"])
print(result)
```

### 將文字句子按照順序和相連拆解成所有可能(str,int)
```python
def scan(word,maxLength=None):
    result = []
    for i in range(len(word)): # 0~last index of word
        for j in range(i+1,len(word)+1): # start:i, end:j ->  i+1~last index of word
            result.append(word[i:j])
            if j-i==maxLength: break
    return result

result = scan("你們好啊")
print(result)
```

### 將附近相關且重複的資料刪除，只取左右不重複的資料(List:str)
```python
def reduce(a):
    b = []
    for i,c in enumerate(a):
        left = ""
        right = ""
        if not i==0: left=a[i-1]
        if not i==len(a)-1: right=a[i+1]
        if not (c in left or c in right): b.append(c)
    return b

result = reduce(["1","123","2","23","3","1","123","2","23","3"])
print(result)
```

### 隨機重新排序(List)
```python
from random import randint
def randSort(a):
    b = []
    while len(a)>0:
        c = len(a)
        b.append(a.pop(randint(0,c-1)))
    return b

print(randSort([1,2,3]))
```

### 隨機取出(List)
```python
from random import randint
def randGet(a):
    if len(a)==0: return None
    return a[randint(0,len(a)-1)]

print(randGet(["y","p","6"]))
```

### 產生長度為l，從範圍從s到e的list(int,int,int)
```python
from random import randint
def rl(s,e,l):
    return [randint(s,e) for i in "."*l]

print(rl(0,5,5))
```

### 藉由給定的物件和機率百分比精度回傳最終得到的物件
#### List,List (List:0<=float<=1,List,int)
```python
from random import randint

def Probability(p=[0.1,0.2,0.7],l=[1,2,3],preci=2):
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

print(Probability(p=[0.05,0.05,0.90],l=["a","k","r"],preci=2))
```
#### Dictionary (Dictionary-> ?:0<=float<=1,int)
```python
from random import randint
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

print(Probability({"item1":0.7,"item2":0.1,"item3":0.2},preci=2))
```

### 藉由給定的物件和機率權重回傳最終得到的物件
#### List,List (List:int,List)
```python
from random import randint

def Probability(p=[1,2,7],l=[1,2,3]):
    #1 2 3 4 5 6 7 8 9 10...
    total = sum(p)
    start = 0
    for i in range(len(p)):
        p[i] = [start,start+p[i]]
        start = p[i][1]
    seed = randint(1,total)
    result = ""
    for i in range(len(p)):
        if seed>p[i][0] and seed<=p[i][1]:
            result = l[i]
            break
    return result

print(Probability([1,1,3],["t","q","y"]))
```
#### Dictionary (Dictionary->?:int)
```python
from random import randint
def Probability(dic={"item1":1,"item2":2,"item3":7}):
    p = list(dic.values())
    l = list(dic.keys())
    total = sum(p)
    start = 0
    for i in range(len(p)):
        p[i] = [start,start+p[i]]
        start = p[i][1]
    seed = randint(1,total)
    result = ""
    for i in range(len(p)):
        if seed>p[i][0] and seed<=p[i][1]:
            result = l[i]
            break
    return result

print(Probability({"t":1,"q":1,"y":3}))
```

### 隨機數 (精確度取決於系統)
##### https://github.com/wayne931121/random/blob/main/randint.py
```python
import time

def random(start,end,dpv=1): #end>start, dpv!=0
    cal = end-start+1
    result = start+round(time.time()*cal*dpv)%cal
    return result

print(random(0,10))
```

### 兩點座標間的距離
```python
def distance(point1,point2):
    return sum(map(lambda p:(p[1]-p[0])**2, zip(point1,point2)))**0.5

#         x y z a b c ...
point1 = [0,0,0,0,0,0]
point2 = [3,4,0,0,0,0]
print(distance(point1,point2))
```

### 座標降維處理
```python
def break_point_last_dimension(point, way=lambda a:1/a):
    point_copied = point[:-1]
    weight = way(abs(point[-1])+1)
    return list(map(lambda a:a*weight, point_copied))

def change_point_into_2D_dimension(point, way=lambda a:1/a): #turn position into 2d eyes position so 2d eyes can see
    while len(point)>2:
        point = break_point_last_dimension(point, way)
    return point

#         x y z a b c ...
point3 = [3,4,0,0,9,0]

print(change_point_into_2D_dimension(point3))
```

### 移除空白數據(移除```None, "", False, 0```)
```python
def removeempty(a):
    return [i for i in a if i]

print(removeempty([5 , 4, False, None, "", 0, 1, 2]))
print(removeempty([5 , 6, None, None, 10, 12, 72]))
```

### 變化量 Delta (在一個函數下從a到b的對應值變化量)
```python
def delta__(f, a, b):
    return f(b)-f(a)

print(delta__(lambda a:a**2, 6, 9))
```

### 變化率 rate of change (在一個函數下從a到b的對應值變化量除以a到b的變化量)
```python
def delta_(f,a,b):
    return delta__(f,a,b)/abs(delta__(lambda a:a, a, b))

print(delta_(lambda a:a**2, 6, 9))
```

### 瞬間變化率 instantaneous rate of change aka Derivative (在一個函數下n0是無限接近n或n並且n1是無限接近n或n且n0不等於n1，取n0到n1的變化率)
```python
import decimal

def delta(f,n,mode=None,preci=10**7):
    decimal.getcontext().prec = preci
    preci = decimal.Decimal(1)/decimal.Decimal(preci)
    n = decimal.Decimal(n)
    result = 0
    if mode=="small to original":
        
        result = delta_(f,n-preci,n)
        
    elif mode=="original to big":
        
        result = delta_(f,n,n+preci)
        
    elif mode=="small to big":
        
        result  = delta_(f,n-preci,n+preci)
        
    elif mode=="original to small":
        
        result = delta_(f,n,n-preci)
        
    elif mode=="big to original":
        
        result = delta_(f,n+preci,n)
        
    elif mode=="big to small":
        
        result = delta_(f,n+preci,n-preci)
        
    else:
        # small to original
        result = delta_(f,n-preci,n)
        
    return float(result)

print(delta(lambda a:a**2, 6))
```
