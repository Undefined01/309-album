import os


def check(path1, path2):
    res = {}
    for baseDir, _, files in os.walk(path1):
        for f in files:
            fullPath = os.path.join(baseDir, f)
            filePath = '/'.join(fullPath.split(os.sep)[2:])
            fullPath2 = os.path.join(path2, filePath)
            if not os.path.isfile(fullPath2):
                if not os.path.isfile(fullPath2.split('.')[0] + '.jpg'):
                    print('[ERROR]', filePath, 'not exist')
    return res


check(r'E:\309图片压缩整理', r'E:\309图片缩略图')
