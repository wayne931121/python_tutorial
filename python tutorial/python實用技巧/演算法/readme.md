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
