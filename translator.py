import http.client
import hashlib
import urllib
import random
import json
from pip._vendor.distlib.compat import raw_input
 
def translate(text):
    appid = '20220930001362291'        # 填写你的appid
    secretKey = '1GKobMNylLnbAPL7qCWk'    # 填写你的密钥
    
    httpClient = None
    myurl = '/api/trans/vip/translate'  # 通用翻译API HTTP地址
    
    fromLang = 'auto'       # 原文语种
    toLang = 'zh'           # 译文语种
    salt = random.randint(32768, 65536)
    # 手动录入翻译内容，q存放
    q = text
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + \
            '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    
    # 建立会话，返回结果
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
    
        return result['trans_result'][0]['dst']
    
    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close()