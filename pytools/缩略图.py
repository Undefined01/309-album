import os
import subprocess


def getFiles(path, exts):
    for baseDir, _, files in os.walk(path):
        for f in files:
            fullPath = os.path.join(baseDir, f)
            run('/'.join(fullPath.split(os.sep)[2:]))


def run(path):
    print(path)
    imageFormat = ['jpg', 'jpeg', 'png']
    if not os.path.isdir('E:\\309图片缩略图\\' + os.path.dirname(path)):
        os.makedirs('E:\\309图片缩略图\\' + os.path.dirname(path))
    if path.split('.')[1].lower() in imageFormat:
        cmd = r'ffmpeg -v quiet -i "E:\309图片压缩整理\{}" -vf scale=-1:250 "E:\309图片缩略图\{}"'.format(path, path)
        print(cmd)
        subprocess.call(cmd)
    else:
        cmd = r'ffmpeg -v quiet -i "E:\309图片压缩整理\{}" -ss 10s -frames:v 1 -vf scale=-1:250 "E:\309图片缩略图\{}.jpg"'.format(path, path.split('.')[0])
        print(cmd)
        subprocess.call(cmd)


getFiles(r'E:\309图片压缩整理', run)
