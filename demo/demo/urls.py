"""demo URL Configuration # demo项目的路由构造

注： 这个多行注释的规范是 上英下中

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/

urlpatterns 中文含义是 路由模式

URLs 中文含义是 网址

views 中文含义是 视图

路由模式列表 是 用来存放 网址到视图的路线规则，更多详情请查看

https://docs.djangoproject.com/en/3.0/topics/http/urls/

Examples:
例子

Function views
函数视图

    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

    1. 加入一个 导入： 从我的应用中导入 视图文件
    2。加入一个网址到 路由模式 列表中，例如 路径（'', 视图文件中的home方法，路由名为home）

Class-based views
基于类视图

    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

    1. 加入一个导入 ： 从我的其他应用中的视图文件中 导入 Home类
    2. 加入一个网址到 路由模式 列表中，例如 路径（'', 将Home类实例化，路由名为home）

Including another URLconf
收录其他路由模式列表

    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    1. 导入 收录 方法，： 从django的路由中导入 收录，路径方法
    2. 加入一个 路由模式， 路径（'blog/'，收录（‘blog目录下的urls文件’））
"""
from django.urls import path
from demo import views
urlpatterns = [
    # http://127.0.0.1:8000
    path('', views.home),

    # http://127.0.0.1:8000/articles
    path('articles/',views.index),

    # http://127.0.0.1:8000/articles/1
    path('articles/1',views.show_1),

    # http://127.0.0.1:8000/articles/2
    path('articles/2',views.show_2),

    # http://127.0.0.1:8000/articles/3
    path('articles/3',views.show_3),
    
    # http://127.0.0.1:8000/articles/4
    path('articles/4',views.show_4),

]
