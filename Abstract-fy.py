# -*- coding: utf-8 -*-            
# @Author : yunwenwu
# @Time : 2022/12/7 17:50
# 英文摘要页
import requests
import random
from hashlib import md5
from docxtpl import DocxTemplate
class AbstractFy:
    def fyA(self,appid='20221215001498326',appkey='mLoRTUdahi5oJE6XiQQi'):
        url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
        L=[]
        for i in range(1,9):
            query = input("请输入要翻译的内容")

            # 函数
            def make_md5(s, encoding='utf-8'):
                return md5(s.encode(encoding)).hexdigest()

            salt = random.randint(32768, 65536)
            sign = make_md5(appid + query + str(salt) + appkey)

            #构建请求
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            payload = {'appid': appid, 'q': query, 'from': 'zh', 'to': 'en', 'salt': salt, 'sign': sign}

            # 发送请求
            r = requests.post(url, params=payload, headers=headers)
            r_1=r.json()

            # 结果处理
            r_2 = r_1['trans_result']
            r_3 = r_2[0]
            r_4 = r_3["dst"]
            L.append(r_4)

        print(L)
        #输出到模板文件
        tpl = DocxTemplate(".\\Standard Document\\Abstract.docx")
        # 渲染主体
        context = {
            'content1': L[0],
            'content2': L[1],
            'content3': L[2],
            'key1': L[3],
            'key2': L[4],
            'key3': L[5],
            'key4': L[6],
            'key5': L[7]
        }
        # 将渲染主体加载到模板文件
        tpl.render(context)
        # 提示信息and保存文件
        print("Abstract页已生成...")
        tpl.save(".\\Generate document\\Abstract.docx")

if __name__=="__main__":
    a=AbstractFy()
    a.fyA()