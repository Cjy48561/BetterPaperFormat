# -*- coding: utf-8 -*-            
# @Author : yunwenwu
# @Time : 2022/12/6 15:03
# 中文摘要页

from docxtpl import DocxTemplate
# 加载模板文件
class Abstract:
        def Save_Abstract(self,content1,content2,content3,key1,key2,key3,key4,key5):
                tpl=DocxTemplate(".\\Standard Document\\Abstract-Chinese.docx")
                # 渲染主体
                context={
                        'content1':content1,
                        'content2':content2,
                        'content3':content3,
                        'key1':key1,
                        'key2':key2,
                        'key3':key3,
                        'key4':key4,
                        'key5':key5
                                 }
                # 将渲染主体加载到模板文件
                tpl.render(context)
                # 提示信息and保存文件
                print("中文摘要页已生成...")
                tpl.save(".\\Generate document\\Abstract-Chinese.docx")