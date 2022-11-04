# Python教學

# Python是什麼?
Python是個高階語言，使用直譯器。Python的優勢是簡單明瞭能輕鬆開發APP，劣勢是執行速度過慢。(直譯器是邊翻譯邊執行，如Javascript語言; 編譯器是編譯完後再執行，如C語言)

## 如何學習Python
到w3school學習入門文法<br>
[https://www.w3schools.com/python/](https://www.w3schools.com/python/)

## Python能做什麼?
Python有很多別人寫好的模組和強大的內建模組，可以做很多事，有些包跑很快是因為他是用C寫的，在Python內運作。

### 網路:
#### [Socket](https://docs.python.org/3/library/socket.html)
客戶端、伺服器端、底層應用。<br>
客戶端，爬蟲、嗅探使用，向伺服器寄出請求，並取得回應，像是網頁原始碼。<br>
伺服器端，開伺服器等待用戶連接並做出相應行動。

#### [SSL](https://docs.python.org/3/library/ssl.html)
客戶端、伺服器端、底層應用。<br>
wrap socket with ssl.包裝ssl到socket上，如讓http變成https。

#### [Request](https://requests.readthedocs.io/en/latest/)
客戶端<br>
爬蟲、抓包使用，向網路寄出請求，並取得回應，像是網頁原始碼。

#### [Flask](https://flask.palletsprojects.com/en/2.2.x/)
伺服器端<br>
網頁伺服器，開伺服器等待用戶連接並做出相應行動。

#### [Scapy](https://scapy.net/)
客戶端<br>
嗅探工具、封包收發測試、網路攻擊工具、偽裝IP工具、網域測試。

### 抓包處理
    lxml<br>
    beatifulsoup<br>
