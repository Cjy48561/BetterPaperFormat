# 如何实现可视化以及相关界面设计？
# 如何实现应用内实时预览docx文档
# 利用python与office实现更好的论文格式
# Using python and office to realize better paper format
from TitlePage import TitlePage
from Abstract import Abstract
from Abstractfy import AbstractFy

if __name__=='__main__':
    # 类实例化并调用函数（标题页）
    TiPg=TitlePage()
    TiPg.Save_TitlePage(Title_Name=input("请输入题目:"),
                        Institution_Name=input("请输入院系名:"),
                        Class_Name=input("请输入班级名:"),
                        Student_Name=input("请输入学生名:"),
                        Student_Number=input("请输入学号:"),
                        Guide_Teacher=input("请输入指导教师名:"),
                        DT_1=input("请输入答辩教师名1:"),DT_2=input("请输入答辩教师名2:"),DT_3=input("请输入答辩教师名3:"),
                        year=input("请输入年份:"),month=input("请输入月份:"))
    # 摘要页相关变量设置
    content1 = input("请输入正文段落1内容:")
    content2 = input("请输入正文段落2内容:")
    content3 = input("请输入正文段落3内容:")
    key1 = input("请输入关键词1:")
    key2 = input("请输入关键词2:")
    key3 = input("请输入关键词3:")
    key4 = input("请输入关键词4:")
    key5 = input("请输入关键词5:")
    # 类实例化并调用函数（中文摘要页）
    Abst=Abstract()
    Abst.Save_Abstract(
        content1,content2,content3,
        key1,key2,key3,key4,key5)
    # 类实例化并调用函数（英文摘要页）
    Abst_fy=AbstractFy()
    Abst_fy.fyA(content1=content1,content2=content2,content3=content3,
                key1=key1,key2=key2,key3=key3,key4=key4,key5=key5)


