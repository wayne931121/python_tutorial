# Python教學

# 目錄

# Python是什麼?
Python是個高階語言，使用直譯器。Python的優勢是簡單明瞭能輕鬆開發APP，劣勢是執行速度過慢。(直譯器是邊翻譯邊執行，如Javascript語言; 編譯器是編譯完後再執行，如C語言)

## 如何學習Python
到W3school學習入門文法<br>
[https://www.w3schools.com/python/](https://www.w3schools.com/python/)

## Python能做什麼?
Python有很多別人寫好的模組和強大的內建模組，可以做很多事，有些模組跑很快因為他用C寫，在Python內運作。

## Python實用模組及功能

### 網路:
讀取網頁、開網頁伺服器、發送封包、接收封包

#### [Socket內建](https://docs.python.org/3/library/socket.html)
客戶端、伺服器端、底層應用。<br>
客戶端，爬蟲、嗅探使用，向伺服器寄出請求，並取得回應，像是網頁原始碼。<br>
伺服器端，開伺服器等待用戶連接並做出相應行動。

#### [SSL內建](https://docs.python.org/3/library/ssl.html)
客戶端、伺服器端、底層應用。<br>
wrap socket with ssl.包裝ssl到socket上，如讓http變成https。

#### [Request](https://requests.readthedocs.io/en/latest/)
客戶端<br>
爬蟲、抓包使用，向網路寄出請求，並取得回應，像是網頁原始碼。

#### [Flask](https://flask.palletsprojects.com/en/2.2.x/)
伺服器端<br>
網頁伺服器，開伺服器等待用戶連接並做出相應行動。

#### [Scapy](https://scapy.net/)
實用工具<br>
嗅探工具、封包收發測試、網路攻擊工具、偽裝IP工具、網域測試。

### 抓包處理
#### 將抓到的封包、原始碼進行處理，通常搭配request模組使用。
#### [Lxml](https://lxml.de/)<br>
#### [Beatifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)

### 控制瀏覽器
#### 爬蟲的一種
#### [Selenium](https://selenium-python.readthedocs.io/)<hr>

### 編輯任何檔案
#### Python內建函數Open

### 音樂標頭編輯(MP3 ID3 Metadata)
#### [Eyed3](https://eyed3.readthedocs.io/en/latest/eyed3.html)

### 照片、影片編輯，串流讀取
#### [OpenCV](https://www.google.com/search?q=opencv+python)

### CSV編輯
#### [CSV內建](https://docs.python.org/3/library/csv.html)

### JSON編輯
#### [JSON內建](https://docs.python.org/3/library/json.html)

### TOML讀取
#### [TOMLLIB內建](https://docs.python.org/zh-tw/dev/library/tomllib.html)
<hr>

### 人工智慧、大數據分析
#### [Tensorflow](https://www.tensorflow.org/)
#### [Pytorch](https://pytorch.org/)
#### [Scikit-Learn](https://scikit-learn.org/)
#### [Keras](https://keras.io/)
#### H5檔案讀取
##### [H5PY](https://docs.h5py.org/)
<hr>

### 陣列、數學與矩陣運算
#### [Numpy](https://numpy.org/)
#### [Scipy](https://scipy.org/)

### 資料圖形化
#### [Matplotlib](https://matplotlib.org/)

### 資料分析
#### [Pandas](https://pandas.pydata.org/)
#### [Pandas支援格式: csv, excel, xml...](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html)<hr>

### 時間
#### [Time內建](https://docs.python.org/3/library/time.html)
#### [Datetime內建](https://docs.python.org/3/library/datetime.html)

### 系統(系統資訊、程式資訊、檔案操作、標準輸入輸出...)、進程、線程
#### [os內建](https://docs.python.org/3/library/os.html)
#### [sys內建](https://docs.python.org/3/library/sys.html)
#### [signal內建](https://docs.python.org/3/library/signal.html)
#### [subprocess內建](https://docs.python.org/3/library/subprocess.html)
#### [shlex內建](https://docs.python.org/3/library/shlex.html)
#### [threading內建](https://docs.python.org/3/library/threading.html)
#### [multiprocessing內建](https://docs.python.org/3/library/multiprocessing.html)
#### [io內建](https://docs.python.org/3/library/io.html)

### 壓縮編碼解碼
#### [zipfile內建(zip)](https://docs.python.org/3/library/zipfile.html)
#### [tarfile內建(tar)](https://docs.python.org/3/library/tarfile.html)
#### [zlib內建(gzip、deflate)](https://docs.python.org/3/library/zlib.html)
#### [gzip內建](https://docs.python.org/3/library/gzip.html)
#### [brotli(br)](https://python-hyper.org/projects/brotlipy/en/latest/)
#### [lzma內建(lzma)](https://docs.python.org/3/library/lzma.html)
#### [bz2內建(bz2)](https://docs.python.org/3/library/bz2.html)

## Python文法結構

### 函數
#### def function_name(args*, kargs**): return value

### 迴圈
#### for i in iterObject: doSomething
#### while flag: doSomething

### 物件
#### class object_name(parent):

## Python資料型態
### str -> string 字符串
### int -> integer 整數
### list -> list 清單(類似陣列，但內容物型態不限)
### dict -> dictionary 字典
### float -> float 浮點數(小數)
### bytes -> bytes 原始數據(只讀r)
### bytearray -> bytearray 原始數據陣列(讀寫rw)
### bool -> boolean 布林值(True or False)

## Python運算子
```
### 假設x=2, y=7
### Python算術運算子
#### \+ => 加 x+y=2+7=9
#### \- => 減 x-y=2-7=-5
#### \* => 乘 x\*y=2\*7=14
#### / => 除 x/y=2/7=0.2857142857142857
#### // => 除完取整數(商) x//y=2//7=0
#### \% => 除完取餘數 x%y=2%7=2
#### \*\* => 次方 x\*\*y=2\*\*7=2*2*2*2*2*2*2=128

### Python指定運算子
#### +=      => x+=10 (x=x+10), x=12
#### -=      => x-=10 (x=x-10), x=-8
#### \*=      => x\*=10 (x=x\*10), x=20
#### /=      => x/=10 (x=x/10), x=0.2
#### //=     => x//=10 (x=x//10), x=0
#### %=      => x%=10 (x=x%10), x=2
#### \*\*=   => x\*\*=10 (x=x\*\*10), x=1024
#### &=      => x&=10 (x=x&10), x=
#### |=      => x|=10 (x=x|10), x=
#### ^=      => x^=10 (x=x^10), x=
#### >>=     => x>>=10 (x=x>>10), x=
#### <<=     => x<<=10 (x=x<<10), x=

### Python比較運算子(關係運算子)
#### ==
#### !=
#### >=
#### <=
#### >
#### <

### Python邏輯運算子
#### and
#### or
#### not

### Python恆等運算子
#### is
#### is not

### Python成員運算子(Membership Operators)
#### in
#### not in

### Python位元運算子
#### &
#### |
#### ^
#### ~
#### <<
#### >>
```
## Python內建函數
### chr
### ord
### str -> string 字符串
### int -> integer 整數
### list -> list 清單(類似陣列，但內容物型態不限)
### dict -> dictionary 字典
### float -> float 浮點數(小數)
### bytes -> bytes 原始數據(只讀r)
### bytearray -> bytearray 原始數據陣列(讀寫rw)
### bool -> boolean 布林值(True or False)
### bin
### oct
### hex
### open
