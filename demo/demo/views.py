# 从django的快捷方法中 导入 渲染方法
from django.shortcuts import render

# 在这里创建你的视图
# Create your views here.

# 定义一个名为home的函数，参数为 request 请求
def home(request):

    # 返回  根据请求渲染 home.html 文件
    return render(request,'home.html')

def index(request):

    return render(request,'index.html')

def show_1(request):

    return render(request,'show_1.html')

def show_2(request):

    return render(request,'show_2.html')

def show_3(request):

    return render(request,'show_3.html')

def show_4(request):

    return render(request,'show_4.html')
