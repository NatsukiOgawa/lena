from subprocess import check_output
import cv2
import os

class face_identification_class():
    def face_identification(self, t, out_list):
        print("[{}]".format(out_list[t]))
        cascade_path = "./cascades/haarcascade_frontalface_default.xml"
        # t_file_name = str(t)
        # if t < 10:
        #     t_file_name = t_file_name.zfill(2)

        # image_file = "{}.jpg".format(t_file_name)
        image_file = "{}".format(out_list[t])
        image_path = "./inputs/" + image_file
        output_path = "./outputs/" + image_file

        #ファイル読み込み
        image = cv2.imread(image_path)

        #グレースケール変換
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        #カスケード分類器の特徴量を取得する

        cascade = cv2.CascadeClassifier(cascade_path)
        #物体認識（顔認識）の実行
        #image – CV_8U 型の行列．ここに格納されている画像中から物体が検出されます
        #objects – 矩形を要素とするベクトル．それぞれの矩形は，検出した物体を含みます
        #scaleFactor – 各画像スケールにおける縮小量を表します
        #minNeighbors – 物体候補となる矩形は，最低でもこの数だけの近傍矩形を含む必要があります
        #flags – このパラメータは，新しいカスケードでは利用されません．古いカスケードに対しては，cvHaarDetectObjects 関数の場合と同じ意味を持ちます
        #minSize – 物体が取り得る最小サイズ．これよりも小さい物体は無視されます
        facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))

        #print(facerect)
        color = (255, 255, 255) #白
        color = (0, 0, 0) #黒

        # 検出した場合
        if len(facerect) > 0:
            #検出した顔を囲む矩形の作成
            for rect in facerect:
                cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)

                #認識結果の保存
                cv2.imwrite(output_path, image)

if __name__ == '__main__':

    # ファイル のみ
    os.chdir("inputs/")
    inputs_length = [f.name for f in os.scandir() if f.is_file()]
    os.chdir("../")

    os.chdir("outputs/")
    outputs_length = [f.name for f in os.scandir() if f.is_file()]
    os.chdir("../")

    
    #round = 200
    round = len(inputs_length)
    # コマンド実行
    cmd = 'ls inputs/'
    out = check_output(cmd.split()).decode('utf-8')
    # 結果を分割してリスト化
    out_list = out.split()
    print(out_list)
    for t in range(round):
        aaa = face_identification_class()
        aaa_aaa = aaa.face_identification(t, out_list)

    print(len(outputs_length)/len(inputs_length))
