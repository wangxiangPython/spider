import base64
import json
import requests

def base64_api(uname, pwd,  img):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd,'typeid':27, "image": b64}
    result = json.loads(requests.post("http://api.kuaishibie.cn/imageXYPlus", json=data).text)
    print(result)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""

def reportError(id):
    data = {"id": id}
    result = json.loads(requests.post("http://api.ttshitu.com/reporterror.json", json=data).text)
    if result['success']:
        return "报错成功"
    else:
        return result["message"]
    return ""


if __name__ == "__main__":
    img_path = 'yzm.png'
    # print(result)