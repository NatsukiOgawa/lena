import os
import pathlib
import shutil

class suffix_change_class():
    def suffix_change(self, file_name, from_suffix, to_suffix):
        # ファイルの拡張子を得る
        sf = pathlib.PurePath(file_name).suffix

        # 変更対象かどうか判定する
        if sf == from_suffix:
            # ファイル名(拡張子除く)を得る
            st = pathlib.PurePath(file_name).stem

            # 変更後のファイル名を得る
            to_name = st + to_suffix

            # ファイル名を変更する
            shutil.move(file_name, to_name)

if __name__ == '__main__':

    # ファイル のみ
    os.chdir("inputs/")
    filenames = [f.name for f in os.scandir() if f.is_file()]
    for i in range(len(filenames)):
        print(filenames[i])
        xxx = pathlib.PurePath(filenames[i]).suffix
        if xxx != ".jpg":
            if xxx == ".gif":
                os.system("rm {}".format(filenames[i]))
            else:
                print(filenames[i])
                aaa = suffix_change_class()
                aaa_aaa = aaa.suffix_change(filenames[i], xxx, '.jpg')
