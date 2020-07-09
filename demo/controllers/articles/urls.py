from django.urls import path
from controllers.articles import views
urlpatterns = [
    path('', views.index, name='article_index'),
    path('<id>',views.show,name='article_show')
]
