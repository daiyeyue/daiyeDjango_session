from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView

# class StudentListView(ListView):
#     """
#     需要设置两个主要内容
#     1. queryset   数据来源集合
#     2. template_name 模板名称
#
#     """
#     queryset = Student.objects.all()
#     template_name = "student_list.html"
#
#
# # Create your views here.
# def mySess(request):
#     print(type(request.session))
#     print(request.session)
#     # 如果session中没有teacher_name的值，返回NoName
#     print(request.session.get("teacher_name", "NoName"))
#     print("My sess")
#     return None
#
#
# def student(request):
#     """
#     请求所有学生的详情列表
#     @param request:
#     @return:
#     """
#     # 大约有10000名学生
#     stus = Student.objects.all()
#
#     # 使用分页器，两个参数
#     # 1. 数据来源，也即数据库查询出的结果
#     # 2. 单页返回的数据量
#     p = Paginator(stus, 40)
#
#     # 对Paginator进行设置或者对变量属性使用
#     print(p.count) # p里面有多少数据
#     print(p.num_pages) # 有多少个页面
#     print(p.page_range) # 页码列表，从1开始
#
#     # 取得第三页内容
#     # 如果页码不存在，则返回InvalidPage
#     return stus


