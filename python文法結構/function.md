# Python中的Function，函數、功能

## 使用時機
如果你需要執行一個重複的程式碼、重複的函數，你不會希望再打一次那些程式碼，特別是在那些程式碼特別常特別複雜或是需要重複條用多次的情況下。
當然你也可以使用迴圈，但是那是連續執行相同程式碼的情況下，如果是不連續的執行就一定要用函數。

## 文法

```python
def function_name(*args, **kargs): return value
```

## 簡單來說
這是一個簡單的函數

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
10 AA AAA
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
