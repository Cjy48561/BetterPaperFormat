# -*- coding: utf-8 -*-            
# @Author : yunwenwu
# @Time : 2022/12/6 15:03
from docxtpl import DocxTemplate
# 加载模板文件
tpl=DocxTemplate(".\\Standard Document\\Abstract-Chinese.docx")
# 渲染主体
context={'content':"C 语言是一门面向过程的计算机编程语言。",
        'key1':"在线阅读",
        'key2':"css",
        'key3':"DW",
        'key4':"系统",
        'key5':"思考"
                 }
# 将渲染主体加载到模板文件
tpl.render(context)
# 提示信息and保存文件
print("中文摘要页已生成...")
tpl.save(".\\Generate document\\Abstract-Chinese.docx")

