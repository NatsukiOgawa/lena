import os

os.chdir("inputs/")
# os.system("ls")
# ファイル のみ
filenames = [f.name for f in os.scandir() if f.is_file()]

for file in os.listdir():
    base, ext = os.path.splitext(file)
    if ext != '.jpg':
        print('file:{},ext:{}'.format(file,ext))
        os.rename("{}{}".format(file, ext), "{}{}".format(file, "jpg"))
