# OpenCV

## 官方網站
https://opencv.org/

https://github.com/opencv

https://docs.opencv.org/5.x/index.html

## 官方High-level GUI模組文檔
https://docs.opencv.org/4.x/d7/dfc/group__highgui.html

## 簡介
相片編輯(預設為BGR 0~255)、影片編輯、網路串流讀取、擴增實境、臉部辨識、手勢辨識、動作辨識、運動跟蹤、物體辨識、圖像分割。

## 下載

```cmd
pip install opencv-python
```

## 使用

### 讀寫圖片:

```python
import cv2

img = cv2.imread(image_path) #讀取圖片
cv2.imshow("window", img.astype(dtype="uint8")) #顯示圖片
cv2.waitkey(0) #等待圖片視窗結束(0表示持續等待，直到使用者按下按鍵為止。非零表示等待毫秒數，函數回傳使用者從鍵盤按下的KeyCode，-1表示使用者沒按，27表示esc，ord("q")->113表示q鍵)
cv2.imwrite(filename, img) #匯出圖片
```

讀取圖片

```python
cv2.imread(image_path, mode)

mode:
    cv2.IMREAD_UNCHANGED 原始讀取保留透明度
    cv2.IMREAD_COLOR 預設值
    cv2.IMREAD_GRAYSCALE 灰階讀取
```

旋轉圖片

```python
cv2.rotate(img_np, mode)

mode:
    cv2.ROTATE_90_CLOCKWISE 順時針旋轉90度
    cv2.ROTATE_90_COUNTERCLOCKWISE 逆時針旋轉90度
    cv2.ROTATE_180 180度旋轉
```

翻轉圖片

```python
cv2.flip(img_np, mode)

mode:
    0 垂直翻轉
    1 水平翻轉
   -1 上下左右顛倒
```

逆時針旋轉90度圖片

```python
cv2.transpose(img_np)
```

設定圖片大小

```python
cv2.resize(img_np, (width, height))
```

裁剪圖片(np.array分割操作)

```python
img_np = cv2.imread(image_path)
img = img_np[y:y+h, x:x+w] #x,y是座標，基準點是圖片左上角，w,h: width, height。
```

轉換圖片色彩通道

```python
cv2.cvtColor(img_np, mode)

mode: #2就是to的意思，音一樣。
    cv2.COLOR_BGR2GRAY
    cv2.COLOR_GRAY2BGR
    cv2.COLOR_RGB2GRAY
    cv2.COLOR_GRAY2RGB
```

### 讀寫影片:

```python
import cv2

cap = cv2.VideoCapture('video_path')              # 讀取影片。
fourcc = cv2.VideoWriter_fourcc(*'MP4V')          # 影片的格式mp4
out = cv2.VideoWriter('output_1.mp4', fourcc, 20.0, (1920,  1080))  # 創建新影片，FPS為20, 尺寸為 640x360

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)                       # 將這幀圖片寫入新影片
    cv2.imshow('Title', frame)
    if cv2.waitKey(1) == ord('q'):
        break                              # 按下 q 鍵停止

# 釋放所有資源
cap.release()
out.release()
cv2.destroyAllWindows()
```

cv2.VideoCapture(video)用法:

```python
cv2.VideoCapture('video_path') 從影片路徑讀取影片
cv2.VideoCapture('url') 從網路串流讀取影片
cv2.VideoCapture(0) 從畚箕電腦攝影鏡頭讀取影片
```

查看影像資訊:

```python
cap = cv2.VideoCapture(video)
cap.get(cv2.CAP_PROP_FRAME_WIDTH)
cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
cap.get(cv2.CAP_PROP_FPS)
cap.get(cv2.CAP_PROP_FOURCC)
cap.get(cv2.CAP_PROP_FRAME_COUNT) #總幀數
cap.get(cv2.CAP_PROP_POS_MSEC) #影片目前時間位置(以毫秒為單位)
```

設定影像尺寸:

```python
cap = cv2.VideoCapture(video)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
```

色彩分離和整合:
```python
import cv2
import numpy as np

image = cv2.imread("u1.jpg")
r = image[:,:,2:3]
g = image[:,:,1:2]
b = image[:,:,0:1]
new_image = np.concat((b,g,r),axis=2).astype(dtype="uint8")
cv2.imshow('image',new_image)
cv2.waitKey(0)
```
去除負數和大於255的值，使其只在0到255間，使大於255的值等於255，小於0的數字歸零:
```python
a = np.array([255,356,10,-1,0,30])

f255 = lambda a:((a>255)*255)+(a*(a<=255))
fn1 = lambda a:a*(a>=0)

def wise(a):
    a = f255(a)
    a = fn1(a)
    return a

a = wise(a)
print(a)
```

直接對顏色進行矩陣運算
```python
image = cv2.imread("your.jpg")
#                       B G R   B  G   R
new_image = wise(image*[2,2,1]+[1,100,-2]).astype("uint8")
cv2.imshow('image',new_image)
cv2.waitKey(0)
```
相片隨機變換顏色播放範例
```python
import cv2
import random
def wise(a):
    a = ((a>255)*255)+(a*(a<=255))
    a = a*(a>=0)
    return a
image = cv2.imread("your_image.jpg")
f1 = lambda:random.randint(0,20)/10
f2 = lambda:random.randint(-255,255)
while True:
    cv2.namedWindow("video",flags=cv2.WINDOW_NORMAL)
    frame = wise(image*[f1(),f1(),f1()]+[f2(),f2(),f2()]).astype("uint8")
    cv2.imshow('video', frame)
    if cv2.waitKey(100) in [27,ord('q')]: #esc key or q key
        break
cv2.destroyAllWindows()
```
