#coding:utf-8
import requests
import subprocess
import shlex
import locale

# 获取系统编码格式
# codes = locale.getdefaultlocale()
# code = None
# if len(codes) > 1:
#     if codes[1] == 'cp936':
#         code = 'gbk'
#     else:
code = 'utf-8'

# 统计断线重连的次数
count = 0


def login():
	url = "http://172.19.1.9:8080/eportal/InterFace.do?method=login"

	headers = {
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'Origin': 'http://172.19.1.9:8080',
		'Referer': 'http://172.19.1.9:8080/eportal/index.jsp?wlanuserip=a1ea6bfa0d6e6eefa185548d2eccb994&wlanacname=29185648f4390d7911ef4b72391e17a9&ssid=&nasip=07e38f2323f330cd5ffcc3a203a63100&snmpagentip=&mac=fadf15c8d0df3a45ee61813a79609e5c&t=wireless-v2&url=096e8e7059e430e024191585b02b6dc9b7b80d56d3cad4404b0c90f7e44fbab3&apmac=&nasid=29185648f4390d7911ef4b72391e17a9&vid=acf5e31dcc166138&port=e65ae3d6b3555e50&nasportid=ac41d60d7f1382081362a1ed29e6af272c4a438e3140152c0358914a2f2ac8c82054d7eb5505b59d',
		'Save-Data': 'on',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
}

	user = '2015*********'
	pwd = '******'

	data = 'userId='+user+'&password='+pwd+'&service=Internet&queryString=wlanuserip%253Da1ea6bfa0d6e6eefa185548d2eccb994%2526wlanacname%253D29185648f4390d7911ef4b72391e17a9%2526ssid%253D%2526nasip%253D07e38f2323f330cd5ffcc3a203a63100%2526snmpagentip%253D%2526mac%253Dfadf15c8d0df3a45ee61813a79609e5c%2526t%253Dwireless-v2%2526url%253D096e8e7059e430e024191585b02b6dc9b7b80d56d3cad4404b0c90f7e44fbab3%2526apmac%253D%2526nasid%253D29185648f4390d7911ef4b72391e17a9%2526vid%253Dacf5e31dcc166138%2526port%253De65ae3d6b3555e50%2526nasportid%253Dac41d60d7f1382081362a1ed29e6af272c4a438e3140152c0358914a2f2ac8c82054d7eb5505b59d&operatorPwd=&operatorUserId=&validcode=&passwordEncrypt=false'

	
	r = requests.post(url,headers=headers,data=data).json()

	#print(r['result'])
	
	# 判断当前是否已在线
	if r['result']=='success':
		return 1
	else:
		return 0

#print(login())

import os

def isNetOK(testserver="baidu.com"):
    return os.system("ping " + testserver+" -c 2 -W 1 > /dev/null")


#import time
def loop():
    count = 0
    while True:
        if isNetOK() != 0:
            if login() == 0:
                count+=1
                print('已断线重连%d次'%count)
            else:
                print("第一次连上网")
        else:
            print("已经连上网")


loop()