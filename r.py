import os
import glob


class qwerty_class():
    def qwerty(self, file_name, from_suffix, to_suffix):
        import pathlib
        import shutil
            # ファイルの拡張子を得る
        sf = pathlib.PurePath(file_name).suffix

            # 変更対象かどうか判定する
        if sf == from_suffix:
                # ファイル名(拡張子除く)を得る
            st = pathlib.PurePath(file_name).stem

                # 変更後のファイル名を得る
            to_name = st + to_suffix

                # ファイル名を変更する
            answer = shutil.move(file_name, to_name)
        return answer





paths = glob.glob("inputs/*") # test ディレクトリ内のファイルを返す。# paths = ["test/a.wav", "test/b.txt", "test/c.png"]
data = []
# for i in range(len(paths)):
#     print(paths[i])
for p in paths:
    kakutyoushi = os.path.splitext(os.path.basename(p))[1] ### 拡張子
    name = os.path.splitext(os.path.basename(p))[0] ### ファイル名のみ
    if kakutyoushi != ".jpg":
        # print(name)
        # print(kakutyoushi)
        full_file_name = name + kakutyoushi


        aaa = qwerty_class()
        aaa_aaa = aaa.qwerty(full_file_name, '.gif', '.jpg')
        # change_suffix('sample.def', '.abc', '.xyz')








        data.append(aaa_aaa)
    # print(name)



for i in range(len(data)):
    print(data[i])

# data.sort()
# for i in range(len(data)):
#     print(data[i])
# a
# b
# c
