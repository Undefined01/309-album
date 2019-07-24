import os
import json


def getDirs(path):
    res = []
    items = os.listdir(path)
    for item in items:
        fullPath = os.path.join(path, item)
        if os.path.isdir(fullPath):
            res.append(fullPath)
    return res


def getFiles(path, exts):
    res = []
    for baseDir, _, files in os.walk(path):
        for f in files:
            fullPath = os.path.join(baseDir, f)
            if fullPath.split('.')[1].lower() in exts:
                res.append('/'.join(fullPath.split(os.sep)[2:]))
            else:
                print('[ignored]', fullPath)
    return res


albums = []
dirs = getDirs(r'E:\309图片')
for i in dirs:
    title = i.split(os.sep)[-1]
    images = getFiles(i, ['jpg', 'png'])
    albums.append({
        'title': title,
        'count': len(images),
        'cover': images[0]
    })
    res = {
        'title': title,
        'items': images
    }
    with open(f'{title}.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(res, ensure_ascii=False, indent=4))

with open('index.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(albums, ensure_ascii=False, indent=4))
