### dir
函數dir可以得到物件能用的參數和函數及各個子項目，像是在以下範例中，dir(a)中可以看見conjugate，代表a.conjugate是存在的，print(a.conjugate)可得到<built-in method conjugate of int object at 0x0000024807C300F0>，這代表他是一個函數，可以執行。
```python
a = 1
print(dir(a))
```

#### search
使用python在資料中尋找含有特定文字的資料
```python
def search(word,List):
    for token in List:
        if (word in token) or (word.lower() in token) or (word.upper() in token):
            print(token)

a = "Hi"
search("la",dir(a))
search("ball",["air","air ball","ball"])
```
