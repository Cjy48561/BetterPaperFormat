# -*- coding: utf-8 -*-            
# @Author : yunwenwu
# @Time : 2023/1/31 15:44
# 致谢页思路:利用模板生成后添加段落与个人信息
# 导入相关模块
from docxtpl import DocxTemplate

class Thanksfor:
    def Save_Thanksfor(self,content1,content2,content3,name,year,month,day):
        # 加载模板文件
        tpl = DocxTemplate(".\\Standard Document\\ThanksFor.docx")
        # 渲染主体
        context={
            'content_1':content1,
            'content_2':content2,
            'content_3':content3,
            'name':name,
            'year':year,
            'month':month,
            'day':day
        }
        # 将渲染主体加载到模板文件中
        tpl.render(context)
        # 提示信息并且保存文件
        tpl.save(".\\Generate document\\ThanksFor.docx")
        print("致谢页已生成......")



if __name__=='__main__':
    A=Thanksfor()
    content1=input("请输入段落1内容:")
    content2=input("请输入段落2内容:")
    content3=input("请输入段落3内容")
    name=input("请输入您的姓名:")
    year=input("请输入致谢年份:")
    month=input("请输入致谢月份:")
    day=input("请输入致谢日期:")
    A.Save_Thanksfor(content1,content2,content3,name,year,month,day)
