# Python中的Function，函數、功能

## 使用時機
如果你需要執行一個重複的程式碼、重複的函數，那麼你不會希望再打一次那些程式碼，特別是在那些程式碼特別常特別複雜或是需要重複條用多次的情況下。
當然你也可以使用迴圈，但是那是連續執行相同程式碼的情況下，如果是不連續的執行就一定要用函數。

## 文法

```python
def function_name(*args, **kargs): return value
```

## 簡單來說

```python
def 函數名稱(參數): return 回傳值
```

### 這是一個簡單的函數

```python
def function():
    print(1)
```

呼叫使用他

```python
function()
```
```
Output:
1
```

不同參數要使用","分開

```python
def function(arg1, arg2, arg3):
    print(arg1*10, arg2, arg3)
function(10, "AA", "AAA")
```
```
Output:
100 AA AAA
```

再一個舉例

```python
def MyFunction(a, m):
    print(a*2+m)
MyFunction(10, 5)
```
```
Output:
25
```

### 參數的預設值
您可以預設參數的值(非必要參數，不傳值也可以，因為有預設值。)

```python
def MyFunction(a=10, m=5):
    print(a*2+m)
    
MyFunction()
MyFunction(20)
MyFunction(20, 30)
```
```
Output:
25
45
70
```

非必要參數一定要放在必要參數的後面

```python
def MyFunction(a, m=5):
    print(a*2+m)
```
```
Output:
```

```python
def MyFunction(m=5, a):
    print(a*2+m)
```
```
Output:
SyntaxError: non-default argument follows default argument
```
### 函數的回傳值
函數預設的回傳值為None

```python
def a():
    pass

a()
```
```
Output:
```

```python
def a():
    pass

print(a())
```
```
Output:
None
```

指定回傳值
```python
def a():
    return 1

a()
```
```
Output:
1
```

將變數賦予回傳值(紀錄回傳值)

```python
def a():
    return 1

b = a()
print(b)
```
```
Output:
1
```

再一個舉例

```python
def hi(words):
    w1 = list(words)
    w1[0] = words[-1]
    w1[-1] = words[0]
    words = "".join(w1).upper()
    return words

b = hi("Hello MyFriends")
print(b)
```
```
Output:
SELLO MYFRIENDH
```

### 使用未知長度的參數
如果您不知道參數的長度

```python
def hi(*words):
    return words

b = hi("a", [636, 888], {"A":1})
print(len(b))
print(b, end="\n\n")
for i in b:
    print(i)
```
```python
Output:
3
('a', [636, 888], {'A': 1})

a
[636, 888]
{'A': 1}
```

```python
def hi(**words):
    return words

b = hi(w="a", c=[636, 888], g={"A":1})
print(b, end="\n\n")
for i in b.keys():
    print(i)

for i in b.items():
    print(i)
```
```python
Output:
{'w': 'a', 'c': [636, 888], 'g': {'A': 1}}

w
c
g
('w', 'a')
('c', [636, 888])
('g', {'A': 1})
```
