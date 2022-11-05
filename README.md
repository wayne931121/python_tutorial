# Python教學

# 目錄

# Python是什麼?
Python是個高階語言，使用直譯器。Python的優勢是簡單明瞭能輕鬆開發APP，劣勢是執行速度過慢。(直譯器是邊翻譯邊執行，如Javascript語言; 編譯器是編譯完後再執行，如C語言)<br>
Python官方網站，含下載、文檔、關於頁面:<br>
[https://www.python.org/](https://www.python.org/)

Python官方文檔<br>
[https://docs.python.org/3/](https://docs.python.org/3/)

Python官方模組<br>
[https://docs.python.org/3/library/index.html](https://docs.python.org/3/library/index.html)

## 如何學習Python
到W3school學習入門文法(右上角地球符號能用Google翻譯調整語言)<br>
[https://www.w3schools.com/python/](https://www.w3schools.com/python/)

到Python官方文檔教學頁面學習入門文法(左上角能調整語言)<br>
[https://docs.python.org/3/tutorial/index.html](https://docs.python.org/3/tutorial/index.html)

## Python能做什麼?
Python有很多別人寫好的模組和強大的內建模組，可以做很多事，有些模組跑很快因為他用C寫，在Python內運作。

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

#### [Scapy](https://scapy.net/)
實用工具<br>
嗅探工具、封包收發測試、網路攻擊工具、偽裝IP工具、網域測試。

### 抓包處理
#### 將抓到的封包、原始碼進行處理，通常搭配request模組使用。
#### [Lxml](https://lxml.de/)<br>
#### [Beatifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)
#### [JSON 內建](https://docs.python.org/3/library/json.html)

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
#### [CSV 內建](https://docs.python.org/3/library/csv.html)

### JSON編輯
#### [JSON 內建](https://docs.python.org/3/library/json.html)

### TOML讀取
#### [TOMLLIB 內建](https://docs.python.org/zh-tw/dev/library/tomllib.html)
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
#### [Math 內建](https://docs.python.org/3/library/math.html)
#### [Numpy](https://numpy.org/)
#### [Scipy](https://scipy.org/)

### 資料圖形化
#### [Matplotlib](https://matplotlib.org/)

### 資料分析
#### [Pandas](https://pandas.pydata.org/)
#### [Pandas支援格式: csv, excel, xml...](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html)<hr>

### 時間
#### [Time 內建(取得當前時間、計算時間差、程式休息幾秒鐘。)](https://docs.python.org/3/library/time.html)
#### [Datetime 內建(取得當前年月日期時間。)](https://docs.python.org/3/library/datetime.html)

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

### 進程、線程
#### [threading 內建(多線程)](https://docs.python.org/3/library/threading.html)
#### [multiprocessing 內建(多進程)](https://docs.python.org/3/library/multiprocessing.html)
#### [concurrent.futures 內建(高階異步線程進程控制接口)](https://docs.python.org/3/library/concurrent.futures.html)

### 壓縮編碼解碼
#### [zipfile 內建(zip)](https://docs.python.org/3/library/zipfile.html)
#### [tarfile 內建(tar)](https://docs.python.org/3/library/tarfile.html)
#### [zlib 內建(gzip、deflate)](https://docs.python.org/3/library/zlib.html)
#### [gzip 內建](https://docs.python.org/3/library/gzip.html)
#### [brotli (br)](https://python-hyper.org/projects/brotlipy/en/latest/)
#### [lzma 內建(lzma)](https://docs.python.org/3/library/lzma.html)
#### [bz2 內建(bz2)](https://docs.python.org/3/library/bz2.html)

### C函數使用
#### [ctypes](https://docs.python.org/3/library/ctypes.html)

### MIMETYPE處理
#### [mimetypes 內建](https://docs.python.org/3/library/mimetypes.html)

### 顏色轉換(例如 rgb to hsl)
#### [colorsys 內建](https://docs.python.org/3/library/colorsys.html)

### 視覺化界面
#### [Thinker 內建(GUI圖形使用者介面，寫應用程式使用。)](https://docs.python.org/3/library/tkinter.html)
#### [Turtle 內建(畫畫用的)](https://docs.python.org/3/library/turtle.html)
#### [Pygame (寫遊戲使用，使用SDL, Simple DirectMedia Layer。)](https://www.pygame.org/)
#### [Pyglet (多媒體遊戲庫。)](https://pyglet.org/)
#### [Cocos2d (寫遊戲使用，使用Pyglet。)](https://github.com/los-cocos/cocos)

## Python文法結構

### 函數
#### def function_name(args*, kargs**): return value

### 迴圈
#### for i in iterObject: doSomething
#### while flag: doSomething

### 物件
#### class object_name(parent):

### 刪除
#### del variable_name

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
#### = 
#### +=     ⇨ x+=10    ⇨ x=x+10, x=12
#### -=     ⇨ x-=10    ⇨ x=x-10, x=-8
#### \*=    ⇨ x\*=10   ⇨ x=x\*10, x=20
#### /=     ⇨ x/=10    ⇨ x=x/10, x=0.2
#### //=    ⇨ x//=10   ⇨ x=x//10, x=0
#### %=     ⇨ x%=10    ⇨ x=x%10, x=2
#### \*\*=  ⇨ x\*\*=10 ⇨ x=x\*\*10, x=1024
#### &=     ⇨ x&=10    ⇨ x=x&10, x=2
#### |=     ⇨ x|=10    ⇨ x=x|10, x=10
#### ^=     ⇨ x^=10    ⇨ x=x^10, x=8
#### >>=    ⇨ x>>=10   ⇨ x=x>>10, x=0
#### <<=    ⇨ x<<=10   ⇨ x=x<<10, x=2048

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
### chr(int) ⇨ 將指定字元Unicode編碼轉為文字[Unicode解說 https://www.readfog.com/a/1638084002220969984](https://www.readfog.com/a/1638084002220969984)
### ord(str) ⇨ 將指定文字轉為Unicode編碼
### str(arg) ⇨ 將變數轉為字符串型態
### int(str) ⇨ 將變數轉為整數型態，無條件捨去
### list(arg)  ⇨ 將變數轉為list型態
### float(arg) -> float 浮點數(小數)
### bytes(arg) -> bytes 原始數據(只讀r)
### bytearray(arg) -> bytearray 原始數據陣列(讀寫rw)
### bool(arg) -> boolean 布林值(True or False)
### bin
### oct
### hex
### open
### filter
### map
### callable
