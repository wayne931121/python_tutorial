# OpenCV

## 官方網站
https://opencv.org/

https://github.com/opencv

https://docs.opencv.org/5.x/index.html

## 簡介
相片編輯(預設為BGR 0~255)、影片編輯、網路串流讀取、擴增實境、臉部辨識、手勢辨識、動作辨識、運動跟蹤、物體辨識、圖像分割。

## 下載

```cmd
pip install opencv-python
```

## 使用

讀寫圖片:

```python
import cv2

img = cv2.imread(image_path) #讀取圖片
cv2.imshow(img) #顯示圖片
cv2.waitkey(0) #等待圖片視窗結束(0表示持續等待，直到使用者按下按鍵為止)
cv2.imwrite(filename, img) #匯出圖片
```

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

轉換圖片色彩通道

```python
cv2.cvtColor(frame, mode)

mode: #2就是to的意思，音一樣。
    cv2.COLOR_BGR2GRAY
    cv2.COLOR_GRAY2BGR
    cv2.COLOR_RGB2GRAY
    cv2.COLOR_GRAY2RGB
```

讀寫影片:

```python
import cv2
cap = cv2.VideoCapture('video_path')              # 讀取影片。
fourcc = cv2.VideoWriter_fourcc(*'MP4V')          # 影片的格式mp4
out = cv2.VideoWriter('output_1.mp4', fourcc, 20.0, (1920,  1080))  # 創建新影片，FPS為20, 尺寸為 640x360
while True:
    ret, frame = cap.read()
    if not ret:
        break
    out.write(img_2)                       # 將這幀圖片寫入新影片
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
