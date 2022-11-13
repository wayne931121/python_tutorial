# Python教學

# 目錄
[Python是什麼](#Python是什麼)

[如何學習Python](#如何學習Python)

[Python能做什麼](#Python能做什麼)

[Python實用模組及功能](#Python實用模組及功能)

[Python編碼解碼支援格式](#Python編碼解碼支援格式)

[Python文法結構](#Python文法結構)

[Python資料型態](#Python資料型態)

[Python運算子](#Python運算子)

[Python內建函數](#Python內建函數)

# Python是什麼?
Python是個高階語言，使用直譯器。Python的優勢是簡單明瞭能輕鬆開發APP，劣勢是執行速度過慢。(直譯器是邊翻譯邊執行，如Javascript語言; 編譯器是編譯完後再執行，如C語言)<br>
Python官方網站，含下載、文檔、關於頁面:<br>
[https://www.python.org/](https://www.python.org/)

Python官方文檔<br>
[https://docs.python.org/3/](https://docs.python.org/3/)

Python官方模組<br>
[https://docs.python.org/3/library/index.html](https://docs.python.org/3/library/index.html)

想下載Python和編輯Python檔案可看這裡<br>
[https://github.com/wayne931121/python_tutorial/blob/main/安裝Python.md](https://github.com/wayne931121/python_tutorial/blob/main/安裝Python.md)

## 如何學習Python
到W3school學習入門文法(右上角地球符號能用Google翻譯調整語言)<br>
[https://www.w3schools.com/python/](https://www.w3schools.com/python/)

到Python官方文檔教學頁面學習入門文法(左上角能調整語言)<br>
[https://docs.python.org/3/tutorial/index.html](https://docs.python.org/3/tutorial/index.html)

## Python能做什麼?
Python有很多別人寫好的模組和強大的內建模組，可以做很多事，有些模組跑很快因為他用C寫，在Python內運作。

Python可以用PyScript在瀏覽器內運作，詳情見此:<br>
https://pyscript.net/

## Python實用模組及功能

### 網路:
讀取網頁、開網頁伺服器、發送封包、接收封包

#### [Socket 內建](https://docs.python.org/3/library/socket.html)
客戶端、伺服器端、底層應用。<br>
客戶端，爬蟲、嗅探使用，向伺服器寄出請求，並取得回應，像是網頁原始碼。<br>
伺服器端，開伺服器等待用戶連接並做出相應行動。

#### [SSL 內建](https://docs.python.org/3/library/ssl.html)
客戶端、伺服器端、底層應用。<br>
wrap socket with ssl.包裝ssl到socket上，如讓http變成https。

#### [IpAddress內建](https://docs.python.org/3/library/ipaddress.html)
底層應用。<br>
處理IP字符串

#### [Http 內建](https://docs.python.org/3/library/http.html)
Http客戶端、伺服器端。

#### [Ftplib 內建](https://docs.python.org/3/library/ftplib.html)
Ftp客戶端。

#### [Urllib 內建](https://docs.python.org/3/library/urllib.html)
客戶端<br>
爬蟲、抓包使用，向網路寄出請求，並取得回應，像是網頁原始碼。

#### [Request](https://requests.readthedocs.io/en/latest/)
客戶端<br>
爬蟲、抓包使用，向網路寄出請求，並取得回應，像是網頁原始碼。

#### [Flask](https://flask.palletsprojects.com/en/2.2.x/)
伺服器端<br>
網頁伺服器，開伺服器等待用戶連接並做出相應行動。

#### [Django](https://www.djangoproject.com/)
伺服器端<br>
網頁伺服器，伺服器框架，開伺服器等待用戶連接並做出相應行動。

#### [Jinja](https://github.com/pallets/jinja/)
伺服器端<br>
網頁伺服器，伺服器框架，開伺服器等待用戶連接並做出相應行動。

#### [Scapy](https://scapy.net/)
實用工具<br>
嗅探工具、封包收發測試、網路攻擊工具、偽裝IP工具、網域測試。

#### [IDNa](https://github.com/kjd/idna)
底層應用，字符串處理。<br>
國際域名轉換。

#### [Aiohttp、Aiodns](https://docs.aiohttp.org/)
客戶端<br>
非同步網頁讀取，使用async。

#### [Pycares](https://github.com/saghul/pycares)
客戶端<br>
DNS掃描。

#### [Grequests](https://github.com/spyoungtech/grequests)
客戶端<br>
非同步網頁讀取，使用gevent。

### 抓包處理
#### 將抓到的封包、原始碼進行處理，通常搭配request模組使用。
#### [Lxml](https://lxml.de/)<br>
#### [Beatifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)
#### [JSON 內建](https://docs.python.org/3/library/json.html)

### 控制瀏覽器
爬蟲的一種
#### [Selenium](https://selenium-python.readthedocs.io/)<hr>

### 編輯任何檔案
#### Python內建函數Open

### 音樂標頭編輯(MP3 ID3 Metadata)
#### [Eyed3](https://eyed3.readthedocs.io/en/latest/eyed3.html)

### 照片、影片編輯，串流讀取
#### [OpenCV[站內教學]](https://github.com/wayne931121/python_tutorial/blob/main/python%20tutorial/python%E6%A8%A1%E7%B5%84/opencv.md)
#### [Pillow](https://pillow.readthedocs.io/)
#### [Moviepy](https://zulko.github.io/moviepy/)

### CSV編輯
#### [CSV 內建](https://docs.python.org/3/library/csv.html)

### JSON編輯
#### [JSON 內建](https://docs.python.org/3/library/json.html)

### Excel編輯
#### [OpenPyXl](https://openpyxl.readthedocs.io/)

### WAV編輯
#### [Wave(.wav) 內建](https://docs.python.org/3/library/wave.html)
#### [PyAudio](https://pypi.org/project/PyAudio/)

### TOML讀取
#### [TOMLLIB 內建](https://docs.python.org/3/library/tomllib.html)
<hr>

### 人工智慧、大數據分析、機器學習
#### [Tensorflow](https://www.tensorflow.org/)
#### [Pytorch](https://pytorch.org/)
#### [Scikit-Learn](https://scikit-learn.org/)
#### [Keras](https://keras.io/)
#### [MediaPipe (人臉辨識)](https://google.github.io/mediapipe/getting_started/python.html)
#### [XGboost](https://xgboost.readthedocs.io/)
#### [PyCaret (機器學習)](https://pycaret.org/)
#### [Jina (雲端人工智慧)](https://docs.jina.ai/)
#### H5檔案讀取
##### [H5PY](https://docs.h5py.org/)

### 陣列、數學與矩陣運算
#### [Math 內建](https://docs.python.org/3/library/math.html)
#### [Numpy](https://numpy.org/)
#### [Scipy](https://scipy.org/)

### 資料圖形化
#### [Matplotlib](https://matplotlib.org/)

### 資料分析
#### [Pandas](https://pandas.pydata.org/)
#### [Pandas支援格式: csv, excel, xml...](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html)

### 人類語言分析(自然語言處理，人工智慧的分支，[維基百科介紹](https://zh.wikipedia.org/zh-tw/%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E5%A4%84%E7%90%86))
#### [NLTK](https://www.nltk.org/)
#### [JieBa (中文斷句處理)](https://github.com/fxsjy/jieba)
<hr>

### 時間
#### [Time 內建(取得當前時間、計算時間差、程式休息幾秒鐘。)](https://docs.python.org/3/library/time.html)
#### [Datetime 內建(取得當前年月日期時間。)](https://docs.python.org/3/library/datetime.html)
#### [Timeit 內建(測試程式運作時間)](https://docs.python.org/3/library/timeit.html)

### 系統(系統資訊、程式資訊、檔案操作、標準輸入輸出...)
#### [os 內建(系統資訊、程式資訊、檔案操作、標準輸入輸出...)](https://docs.python.org/3/library/os.html)
#### [sys 內建(系統資訊、程式資訊、檔案操作、標準輸入輸出...)](https://docs.python.org/3/library/sys.html)
#### [signal 內建(接收信號並處理，如接收Ctrl+C訊號，通常在迴圈內使用。)](https://docs.python.org/3/library/signal.html)
#### [subprocess 內建(調用命令列命令並取得結果。)](https://docs.python.org/3/library/subprocess.html)
#### [shlex 內建(解析文字Unix shell命令或生成安全命令。)](https://docs.python.org/3/library/shlex.html)
#### [io 內建(輸入輸出)](https://docs.python.org/3/library/io.html)
#### [argparse 內建(使用者參數處理)](https://docs.python.org/3/library/argparse.html)
#### [platform 內建(系統資訊)](https://docs.python.org/3/library/platform.html)
#### [logging 內建(日誌設定)](https://docs.python.org/3/library/logging.html)
#### [tempfile 內建(暫存檔案)](https://docs.python.org/3/library/tempfile.html)
#### [pathlib 內建(檔案系統路徑處理)](https://docs.python.org/3/library/pathlib.html)
#### [gc 內建(清理運行中不必要的記憶體)](https://docs.python.org/3/library/gc.html)
#### [traceback 內建(在try except的except中追蹤錯誤的來源行數)](https://docs.python.org/3/library/traceback.html)
#### [functools 內建(高階函數和裝飾器用法)](https://docs.python.org/3/library/functools.html)

### 進程、線程
#### [threading 內建(多線程)](https://docs.python.org/3/library/threading.html)
#### [multiprocessing 內建(多進程)](https://docs.python.org/3/library/multiprocessing.html)
#### [concurrent.futures 內建(高階異步線程進程控制接口)](https://docs.python.org/3/library/concurrent.futures.html)

### Async、Coroutine
#### [asyncio 內建(非同步io處理)](https://docs.python.org/3/library/asyncio.html)
#### [gevent (Coroutine)](https://github.com/gevent/gevent)

### 壓縮編碼解碼
#### [zipfile 內建(zip)](https://docs.python.org/3/library/zipfile.html)
#### [tarfile 內建(tar)](https://docs.python.org/3/library/tarfile.html)
#### [zlib 內建(gzip、deflate)，網路資料壓縮格式](https://docs.python.org/3/library/zlib.html)
#### [gzip 內建，網路資料壓縮格式](https://docs.python.org/3/library/gzip.html)
#### [brotli (br)，網路資料壓縮格式](https://python-hyper.org/projects/brotlipy/en/latest/)
#### [lzma 內建(lzma)](https://docs.python.org/3/library/lzma.html)
#### [bz2 內建(bz2)](https://docs.python.org/3/library/bz2.html)

### 字元編碼識別
#### [chardet](https://github.com/chardet/chardet)
#### [cchardet](https://github.com/PyYoshi/cChardet)
#### [uchardet(C語言)](https://github.com/freedesktop/uchardet)

### C函數使用
#### [ctypes 內建](https://docs.python.org/3/library/ctypes.html)

### Python變數儲存
#### [pickle(.pkl) 內建](https://docs.python.org/3/library/pickle.html)

### 加密解密
#### [Itsdangerous](https://itsdangerous.palletsprojects.com/)
#### [pyOpenSSL](https://www.pyopenssl.org/)
#### [RSA](https://stuvel.eu/python-rsa-doc/)
#### [PyCrypto](https://www.pycrypto.org/)
#### [Cryptography](https://cryptography.io/)
#### [PyCryptodome](https://www.pycryptodome.org/)

### 快取工具
#### [cachetools](https://github.com/tkem/cachetools)

### MIMETYPE處理
#### [mimetypes 內建](https://docs.python.org/3/library/mimetypes.html)

### Google Api
#### [google-api-core](https://github.com/googleapis/python-api-core)

### 更輕鬆地寫出class
#### [attrs](https://www.attrs.org/)

### 顏色轉換(例如 rgb to hsl)
#### [colorsys 內建](https://docs.python.org/3/library/colorsys.html)

### 字符串處理、檢查、正規表達式
#### [re 內建(regex)](https://docs.python.org/3/library/re.html)
#### [string 內建](https://docs.python.org/3/library/string.html)
#### [inspect 內建](https://docs.python.org/3/library/inspect.html)

### 視覺化界面
#### [Thinker 內建(GUI圖形使用者介面，寫應用程式使用。)](https://docs.python.org/3/library/tkinter.html)
#### [Turtle 內建(畫畫用的)](https://docs.python.org/3/library/turtle.html)
#### [Kivy (寫應用程式使用，支援Android，iOS，Linux，OS X和Windows，使用SDL庫。)](https://kivy.org/)
#### [Pygame (寫遊戲使用，使用SDL庫, Simple DirectMedia Layer。)](https://www.pygame.org/)
#### [PySimpleGUI (GUI)](https://www.pysimplegui.org/)
#### [PyGTK (Gtk+的圖形使用介面庫 PyGObject)](https://pygobject.readthedocs.io/en/latest/index.html)
#### [Pyglet (多媒體遊戲庫。)](https://pyglet.org/)
#### [PySide (圖形使用介面框架Qt的Python版本。)](https://doc.qt.io/qtforpython/index.html)
#### [PyQt (圖形使用介面框架)](https://www.riverbankcomputing.com/software/pyqt/)
#### [Cocos2d (寫遊戲使用，使用Pyglet庫。)](https://github.com/los-cocos/cocos)
#### [Wxpython (GUI工具包)](https://wxpython.org/)

### 打包成exe檔
#### [PyInstaller](https://pyinstaller.org/)

### 運作Javascript
#### [Js2Py](https://github.com/PiotrDabkowski/Js2Py)
#### [STPyV8](https://github.com/cloudflare/stpyv8)

### Windows Api(如windows檔案管理、控制Excel、訊息對話框)
#### [PyWin32](https://github.com/wayne931121/python_tutorial/blob/main/python%20tutorial/python%E6%A8%A1%E7%B5%84/pywin32.md)

## 加速Python的幾種方法
### 1. 改善程式結構
### 2. 將遞歸函數改成迴圈
### 3. 使用cpython或pypy

## Python編碼解碼支援格式
### [https://docs.python.org/3/library/codecs.html](https://docs.python.org/3/library/codecs.html)
### [Base64編碼解碼(內建)](https://docs.python.org/3/library/base64.html)

## Python文法結構

### 函數

```python
def function_name(*args, **kargs): return value
```

[詳細資料](https://github.com/wayne931121/python_tutorial/blob/main/python%20tutorial/python%E6%96%87%E6%B3%95%E7%B5%90%E6%A7%8B/function.md)


### 迴圈

```python
for i in iterObject: doSomething
while flag: doSomething
```

[詳細資料](https://github.com/wayne931121/python_tutorial/blob/main/python%20tutorial/python%E6%96%87%E6%B3%95%E7%B5%90%E6%A7%8B/loop.md)

### 物件

```python
class object_name(parent):
    pass
```

### 如果...做

```python
if flag: #如果flag是True則做...
  doSomthing
elif flag1: #又或者如果flag1是True則做...
  doSomthing
else:  #又或者則做...
  doSomthing
```

### 嘗試...捕捉錯誤

```python
try
  doSomthing
except Exception as e: #將預期到的錯誤視為e
  doSomthing
finally:  #到最後，無論如何都要做...
  doSomthing
```

### 刪除

```python
del variable_name
```

## Python資料型態
### str -> string 字符串 "文字"
### int -> integer 整數  1
### list -> list 清單(類似陣列，但內容物型態不限) ["文字",1,...]
### tuple -> tuple 類似list，但只讀不能更改 ("文字",1,...)
### dict -> dictionary 字典(查表用) {"魚":fish,...}
### float -> float 浮點數(小數) 1.111
### bytes -> bytes 原始數據(只讀r) b'\xe6\x88\x91\xe6\x84\x9b\xe4\xbd\xa0'
### bytearray -> bytearray 原始數據陣列(讀寫rw) bytearray(b'\xe6\x88\x91\xe6\x84\x9b\xe4\xbd\xa0')
### bool -> boolean 布林值(True or False)

<details><summary>展開示例</summary>

```cmd
>>> a = "text"
>>> type(a)
<class 'str'>
>>>
>>> a[0]
't'
>>> a[1]
'e'
>>> a[-1]
't'
>>> a[0]="Y"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
>>> a = list(a)
>>> a
['t', 'e', 'x', 't']
>>> a[0]
't'
>>> a[1]
'e'
>>> a[-1]
't'
>>> a[0:2]
['t', 'e']
>>> a[0]="Y"
>>> a
['Y', 'e', 'x', 't']
>>> a[0]
'Y'
>>> "".join(a)
'Yext'
>>> "HEY".join(a)
'YHEYeHEYxHEYt'
>>> ".".join(a)
'Y.e.x.t'
>>> a = "".join(a)
>>> a
'Yext'
```
```cmd
>>> a = 1
>>> type(1)
<class 'int'>
>>> a + 1
2
>>> a
1
>>> a = a+1
>>> a
2
>>> a += 10
>>> a
12
>>>
```

```cmd
>>################# Tuple #################
>>> (0,1,2)
(0, 1, 2)
>>> type((0,1,2))
<class 'tuple'>
>>> (0,1,2)[0]
0
>>> a = (0,1,2)
>>> a[0]
0
>>> a[0]=5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>############### List ####################
>>> a = [0,1,2]
>>> a
[0, 1, 2]
>>> a[0]
0
>>> a[0]=5
>>> a
[5, 1, 2]
>>> type([0,1,2])
<class 'list'>
>>> type(a)
<class 'list'>
>>>
```

```cmd
>>> {"TT":1, 0:"OO", True: print}
{'TT': 1, 0: 'OO', True: <built-in function print>}
>>> type({"TT":1, 0:"OO", True: print})
<class 'dict'>
>>> {"TT":1, 0:"OO", True: print}[True]
<built-in function print>
>>> {"TT":1, 0:"OO", True: print}[True]("123")
123
>>> {"TT":1, 0:"OO", True: print}[0]
'OO'
>>> {"TT":1, 0:"OO", True: print}["TT"]
1
```

```cmd
>>> type(135.54)
<class 'float'>
```

```cmd
>>> bytes("YY牛Z", encoding="utf-8")
b'YY\xe7\x89\x9bZ'

>>> b"123"
b'123'

>>> type(b"123")
<class 'bytes'>
```

```cmd
>>> bytearray("YY牛Z", encoding="utf-8")
bytearray(b'YY\xe7\x89\x9bZ')

>>> bytearray(b'YY\xe7\x89\x9bZ')
bytearray(b'YY\xe7\x89\x9bZ')

>>> type(bytearray(b'YY\xe7\x89\x9bZ'))
<class 'bytearray'>
```
```cmd
>>> True
True
>>> False
False
>>> type(True)
<class 'bool'>
>>> a = False
>>> type(a)
<class 'bool'>
>>>
```

</details>

## Python運算子
## [https://www.w3schools.com/python/python_operators.asp](https://www.w3schools.com/python/python_operators.asp)

### 假設x=2, y=7
### Python算術運算子(Arithmetic Operators)
#### \+ ⇨ 加 x+y=2+7=9
#### \- ⇨ 減 x-y=2-7=-5
#### \* ⇨ 乘 x\*y=2\*7=14
#### / ⇨ 除 x/y=2/7=0.2857142857142857
#### // ⇨ 除完取整數(商) x//y=2//7=0
#### \% ⇨ 除完取餘數 x%y=2%7=2
#### \*\* ⇨ 次方 x\*\*y=2\*\*7=2\*2\*2\*2\*2\*2\*2=128

### Python指定運算子(Assignment Operators)
| 運算子  | 示例      | 相當於     | 結果     |
| --------- | ----------- | ---------- | -------- |
| =       | x=2       | x=2        | x=2      |
| +=      | x+=10     | x=x+10     | x=12     |
| -=      | x-=10     | x=x-10     | x=-8     |
| \*=     | x\*=10    | x=x\*10    | x=20     |
| /=      | x/=10     | x=x/10     | x=0.2    |
| //=     | x//=10    | x=x//10    | x=0      |
| %=      | x%=10     | x=x%10     | x=2      |
| \*\*=   | x\*\*=10  | x=x\*\*10  | x=1024   |
| &=      | x&=10     | x=x&10     | x=2      |
| \|=     | x\|=10    | x=x\|10    | x=10     |
| ^=      | x^=10     | x=x^10     | x=8      |
| >>=     | x>>=10    | x=x>>10    | x=0      |
| <<=     | x<<=10    | x=x<<10    | x=2048   |

### Python比較運算子(關係運算子)(Comparison Operators)
#### ==  ⇨ x==2: True,  x是2(x等於2)
#### !=  ⇨ x!=2: False, x不是2(x不等於2)
#### >=  ⇨ x>=2: True,  x大於等於2
#### <=  ⇨ x<=2: True,  x小於等於2
#### >   ⇨ x>2: False,  x大於2
#### <   ⇨ x<2: False,  x小於2

### Python邏輯運算子(Logical Operators)
#### and 兩邊條件都成立則返回True，否則False。 m = (1 and 0), m: False
#### or  兩邊條件至少一邊成立則返回True，否則False。  m = (1 or 0), m: True
#### not 不是、相反，True變False，False變True。  m = not (1 and 0), m: True

### Python恆等運算子(Identity Operators)
#### is  完全相等

### Python成員運算子(Membership Operators)
#### in 在什麼之中 m = ("1" in "hh1dd"), m: True

### Python位元運算子(Bitwise Operators)(int only)
#### & ⇨ and 將數字轉為2進制並對每一位數進行and運算 10&2 ⇨ 1010 & 0010 = 0010 ⇨ 2
#### | ⇨ or 將數字轉為2進制並對每一位數進行or運算 10|2 ⇨ 1010 | 0010 = 1010 ⇨ 10
#### ^ ⇨ xor 將數字轉為2進制並對每一位數進行xor運算(兩數只有一邊為True才返回True) 10^2 ⇨ 1010 ^ 0010 = 1000 ⇨ 8
#### ~ ⇨ not 將數字轉為2進制並反轉再轉回數字(2的補數) ~10(正數) ⇨ ~1010 ⇨0、1互轉 0101 ⇨ 負數且2的補數 ⇨ 0101-1 ⇨0、1互轉 -0100 ⇨ -1011 ⇨ -11(負數轉正數則反向操作)
#### << ⇨ 將數字轉為2進制並在右邊補數個0再轉回數字 10<<2 ⇨ 1010<<2 ⇨ 101000 ⇨ 40
#### >> ⇨ 將數字轉為2進制並在右邊減少數個位數再轉回數字 10>>2 ⇨ 1010>>2 ⇨ 10 ⇨ 2

## Python內建函數

### [https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)
iterable: 可遍歷物件，arg: argument參數。

### 文字Unicode編碼處理

### chr(int) ⇨ 將指定字元Unicode編碼轉為文字[Unicode解說 https://www.readfog.com/a/1638084002220969984](https://www.readfog.com/a/1638084002220969984)

### ord(str) ⇨ 將指定文字轉為Unicode編碼

<details><summary>展開示例</summary>

```cmd
>>> ord("我")
25105
>>> chr(25105)
'我'
>>> bytes("我", encoding="utf-8")
b'\xe6\x88\x91'
>>> int("e6",16)
230
>>> int("88",16)
136
>>> int("91",16)
145
>>> bin(230)
'0b11100110'
>>> bin(136)
'0b10001000'
>>> bin(145)
'0b10010001'
>>> bin(230).split("1110")[1]
'0110'
>>> "10".join(bin(136).split("10")[1:])
'001000'
>>> "10".join(bin(145).split("10")[1:])
'010001'
>>> int("0110"+"001000"+"010001", 2)
25105
>>> chr(25105)
'我'
>>>
```

</details>

### 變數型態轉換

### str(arg) ⇨ 將變數轉為字符串型態
### int(str, int base) ⇨ 將變數轉為整數型態，無條件捨去; 或是將十進位數字轉為其他數字
### float(arg) ⇨ 將參數轉為float
### list(iterable)  ⇨ 將可遍歷變數轉為list型態
### tuple(iterable)  ⇨ 將可遍歷變數轉為tuple型態
### set(iterable) ⇨ 將可遍歷變數轉為dict型態，或是建立字典
### bytes(arg) ⇨ 將參數轉為bytes
### bytearray(arg) ⇨  將參數轉為bytearray
### bool(arg) ⇨ 將參數轉為布林值有值或非為空為True，無值或空的或None為False

<details><summary>展開示例</summary>

```cmd
>>> str(123)
'123'
>>> str([1,2.3])
'[1, 2.3]'
>>> str(True)
'True'
>>> 1+"P"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> str(1)+"P"
'1P'
```
```cmd
>>> int("5")
5
>>> "5"+"5"
'55'
>>> int("5")+int("5")
10
>>> int("ffffff", 16)
16777215
>>> int("10000000000", 2)
1024
>>> int(True)
1
>>> int(False)
0
>>> int(0.5)
0
>>> int(1.5)
1
```
```cmd
>>> float(1)
1.0
```
```cmd
>>> list("YRTYAAAdd__5546}}")
['Y', 'R', 'T', 'Y', 'A', 'A', 'A', 'd', 'd', '_', '_', '5', '5', '4', '6', '}', '}']
>>> list("YRTYAAAdd__5546}}")[0]
'Y'
>>> list("YRTYAAAdd__5546}}")[1]
'R'
>>> list("YRTYAAAdd__5546}}")[-1]
'}'
```
```cmd
>>> tuple([1,2,3,4,5,6])
(1, 2, 3, 4, 5, 6)
```
```cmd
>>> set([1,2,3])
{1, 2, 3}
```
```cmd
>>> bytes("我", encoding="utf-8")
b'\xe6\x88\x91'

>>> bytes("我", encoding="utf-8")[0]=1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'bytes' object does not support item assignment

>>> bytearray("我", encoding="utf-8")[0]=1

>>> bytearray("我", encoding="utf-8")
bytearray(b'\xe6\x88\x91')

>>> a = bytearray(b'\xe6\x88\x91') #as same as: a=bytearray("我", encoding="utf-8")
>>> a
bytearray(b'\xe6\x88\x91')
>>> a[0]
230
>>> a[1]
136
>>> a[2]
145
>>> len(a)
3
>>> a[0]=1
>>> a
bytearray(b'\x01\x88\x91')
>>> a[0]
1
```
```cmd
>>> bool
<class 'bool'>
>>> bool(0)
False
>>> bool(1)
True
>>> bool(104516547452)
True
>>> bool(None)
False
>>> bool("")
False
>>> bool(b"")
False
>>> bool("fggfdhghh5643fcxg")
True
>>> bool("RRR")
True
>>> bool(bool)
True
>>>
```

</details>

### 其他

### bin(int) ⇨ 將十進位數字轉為二進位
### oct(int) ⇨ 將十進位數字轉為八進位
### hex(int) ⇨ 將十進位數字轉為十六進位
### open(str file_path, str mode, encoding=str encoding) ⇨ 開啟檔案(檔案路徑file_path, 模式mode, encoding=編碼方式)
### print(\*args) ⇨ 打印參數
### len(arg) ⇨ 回傳參數長度
### range(int start, int end, int 間距) ⇨ range(起始值, 終點值_不包含, 間隔)
### enumerate(iterable, start=int) ⇨ 將可遍歷物件每個項目加上index
### zip(\*iterables, strict=False) ⇨ 將數個可遍歷物件壓縮成一個供遍歷使用
### reversed(iterables) ⇨ 回傳可遍歷物件反轉
### abs(int) ⇨ 回傳絕對值
### round(int, ndigits=int) ⇨ 通常為四捨五入
### pow(int, int) ⇨ 次方，pow(2, 5)=2**5=2*2*2*2*2=32，pow(32,1/5)=2
### max(\*args) ⇨ 回傳最大值
### min(\*args) ⇨ 回傳最小值
### id(arg) ⇨ 回傳變數id
### iter(arg) ⇨ 將參數變成可遍歷物件回傳
### next(iterable) ⇨ 回傳可遍歷物件的下個物件，若已到結尾則拋出錯誤
### globals() ⇨ 回傳全域變數
### locals() ⇨ 回傳區域變數
### filter(function, iterable) ⇨ 將可遍歷物件iterable放進函數function內個別執行篩選得到一個新的list
### map(function, iterable) ⇨ 將可遍歷物件iterable放進函數function內個別執行得到一個新的list
### callable(arg) ⇨ 檢查指定參數arg是否可以呼叫調用
### eval(str) ⇨ 將字符串視為程式碼執行並回傳值，不可賦值。
### exec(str) ⇨ 將字符串視為程式碼執行並回傳是否成功。
### dir(arg) ⇨ 取得變數、物件、模組所有可用方法。(__dir__())
### type(arg) ⇨ 取得參數型態、構建新屬性類別。
### help() ⇨ help info，取得模組資訊介紹

## 參考
#### [維基百科](https://zh.wikipedia.org/)
#### 其他各大網站
