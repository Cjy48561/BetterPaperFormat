# 利用python与office实现更好的论文格式
# Using python and office to realize better paper format
from TitlePage import TitlePage
from Abstract import Abstract

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
    # 类实例化并调用函数（中文摘要页）
    Abst=Abstract()
    Abst.Save_Abstract(
        content1=input("请输入正文段落1内容:"),
        content2=input("请输入正文段落2内容:"),
        content3=input("请输入正文段落3内容:"),
        key1=input("请输入关键词1:"),
        key2=input("请输入关键词2:"),
        key3=input("请输入关键词3:"),
        key4=input("请输入关键词4:"),
        key5=input("请输入关键词5:")
    )