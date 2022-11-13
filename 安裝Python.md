# 安裝Python
### 1. 到官方網站下載Python(Download Python)<br>
#### [https://www.python.org/downloads/](https://www.python.org/downloads/)
### 2. 安裝Python(Install Python)
### 3. 設定環境變數(如果安裝時設定則免除這步驟)
完成後打開電腦的CMD鍵入Python，如果有找到命令或出現類似以下資料就成功了!<br>
註: 打開CMD : (Windows -> 按Windows+R, 輸入cmd, 按Enter)
```cmd
Microsoft Windows [版本 10.0.19043.2130]
(c) Microsoft Corporation. 著作權所有，並保留一切權利。

C:\Users\$UserName>python
Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello World")
Hello World
>>> exit()

C:\Users\$UserName>
```
## Python可用來開發Python的工具

### 程式碼編輯器(文字編輯器)
#### Notepad++
#### Notepad Windows內建
<hr>

### 整合執行環境
#### Anaconda
可輕鬆建立Python虛擬環境，並且可選擇不同版本。如果想了解其他Python Virtual Environment，可點擊這裡: https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe
#### Jupyter Notebook:
格式為ipython(.ipynb)<br>
打碼完按Ctrl+Enter就可執行，而且還能使用文字標題欄增加可讀性，並且能新增複製刪除欄以儲存執行結果和更改前的程式碼達到輕鬆除錯。可將完成的檔案匯出python、html、pdf等多種檔案，並且能自定快速鍵。<br>
缺點: 在編輯一些視窗化的程式，如要用到sdl2的時候，需要每執行完一遍就restart kernel。(不適合編輯視窗化的程式)
#### PyCharm
適合很常使用Python的人，能輕鬆編輯運作Python。不適合會很常使用多程式語言而Python並沒有占他們程式語言很重要一部分的人。
#### Vscode
適合使用多程式語言且用Windows的人，能輕鬆編輯運作Python，但是自動拼字很煩人記得關。(自動拼字: 自動提示、auto-completion)。


### 推薦
#### Anaconda + Jupyter Notebook + Notepad++
