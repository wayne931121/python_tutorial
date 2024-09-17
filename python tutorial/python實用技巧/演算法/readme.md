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

### 將文字句子按照順序和相連拆解成所有可能
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
