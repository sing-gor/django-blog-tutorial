# 从django的快捷方法中 导入 渲染方法
from django.shortcuts import render
from services.site_data import SiteData
# 在这里创建你的视图
# Create your views here.
site_data = SiteData('http://127.0.0.1:8000')
context = {}
context['site_data'] = site_data

# 定义一个名为home的函数，参数为 request 请求
def home(request):

    # 返回  渲染 home.html 文件 来响应这个请求
    return render(request,'home.html', context=context)

def index(request):

    return render(request,'index.html',context=context)

def show_1(request):

    return render(request,'show_1.html',context=context)

def show_2(request):

    return render(request,'show_2.html',context=context)

def show_3(request):

    return render(request,'show_3.html',context=context)

def show_4(request):

    return render(request,'show_4.html',context=context)
