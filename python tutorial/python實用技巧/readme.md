### dir
函數dir可以得到物件能用的參數和函數及各個子項目，像是在以下範例中，`dir(a)`中可以看見`conjugate`，代表`a.conjugate`是存在的，`print(a.conjugate)`可得到`<built-in method conjugate of int object at 0x0000024807C300F0>`，這代表他是一個函數，可以執行。
```python
a = 1
print(dir(a))
```

#### search
使用python在資料中尋找含有特定文字的資料
```python
def UL(w): #不分大小寫
    if len(w)>11:
        print("Warning your key word is too big, will take long time to process, you can try to split it to small word and resent")
    word = [""]
    for e in w:
        for i in range(len(word)):
            word.append(word[i]+e.lower())
            word.append(word[i]+e.upper())
    return word[-(2**len(w)):]

def search(*words,List=[],mode="and"):
    words = [UL(i) for i in words]
    for token in List:
        flag = 0
        for word in words: #從所有關鍵字尋找
            for keyWord in word: #關鍵字不分大小寫
                if keyWord in token: 
                    flag+=1 #找到
                    break
        if mode=="and" and flag==len(words): #全部找到
            print(token)
        elif mode=="or" and flag>0: #有找到
            print(token)

a = "1"
search("la",mode="or",List=dir(a))
search("bal","k",mode="or",List=["air","air ball","ball"])
```
