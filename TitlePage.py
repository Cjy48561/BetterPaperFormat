# -*- coding: utf-8 -*-            
# @Author : yunwenwu
# @Time : 2022/12/6 9:25
# 导入相关模块
from docxtpl import DocxTemplate

class TitlePage:

    def Save_TitlePage(self,Title_Name,Institution_Name,Class_Name,Student_Name,Student_Number,Guide_Teacher,DT_1,DT_2,DT_3,year,month):
        # 加载模板文件
        tpl=DocxTemplate(".\\Standard Document\\Title Page.docx")
        # 渲染主体
        context={'TitleName':Title_Name,
                 'InstitutionName':Institution_Name,
                 'ClassName':Class_Name,
                 'StudentName':Student_Name,
                 'StudentNumber':Student_Number,
                 'GuideTeacher':Guide_Teacher,
                 'DT1':DT_1,'DT2':DT_2,'DT3':DT_3,
                 'Year':year,'Month':month
                 }
        # 将渲染主体加载到模板文件
        tpl.render(context)
        # 提示信息and保存文件
        print("标题页已生成...")
        tpl.save(".\\Generate document\\Title Page.docx")