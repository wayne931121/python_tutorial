# OpenCV

## 官方網站
https://opencv.org/

https://github.com/opencv

https://docs.opencv.org/5.x/index.html

## 簡介
相片編輯(0~255)、影片編輯、網路串流讀取、擴增實境、臉部辨識、手勢辨識、動作辨識、運動跟蹤、物體辨識、圖像分割。

## 下載

```cmd
pip install opencv-python
```

## 使用

```python
import cv2

img = cv2.imread(image_path) #讀取圖片
cv2.imshow(img) #顯示圖片
cv2.waitkey(0) #等待圖片視窗結束
cv2.imwrite(filename, img) #匯出圖片
```

`cv2.rotate(img_np, mode)`旋轉圖片

```
mode:
    cv2.ROTATE_90_CLOCKWISE 順時針旋轉90度
    cv2.ROTATE_90_COUNTERCLOCKWISE 逆時針旋轉90度
    cv2.ROTATE_180 180度旋轉
```

`cv2.flip(img_np, mode)`翻轉圖片
```
mode:
    0 垂直翻轉
    1 水平翻轉
   -1 上下左右顛倒
```

`cv2.transpose(img_np)`逆時針旋轉90度圖片

`cv2.resize(img_np, (width, height))`設定圖片大小
