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
```python
Output:
0
1
2
3
4
5
```

`range(6)`可理解為做6次，也可理解成從\[0-6(不包含)\]，不包含尾巴也就是\[0-5\]從0到5做一些事情。

`range(start, end, space)`也就是從start開始到end(不包含)每次間隔space做一些事情，總共做絕對值end-start次。(預設start為0，可以只傳end如`range(9)`。預設space間隔為1，可以只傳start和end如`range(4,9)`。)

```python
Input:
list(range(6))

Output:
[0, 1, 2, 3, 4, 5]
```

```python
Input:
list(range(2, 9))

Output:
[2, 3, 4, 5, 6, 7, 8]
```

```python
Input:
list(range(3,10,2))

Output:
[3, 5, 7, 9]
```

其他示例:

```python
Input:
for i in ["a", "b", "c"]:
    print(i)

Output:
a
b
c

Input:
for i in {"t":0, 3:"G", "L39":print}.items():
    print(i[0], ":", i[1])

Output:
t : 0
3 : G
L39 : <built-in function print>
```

```python
Input:
for i in "KK__\nGHYYK536DD?!\'\"^^)++":
    print(i)

Output:
K
K
_
_


G
H
Y
Y
K
5
3
6
D
D
?
!
'
"
^
^
)
+
+
```

### While迴圈

```python
while 狀況(True or False): 做一些事情
```

```python
Input:
i = 0
while i<10:
    print(i)
    i += 1

Output:
0
1
2
3
4
5
6
7
8
9
```

將物件轉換為可遍歷物件`iter(object)`，並且用next呼叫，結束時拋出StopIteration錯誤。(如果您今天處理的是一些其他模組的可遍歷物件，
並且您不知道如何存取可遍歷物件中的物件僅知道可以使用for迴圈讀取，而您不想使用for迴圈或是想使用分次不連續呼叫即可使用`iter`。)

```python
Input:
a = {0:5, 1:7, 3:5}
a = iter(a.items())
try:
    while 1:
        print(next(a))
except StopIteration:
    pass

Output:
(0, 5)
(1, 7)
(3, 5)
```

```python
Input:
a = "GGB"
a = iter(a)
try:
    while 1:
        print(next(a))
except StopIteration:
    pass

Output:
G
G
B
```
### 遞歸函數
透過在函數內重新呼叫自身函數形成迴圈，這種方式會比迴圈還慢且更消耗記憶體，但是可能能寫得更淺顯易懂。
```python
Input:
def sum_i0(i, min_limit):
    if i>min_limit:
        return i+sum_i0(i-1, min_limit)
    return i

sum_i0(100, 0)

Output:
5050 #100+99+98+97......+2+1+0 = (100+0)*101/2 = 5050
```

```python
Input:
def sum_i1(i, max_limit):
    if i<max_limit:
        return i+sum_i1(i+1, max_limit)
    return i

sum_i1(0, 100)

Output:
5050 #0+1+2+3+4+5+6......+99+100 = (100+0)*101/2 = 5050
```

```python
Input:
def CustomSum(i, min_limit, table={}):
    if i>min_limit:
        r = CustomSum(i-1, min_limit, table) #先前加好的值
        table["now_value"] = i*table["now_value"]
        return r+table["now_value"]
    table["now_value"] = i
    return i

CustomSum(10, 1)
CustomSum(100, 1)

Output:
4037913
94269001683709979260859834124473539872070722613982672442938359305624678223479506023400294093599136466986609124347432647622826870038220556442336528920420940313

"""
Why does this happen:
CustomSum(5, 1):
table = {}
5>1:
    r = CustomSum(4, 1, table)
        4>1:
            r = CustomSum(3, 1, table)
                3>1:
                    r = CustomSum(2, 1, table)
                        2>1:
                            r = CustomSum(1, 1, table)
                                1>1:False
                                table["now_value"] = 1 ------|這次的table["now_value"]會造就下一次table["now_value"]的其中一個乘數。
                                return 1 --->----------------↓----|這次的return值會造就下一次return的其中一個加數。
                            table["now_value"] = 2*1  <--- 2*1    ↓
                            return 1+2    ⇨ (1)+(2*1)      <----- 1+2
                    table["now_value"] = 3*2    ⇨ 3*2*1
                    return 3+6    ⇨ (1+2*1)+(3*2*1)
            table["now_value"] = 4*6    ⇨ 4*3*2*1
            return 9+24    ⇨ (1 +2*1+3*2*1)+(4*3*2*1)
    table["now_value"] = 5*24 ⇨ 5*4*3*2*1
    return 33+120 ⇨ ( 1 + 2*1 + 3*2*1 + 4*3*2*1 + 5*4*3*2*1 )
"""
```
