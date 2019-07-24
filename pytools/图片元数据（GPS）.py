def getLocation(imgPath):
    import PIL.Image as Image
    from PIL.ExifTags import TAGS
    import requests
    import json
    import base64
    
    info = Image.open(imgPath)._getexif()
#     for k, v in info.items():
#         name = TAGS.get(k, k)
#         print( '%s (%s) = %s' % (name, k, v))
#     print('-'*80)
    
    GPSInfo = info[34853]
    DateTime = info[306]
    
    direction = {'N':1,'S':-1,'E':1,'W':-1}
    frac = lambda x: float(x[0])/float(x[1])
    
    latitude = direction[GPSInfo[1]] * (frac(GPSInfo[2][0]) + frac(GPSInfo[2][1])/60 + frac(GPSInfo[2][2])/3600)
    longitude = direction[GPSInfo[3]] * (frac(GPSInfo[4][0]) + frac(GPSInfo[4][1])/60 + frac(GPSInfo[4][2])/3600)
    
    # https://www.cnblogs.com/limeiky/p/5818601.html
    GPSLocation = (latitude, longitude)
    res = requests.get(f'http://api.map.baidu.com/ag/coord/convert?from=0&to=1&y={latitude}&x={longitude}')
    res = json.loads(res.text)
    BaiduLocation = (base64.b64decode(res['y']).decode(), base64.b64decode(res['x']).decode())
    res = requests.get(f'http://api.map.baidu.com/?qt=rgc&x={BaiduLocation[1]}&y={BaiduLocation[0]}&dis_poi=1')
    res = json.loads(res.text)
    address = res['content']['address'] + ',' + res['content']['business']
    return GPSLocation, BaiduLocation, address

getLocation('1.jpg')