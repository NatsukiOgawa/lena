import cv2


class my_cascade_class():
    def my_cascade(self, image, cascade_name):
        # image = "pos/pika.jpg"
        # image = "object.png"
        # カスケードファイルを読み込む
        face_cascade = cv2.CascadeClassifier(cascade_name)
        # 画像を読み込む
        loaded_img = cv2.imread(f"{image}")
        # （高さ・幅・色数)
        # 読み込んだ画像を、グレースケール画像として読み込む
        gray = cv2.cvtColor(loaded_img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray)
        if len(faces) == 0:
            print('画像が認識されません')
        else:
            for (x,y,w,h) in faces:
                    # この中で、顔の部分に色をつけている処理をしている
                penned_img = cv2.rectangle(loaded_img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = penned_img[y:y+h, x:x+w]
            # 画像を表示させる
            cv2.imshow('img',penned_img)
            # キーボードの入力を待つ
            cv2.waitKey(0)
            # 画像windowを閉じる
            cv2.destroyAllWindows()



            """
            opencv_createsamples -img ./pos/pika.jpg -vec ./vec/image.vec -num 50 -bgcolor 255 -maxidev 40 -maxxangle 0.8 -maxyangle 0.8 -maxzangle 0.5 -show
            <コマンド名           > -img <正解画像のpath> -vec ./vec/image.vec -num <サンプルにする画像数> -bgcolor 255 -maxidev 40 -maxxangle 0.8 -maxyangle 0.8 -maxzangle 0.5 -show
            """


if __name__ == '__main__':
    file_name = "object.png"
    cascade_name = "cascade.xml"

    aaa = my_cascade_class()
    aaa_aaa = aaa.my_cascade(file_name, cascade_name)
