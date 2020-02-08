import os
import cv2

#保存ディレクトリ作成
# os.mkdir('./data')

cap = cv2.VideoCapture('./movie/test.mp4')
number = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

#初期値設定
n = 0

#ループを回す
while True:
    ret, frame = cap.read()
    if ret:
        cv2.imwrite('./data/{}.jpg'.format(str(n).zfill(number)), frame)
        n += 1
    else:
        break
