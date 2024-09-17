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
