# Python中的Loop，迴圈(以及遞歸函數介紹Recursion)

## 使用時機
連續執行相同程式碼的情況下，就需要使用迴圈。

## 文法

### For迴圈

```python
for i in iterObject: doSomething
```

### While迴圈

```python
while condition: doSomething
```

### 遞歸函數

```python
def myFunction(*args, **kargs):
    if condition:
        myFunction(*args, **kargs)
```

## For迴圈

```python
for i in 可遍歷物件: 做一些事情
```

舉例來說:

```python
for i in range(6):
    print(i)
```

range(6)可理解為做6次，也可理解成從\[0-6(不包含)\]，不包含尾巴也就是\[0-5\]從0到5做一些事情。
range(start, end, space)也就是從start開始到end(不包含)每次間隔space做一些事情，總共做絕對值end-start次。

```python
Input:
list(range(6))
Output:
[0, 1, 2, 3, 4, 5]

Input:
list(range(2, 9))
Output:
[2, 3, 4, 5, 6, 7, 8]

Input:
list(range())
Output:
[0, 1, 2, 3, 4, 5]
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
