import os
import shutil


def mv1(path1, path2):
    for baseDir, _, files in os.walk(path1):
        for f in files:
            fullPath = os.path.join(baseDir, f)
            category = '_'.join(fullPath.split(os.sep)[2:])
            ext = category.split('.')[1]

            shutil.move(fullPath, os.path.join(path2, category))


def mv2(path1, path2):
    for baseDir, _, files in os.walk(path1):
        for f in files:
            fullPath = os.path.join(baseDir, f)
            category = fullPath.split(os.sep)[2]
            catagory = '/'.join(category.split(' '))

            target = os.path.join(path2, catagory)
            if not os.path.isdir(os.path.dirname(target)):
                os.makedirs(os.path.dirname(target))
            shutil.move(fullPath, target)


# mv1(r'E:\309图片压缩整理', r'E:\309转码')
mv2(r'E:\309转码完成', r'E:\309转码')
